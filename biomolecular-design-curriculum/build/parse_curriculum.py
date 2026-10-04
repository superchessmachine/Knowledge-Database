#!/usr/bin/env python3
"""Parse the curriculum markdown into structured records for the workbook."""
import re, json, sys, pathlib, collections

VID = re.compile(r'youtu(?:\.be/|be\.com/watch\?v=)([A-Za-z0-9_-]{11})')
PLAY = re.compile(r'youtube\.com/playlist\?list=([A-Za-z0-9_-]+)')
DUR = re.compile(r'(?<![\d:])(\d{1,2}):([0-5]\d):([0-5]\d)(?![\d:])|(?<![\d:])(\d{1,3}):([0-5]\d)(?![\d:])')
MDLINK = re.compile(r'\[([^\]]*)\]\((https?://[^)]+)\)')

def dur_secs(text):
    m = DUR.search(text)
    if not m: return None
    s = (int(m.group(1))*3600 + int(m.group(2))*60 + int(m.group(3))
         if m.group(1) else int(m.group(4))*60 + int(m.group(5)))
    return s if 30 <= s <= 6*3600 else None

def fmt(sec):
    if sec is None: return ""
    h, r = divmod(int(sec), 3600); m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def clean(t):
    t = MDLINK.sub(r'\1', t)
    t = re.sub(r'https?://\S+', ' ', t)          # kill raw URLs
    t = re.sub(r'\[\s*\]\([^)]*\)', ' ', t)      # empty md links
    t = re.sub(r'[*_`]', '', t)
    t = t.replace('▶', '').replace('—', '-')
    t = re.sub(r'\(\s*\)', ' ', t)
    return re.sub(r'\s+', ' ', t).strip(' -·|()[]')

def usable(t):
    t = (t or '').strip()
    if len(t) < 4: return False
    if t.lower().startswith(('http', 'www.')): return False
    if re.fullmatch(r'[\d:\s.\-–—|]+', t): return False
    return True


PAPER_INLINE = re.compile(
    r'(?:\*\*|\*)?\s*(?:PAPERS?|Papers?)\s*:?\s*(?:\*\*|\*)?\s*(.+?)$', re.I)

def inline_paper(text):
    """Pull a 'Paper: ...' citation out of the same line/paragraph as a video."""
    m = re.search(r'(?:\*\*|\*)?\s*PAPERS?\s*:(?:\*\*|\*)?\s*(.+)', text, re.I)
    if not m: return ""
    cit = clean(m.group(1))
    cit = re.split(r'\s{2,}|\s\|\s', cit)[0]
    return cit[:300] if len(cit) > 10 else ""

