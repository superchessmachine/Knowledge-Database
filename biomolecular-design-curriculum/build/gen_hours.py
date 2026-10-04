#!/usr/bin/env python3
"""Generate the runtime-budget section from the assembled parts."""
import re, sys, pathlib, glob, collections

PARTS = [
    ("Part I — Foundations",            r'^(1[02468]|18)_'),
    ("Part II — The Method Atlas",      r'^(4[0-9]|5[0-9]|6[0-9])_'),
    ("Part III — Upstream AI Research", r'^(7[0-9]|8[0-4])_'),
    ("Part IV — Performance Engineering", r'^8[5-9]_'),
    ("Part V — Contribution",           r'^9[01]_'),
    ("Part VI — Appendices",            r'^9[2-9]_'),
]
DUR = re.compile(r'(?<![\d:])(\d{1,2}):([0-5]\d):([0-5]\d)(?![\d:])'
                 r'|(?<![\d:])(\d{1,3}):([0-5]\d)(?![\d:])')

def secs_in(t):
    s = n = 0
    for m in DUR.finditer(t):
        v = (int(m.group(1))*3600 + int(m.group(2))*60 + int(m.group(3))
             if m.group(1) else int(m.group(4))*60 + int(m.group(5)))
        if 60 <= v <= 5*3600:
            s += v; n += 1
    return s, n

def main(d, dst):
    d = pathlib.Path(d)
    files = sorted(p for p in d.glob("[0-9][0-9]_*.md"))
    tot_s = tot_n = 0
    rows = []
    for label, pat in PARTS:
        s = n = 0
        for f in files:
            if re.match(pat, f.name):
                a, b = secs_in(f.read_text()); s += a; n += b
        if n:
            rows.append((label, s, n)); tot_s += s; tot_n += n
    vids = len(set(re.findall(r'youtu(?:\.be/|be\.com/watch\?v=)([A-Za-z0-9_-]{11})',
                              "".join(f.read_text() for f in files))))
    H = tot_s/3600
    L = ["## 0.9 How long this is, honestly", "",
         f"**{vids:,} individual videos. About {H:,.0f} hours of timed runtime**, plus the",
         "enumerated courses whose lectures are listed without durations. Call it three",
         "thousand hours.", "",
         "That number is not a target. It is the size of the field's recorded output in",
         "the areas this document covers, and stating it plainly is more useful than",
         "pretending there is a schedule. At ten hours a week it is roughly six years; at",
         "twenty it is three. **Nobody should watch all of it, and the document is not",
         "built on the assumption that anyone will.**", "",
         "| Part | Timed hours | Timed items |", "|---|---:|---:|"]
    for label, s, n in rows:
        L.append(f"| {label} | {s/3600:,.0f} | {n:,} |")
    L.append(f"| **Total** | **{H:,.0f}** | **{tot_n:,}** |")
    L += ["",
      "### What to actually do with it", "",
      "**The 150-hour core.** If you do nothing else, do these: the matrix-calculus",
      "course in B.1, Kardar's statistical mechanics in B.2, the classical prediction",
      "course enumerated in Atlas L.1, the BUILD block of Atlas B and Atlas S, and the",
      "paired-reading tables for Atlas P, Q and R. That is about a hundred and fifty",
      "hours and it is the difference between running tools and understanding them.", "",
      "**The reference mode.** Everything else is a reference. When you hit a method you",
      "do not understand, open its family, watch the two or three talks flagged in bold,",
      "read the paired paper, and move on. The Atlas is organized by problem precisely",
      "so that this works.", "",
      "**The standing diet.** One talk a week from Part III, permanently, chosen from the",
      "archives in Appendix A. The point is not to keep up. It is to keep the vocabulary",
      "live so that when a transfer is available you recognize it.", "",
      "**The thing that actually converts hours into ability** is none of the above. It",
      "is the sixty-three derivation checkpoints and the nineteen BUILD blocks. A hundred",
      "hours of watching with ten checkpoints completed beats a thousand hours of",
      "watching with none, and it is not close."]
    pathlib.Path(dst).write_text("\n".join(L) + "\n")
    print(f"hours: {H:,.0f} across {tot_n:,} timed items, {vids:,} videos")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
