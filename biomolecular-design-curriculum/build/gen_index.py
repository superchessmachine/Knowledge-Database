#!/usr/bin/env python3
"""Generate the method/software index appendix from the assembled full.md."""
import re, sys, pathlib, collections

BLOCK = set("""
BPDMC RosettaCommons MLCB MLSB MIA IPD CECAM BioExcel EleutherAI NPTEL OCW IAS IPAM TTIC ICTP
NeurIPS ICML ICLR CVPR ICCV ECCV SIGGRAPH USENIX OSDI MLSys ISCA JMLR TMLR
PNAS JCTC JCP JACS JMB NAR RNA DNA PDB USA PDF URL HTTP AND THE FOR NOT BUILD CORE ONLY
UNVERIFIED MIT UCLA UCSF CMU NYU EPFL ETH JHU UCSD UW HMS CSAIL UIUC USC UCL TUM LMU IIT
DeepMind OpenAI NVIDIA Microsoft Google Meta Anthropic FAIR MSR CMSA TCBG MLST FAR MODE
AlQuraishi McCoy MacKay LeCun Jumper Baker Kortemme Bradley Bowman Zuckerman Chatterjee
III GCV GPT CNN PCA SAM MAE RMSD ODE SDE SEC ACL ACS ALIGN ALLODD IEEE JSON HTML CSS
ARXIV DOI ISBN FAQ API CPU RAM SSH PNG TBD TODO NOTE WARNING
""".split())

CANON = {
 "AlphaFold2":"AlphaFold 2","AlphaFold3":"AlphaFold 3","CASP14":"CASP",
 "ProteinMPNN":"ProteinMPNN","LigandMPNN":"LigandMPNN","ThermoMPNN":"ThermoMPNN",
}

def sections(text):
    """Yield (char_offset, label) for every numbered heading."""
    out=[]
    for m in re.finditer(r'^(#{1,3})\s+(.*)$', text, re.M):
        h=m.group(2).strip()
        lab=None
        a=re.match(r'(Atlas [A-S])\b\s*—\s*(.*)', h)
        b=re.match(r'([A-E]\.\d+(?:\.\d+)?)\s+(.*)', h)
        c=re.match(r'([A-S]\.\d+)\s+(.*)', h)
        d=re.match(r'(DLT-\d+(?:\.\d+)?)\s+(.*)', h)
        e=re.match(r'(Appendix [A-Z])\b\s*—\s*(.*)', h)
        for mm in (a,b,c,d,e):
            if mm: lab=mm.group(1); break
        if lab:
            mm=re.match(r'Atlas ([A-S])$', lab)
            if mm: lab=mm.group(1)+'.0'
            out.append((m.start(), lab))
    return out

def main(src, dst):
    raw = pathlib.Path(src).read_text()
    # blank out URLs and inline code so video IDs and paths never enter the index
    t = re.sub(r'https?://\S+', lambda m: ' '*len(m.group(0)), raw)
    t = re.sub(r'`[^`\n]*`', lambda m: ' '*len(m.group(0)), t)
    secs = sections(t)
    offs = [o for o,_ in secs]
    import bisect
    def sec_at(pos):
        i = bisect.bisect_right(offs, pos) - 1
        return secs[i][1] if i >= 0 else None

    pat = re.compile(r'\b(?:[A-Z][a-z]+(?:[A-Z][a-zA-Z0-9]+)+|[A-Z]{3,}[0-9]*'
                     r'|[A-Z][a-zA-Z]*(?:Fold|MPNN|Diff|Flow|Net|Craft|Dock|Gen|Bench|Gym)[a-zA-Z0-9-]*)\b')
    hits = collections.defaultdict(set)
    for m in pat.finditer(t):
        w = m.group(0)
        if w in BLOCK or len(w) < 3: continue
        s = sec_at(m.start())
        if s: hits[CANON.get(w, w)].add(s)

    def key(lab):
        m=re.match(r'Atlas ([A-S])', lab)
        if m: return (1, m.group(1), 0, 0)
        m=re.match(r'([A-Z])\.(\d+)(?:\.(\d+))?', lab)
        if m: return (0, m.group(1), int(m.group(2)), int(m.group(3) or 0))
        m=re.match(r'DLT-(\d+)(?:\.(\d+))?', lab)
        if m: return (2, "D", int(m.group(1)), int(m.group(2) or 0))
        m=re.match(r'Appendix ([A-Z])', lab)
        if m: return (3, m.group(1), 0, 0)
        return (4, lab, 0, 0)

    entries = {w: sorted(s, key=key) for w, s in hits.items() if len(s) >= 2}
    by_letter = collections.defaultdict(list)
    for w in sorted(entries, key=str.lower):
        by_letter[w[0].upper()].append(w)

    L = ["## Appendix E — Index of Methods, Software and Systems", "",
         f"Every named method, model, package and system that appears in at least two",
         f"places, with the sections that discuss it. **{len(entries)} entries.** Generated",
         "from the assembled text at build time, so it cannot drift out of date.", "",
         "Section labels: `Atlas A`–`Atlas S` are the method families in Part II;",
         "`B.n` are the foundation modules in Part I; `D.n` are the AI sections in",
         "Part III; `DLT-n` are the deep learning theory sections; `E.n` are the",
         "performance engineering sections in Part IV.", ""]
    for letter in sorted(by_letter):
        L.append(f"**{letter}**")
        L.append("")
        for w in by_letter[letter]:
            L.append(f"- {w} — {', '.join(entries[w])}")
        L.append("")
    pathlib.Path(dst).write_text("\n".join(L))
    print(f"index: {len(entries)} entries")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