def parse(path):
    lines = pathlib.Path(path).read_text().split("\n")
    part = section = sec_title = ""
    section_anchor = ""
    vids, papers, paired, checkpoints, capstones = [], [], [], [], []
    seen_order = {}
    i = 0
    while i < len(lines):
        raw = lines[i]; line = raw.rstrip()

        m = re.match(r'^# (Part [IVX]+.*)$', line)
        if m: part = clean(m.group(1)); i += 1; continue

        mc = re.match(r'^### ([IVX]+) [—-] (.+?)\s*(?:\*\(([^)]*)\)\*)?\s*$', line)
        if mc:
            body = []; j = i+1
            while j < len(lines) and not lines[j].startswith('###') and not lines[j].startswith('---'):
                body.append(lines[j]); j += 1
            capstones.append({"num": mc.group(1), "name": clean(mc.group(2)),
                              "when": clean(mc.group(3) or ""), "text": clean(" ".join(body))[:1500]})
            section = clean(mc.group(2)); i = j; continue

        m = re.match(r'^#{1,3} (.+)$', line)
        if m:
            h = clean(m.group(1))
            if not h.lower().startswith('part '):
                section = h
                sec_title = h
                if re.match(r'^C\.1\b', h): section_anchor = 'C.1'
                elif re.match(r'^C\.\d', h) or h.startswith('Appendix'): section_anchor = ''
            i += 1; continue

        # numbered derivation checkpoints
        m = re.match(r'^\s*(\d{1,3})\.\s+(\S.*)$', line)
        if m and 'C.1' in section_anchor:
            body = [line]
            j = i+1
            while j < len(lines) and lines[j].startswith("    "):
                body.append(lines[j]); j += 1
            checkpoints.append({"num": int(m.group(1)), "section": section,
                                "text": clean(" ".join(body))[:1200]})
            i = j; continue


        # papers blocks
        if line.lstrip().startswith("**Papers") or line.lstrip().startswith("**Paper:"):
            body = [line]; j = i+1
            while j < len(lines) and lines[j].strip() and not lines[j].startswith(('|','#','>')):
                body.append(lines[j]); j += 1
            txt = clean(" ".join(body))
            txt = re.sub(r'^Papers?:?\s*', '', txt)
            for cite in re.split(r'\s·\s', txt):
                cite = cite.strip(" .·")
                if len(cite) > 12:
                    papers.append({"part": part, "section": section, "citation": cite[:400]})
            i = j; continue

        # paired-reading tables
        if line.startswith('|') and 'Watch this' in line and 'read this' in line:
            j = i+2
            while j < len(lines) and lines[j].startswith('|'):
                c = [clean(x) for x in lines[j].strip('|').split('|')]
                if len(c) >= 3 and c[0]:
                    paired.append({"part": part, "section": section,
                                   "watch": c[0][:300], "read": c[1][:300], "question": c[2][:400]})
                j += 1
            i = j; continue

        # ---- videos ----
        if 'youtu' in line:
            if line.lstrip().startswith('|'):
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                url_cell = next((c for c in cells if VID.search(c)), "")
                for vm in VID.finditer(line):
                    vid = vm.group(1)
                    rest = [c for c in cells if c is not url_cell]
                    d = None
                    for c in cells:
                        if not VID.search(c) and dur_secs(c): d = dur_secs(c); break
                    if d is None: d = dur_secs(line)
                    cands = [clean(c) for c in rest
                             if clean(c) and not re.fullmatch(r'[—\-–]|\d{1,3}|\d{4}|[\d:]+|[★*]+', clean(c))
                             and not DUR.fullmatch(c.strip())]
                    cands = [c for c in cands if usable(c)]
                    title = max(cands, key=len) if cands else clean(MDLINK.sub(r'\1', url_cell)) or "(untitled)"
                    others = [c for c in cands if c != title]
                    speaker = ""
                    for c in others:
                        if re.search(r'[A-Z][a-z]+\s+[A-Z]', c) or '(' in c:
                            speaker = c; break
                    if not speaker and others: speaker = others[0]
                    star = '★' in line or '**' in line
                    tail = line[vm.end():] if vm.end() < len(line) else ""
                    yield_rec = {"part": part, "section": section, "title": title[:300],
                                 "speaker": speaker[:200], "secs": d, "vid": vid, "star": star,
                                 "paper": inline_paper(line)}
                    vids.append(yield_rec)
                i += 1; continue
            else:
                # unwrap the paragraph
                para = [line]; j = i+1
                while j < len(lines) and lines[j].strip() and 'youtu' in "".join(lines[max(0,j-1):j+2]) or \
                      (j < len(lines) and lines[j].strip() and not lines[j].startswith(('|','#','>','-')) and j-i < 12):
                    para.append(lines[j]); j += 1
                    if j < len(lines) and not lines[j].strip(): break
                blob = " ".join(para)
                for vm in VID.finditer(blob):
                    vid = vm.group(1)
                    before = blob[:vm.start()]
                    bolds = re.findall(r'\*\*(.+?)\*\*', before)
                    ital = re.findall(r'\*(.+?)\*', before)
                    title = clean(bolds[-1]) if bolds else (clean(ital[-1]) if ital else "")
                    if not usable(title):
                        tail = clean(before)
                        parts = [x.strip() for x in re.split(r'[·|]', tail) if usable(x.strip())]
                        title = parts[-1][-140:] if parts else "(see curriculum section)"
                    win = blob[max(0, vm.start()-160):vm.start()+60]
                    after = blob[vm.end():vm.end()+420]
                    vids.append({"part": part, "section": section, "title": title[:300],
                                 "speaker": "", "secs": dur_secs(win), "vid": vid,
                                 "star": '**' in before[-200:],
                                 "paper": inline_paper(after)})
                i = j; continue
        i += 1
    return vids, papers, paired, checkpoints, capstones

if __name__ == "__main__":
    v, pa, pr, ck, cp = parse(sys.argv[1])
    out = {"videos": v, "papers": pa, "paired": pr, "checkpoints": ck, "capstones": cp}
    pathlib.Path(sys.argv[2]).write_text(json.dumps(out))
    uniq = len({x["vid"] for x in v})
    print(f"video mentions {len(v)} | unique {uniq} | papers {len(pa)} | "
          f"paired {len(pr)} | checkpoints {len(ck)} | capstones {len(cp)}")
