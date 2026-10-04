#!/usr/bin/env python3
"""Build the curriculum progress-tracker workbook."""
import json, re, sys, pathlib, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

INK   = "1F2937"; MUTED = "6B7280"; LINE = "D1D5DB"
PART_COLOR = {
    "Part I":   "E8F0FE", "Part II":  "E6F4EA", "Part III": "FFF4E5",
    "Part IV":  "F3E8FF", "Part V":   "FCE8E6", "Part VI":  "ECEFF1",
}
HEAD_FILL = PatternFill("solid", fgColor=INK)
HEAD_FONT = Font(color="FFFFFF", bold=True, size=11)
TITLE_FONT = Font(bold=True, size=18, color=INK)
SUB_FONT = Font(size=11, color=MUTED)
THIN = Side(style="thin", color=LINE)
BORDER = Border(bottom=THIN)

def part_key(p):
    m = re.match(r'(Part [IVX]+)', p or "")
    return m.group(1) if m else "Part VI"

def fmt_dur(sec):
    if not sec: return ""
    h, r = divmod(int(sec), 3600); m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def style_header(ws, row, ncols, height=28):
    ws.row_dimensions[row].height = height
    for c in range(1, ncols+1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEAD_FILL; cell.font = HEAD_FONT
        cell.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)

def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w

def build(data, out):
    V = data["videos"]
    wb = Workbook(); wb.remove(wb.active)

    # ---------- de-duplicate, keep first appearance, record other sections ----------
    first, extra = {}, collections.defaultdict(list)
    for v in V:
        k = v["vid"]
        if k not in first:
            first[k] = dict(v)
        else:
            if v["section"] != first[k]["section"]:
                extra[k].append(v["section"])
            if not first[k]["secs"] and v["secs"]: first[k]["secs"] = v["secs"]
            if not first[k]["speaker"] and v["speaker"]: first[k]["speaker"] = v["speaker"]
            if v["star"]: first[k]["star"] = True
    rows = list(first.values())

    # =====================================================================
    # 1. START HERE
    # =====================================================================
    ws = wb.create_sheet("Start Here")
    widths(ws, {"A": 3, "B": 34, "C": 92})
    ws["B2"] = "The Biomolecular Design Curriculum"; ws["B2"].font = TITLE_FONT
    ws["B3"] = "Progress tracker · third edition · compiled October 2026"; ws["B3"].font = SUB_FONT
    ws.merge_cells("B2:C2"); ws.merge_cells("B3:C3")

    total_secs = sum(v["secs"] or 0 for v in rows)
    facts = [
        ("What this is",
         "A multi-year self-study program in every computational method for proteins, DNA and RNA, "
         "the AI research upstream of it, and the engineering that makes it fast."),
        ("Videos tracked", f"{len(rows):,} unique talks and lectures"),
        ("Timed runtime", f"about {total_secs/3600:,.0f} hours (not every entry carries a duration)"),
        ("Papers paired", f"{len(data['papers']):,} citations, linked to the section that discusses them"),
        ("Watch-then-read pairs", f"{len(data['paired']):,} — the core study device of this curriculum"),
        ("Derivation checkpoints", f"{len(data['checkpoints'])} — these are what convert watching into ability"),
        ("Capstone projects", f"{len(data['capstones'])}"),
        ("", ""),
        ("HOW TO USE THIS", ""),
        ("1 · Progress Tracker",
         "The main sheet. Every video in reading order. Set Status to Watching or Done and the "
         "Dashboard updates itself. Filter by Part, Section or Priority to carve out a study block."),
        ("2 · Core Path",
         "If you do nothing else, do this. Roughly 150 hours that take you from running tools to "
         "understanding them."),
        ("3 · Dashboard", "Live completion by Part and by Section. Formula-driven; do not type into it."),
        ("4 · Paired Reading",
         "Watch this, then read that, holding this question. The single most useful device here — "
         "the gap between a talk and its paper is where the real understanding sits."),
        ("5 · Checkpoints",
         "73 things to derive from a blank page. Only the third state — 'can reproduce from blank "
         "paper' — counts."),
        ("6 · Capstones", "11 projects, each cross-referenced from the family that motivates it."),
        ("7 · Papers", "Every citation, by section."),
        ("8 · Sections", "The full table of contents with counts and hours."),
        ("", ""),
        ("A note on the hours",
         "The runtime figure is not a target. It is the size of the field's recorded output. Nobody "
         "should watch all of it and this is not built on the assumption that anyone will. Treat it "
         "as a reference you work through and keep returning to."),
        ("Priority column",
         "★ marks entries the curriculum flags as the ones to watch first within their section."),
        ("Dead links",
         "Checked October 2026: none dead. A small number have embedding disabled, which means they "
         "play on YouTube but cannot be iframed."),
    ]
    r = 5
    for k, v in facts:
        if k and not v:
            ws.cell(r, 2, k).font = Font(bold=True, size=12, color=INK)
        else:
            ws.cell(r, 2, k).font = Font(bold=True, size=10, color=INK)
            c = ws.cell(r, 3, v); c.font = Font(size=10); c.alignment = Alignment(wrap_text=True, vertical="top")
            ws.row_dimensions[r].height = max(15, 13 * (1 + len(v)//95))
        r += 1
    ws.sheet_view.showGridLines = False

    # =====================================================================
    # 2. PROGRESS TRACKER
    # =====================================================================
    tr = wb.create_sheet("Progress Tracker")
    hdr = ["#", "Part", "Section", "Title", "Speaker / host", "Duration", "Hours",
           "Priority", "Status", "Date done", "Notes", "Watch", "Also appears in"]
    tr.append(hdr); style_header(tr, 1, len(hdr))
    for i, v in enumerate(rows, 1):
        pk = part_key(v["part"])
        tr.append([i, v["part"], v["section"], v["title"], v["speaker"],
                   fmt_dur(v["secs"]), round((v["secs"] or 0)/3600, 2),
                   "★" if v["star"] else "", "Not started", None, "",
                   f'https://www.youtube.com/watch?v={v["vid"]}',
                   "; ".join(sorted(set(extra[v["vid"]]))[:4])])
        rr = i + 1
        fill = PatternFill("solid", fgColor=PART_COLOR.get(pk, "FFFFFF"))
        for c in range(1, len(hdr)+1):
            cell = tr.cell(rr, c); cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=(c in (3, 4, 5, 11, 13)))
            if c in (1, 2, 3): cell.fill = fill
        lk = tr.cell(rr, 12)
        lk.hyperlink = lk.value; lk.value = "▶ watch"
        lk.font = Font(color="1A56DB", underline="single")
        tr.cell(rr, 8).alignment = Alignment(horizontal="center")
        tr.cell(rr, 10).number_format = "yyyy-mm-dd"
    n = len(rows) + 1
    widths(tr, {"A": 6, "B": 22, "C": 30, "D": 62, "E": 30, "F": 10, "G": 8,
                "H": 9, "I": 13, "J": 12, "K": 34, "L": 11, "M": 28})
    tr.freeze_panes = "D2"; tr.auto_filter.ref = f"A1:M{n}"
    dv = DataValidation(type="list", formula1='"Not started,Watching,Done,Skipped"', allow_blank=True)
    tr.add_data_validation(dv); dv.add(f"I2:I{n}")
    tr.conditional_formatting.add(f"I2:I{n}",
        CellIsRule(operator="equal", formula=['"Done"'],
                   fill=PatternFill("solid", fgColor="C6E7CE"), font=Font(color="14532D", bold=True)))
    tr.conditional_formatting.add(f"I2:I{n}",
        CellIsRule(operator="equal", formula=['"Watching"'],
                   fill=PatternFill("solid", fgColor="FDF0C8"), font=Font(color="7A5B00", bold=True)))
    tr.conditional_formatting.add(f"I2:I{n}",
        CellIsRule(operator="equal", formula=['"Skipped"'],
                   fill=PatternFill("solid", fgColor="EDEDED"), font=Font(color="7A7A7A", italic=True)))
    tr.conditional_formatting.add(f"A2:H{n}",
        FormulaRule(formula=[f'$I2="Done"'], font=Font(color="9AA0A6", strike=True)))

    # =====================================================================
    # 3. DASHBOARD
    # =====================================================================
    db = wb.create_sheet("Dashboard")
    widths(db, {"A": 3, "B": 34, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 14})
    db["B2"] = "Progress"; db["B2"].font = TITLE_FONT
    db["B3"] = "Driven by the Status column on Progress Tracker. Nothing here needs editing."
    db["B3"].font = SUB_FONT
    T = f"'Progress Tracker'"
    db["B5"] = "OVERALL"; db["B5"].font = Font(bold=True, size=12, color=INK)
    overall = [("Videos total", f"=COUNTA({T}!A2:A{n})"),
               ("Done",         f'=COUNTIF({T}!$I$2:$I${n},"Done")'),
               ("Watching",     f'=COUNTIF({T}!$I$2:$I${n},"Watching")'),
               ("Skipped",      f'=COUNTIF({T}!$I$2:$I${n},"Skipped")'),
               ("Percent done", f'=IFERROR(COUNTIF({T}!$I$2:$I${n},"Done")/COUNTA({T}!A2:A{n}),0)'),
               ("Hours total",  f"=ROUND(SUM({T}!$G$2:$G${n}),0)"),
               ("Hours done",   f'=ROUND(SUMIF({T}!$I$2:$I${n},"Done",{T}!$G$2:$G${n}),1)')]
    r = 6
    for label, f in overall:
        db.cell(r, 2, label).font = Font(bold=True, size=10)
        c = db.cell(r, 3, f)
        c.number_format = "0.0%" if "Percent" in label else "#,##0"
        c.font = Font(size=10); r += 1

    r += 2
    db.cell(r, 2, "BY PART").font = Font(bold=True, size=12, color=INK)
    r += 1
    for j, h in enumerate(["Part", "Videos", "Done", "% done", "Hours", "Hrs done"]):
        db.cell(r, 2+j, h)
    style_header(db, r, 7, height=22)
    hdr_r = r; r += 1
    for pk in ["Part I", "Part II", "Part III", "Part IV", "Part V", "Part VI"]:
        db.cell(r, 2, pk).fill = PatternFill("solid", fgColor=PART_COLOR[pk])
        db.cell(r, 2).font = Font(bold=True, size=10)
        db.cell(r, 3, f'=COUNTIF({T}!$B$2:$B${n},$B{r}&"*")')
        db.cell(r, 4, f'=COUNTIFS({T}!$B$2:$B${n},$B{r}&"*",{T}!$I$2:$I${n},"Done")')
        db.cell(r, 5, f'=IFERROR(D{r}/C{r},0)').number_format = "0.0%"
        db.cell(r, 6, f'=ROUND(SUMIF({T}!$B$2:$B${n},$B{r}&"*",{T}!$G$2:$G${n}),0)')
        db.cell(r, 7, f'=ROUND(SUMIFS({T}!$G$2:$G${n},{T}!$B$2:$B${n},$B{r}&"*",{T}!$I$2:$I${n},"Done"),1)')
        for c in range(2, 8): db.cell(r, c).border = BORDER
        r += 1
    db.conditional_formatting.add(f"E{hdr_r+1}:E{r-1}",
        CellIsRule(operator="greaterThan", formula=["0.999"],
                   fill=PatternFill("solid", fgColor="C6E7CE")))

    r += 2
    db.cell(r, 2, "BY SECTION").font = Font(bold=True, size=12, color=INK)
    r += 1
    for j, h in enumerate(["Section", "Videos", "Done", "% done", "Hours"]):
        db.cell(r, 2+j, h)
    style_header(db, r, 6, height=22)
    r += 1
    sec_order, sec_count = [], collections.Counter()
    for v in rows:
        if v["section"] not in sec_count: sec_order.append(v["section"])
        sec_count[v["section"]] += 1
    for s in sec_order:
        db.cell(r, 2, s).font = Font(size=9)
        db.cell(r, 2).alignment = Alignment(wrap_text=True, vertical="top")
        db.cell(r, 3, f'=COUNTIF({T}!$C$2:$C${n},$B{r})')
        db.cell(r, 4, f'=COUNTIFS({T}!$C$2:$C${n},$B{r},{T}!$I$2:$I${n},"Done")')
        db.cell(r, 5, f'=IFERROR(D{r}/C{r},0)').number_format = "0.0%"
        db.cell(r, 6, f'=ROUND(SUMIF({T}!$C$2:$C${n},$B{r},{T}!$G$2:$G${n}),1)')
        for c in range(2, 7): db.cell(r, c).border = BORDER
        r += 1
    db.sheet_view.showGridLines = False

    # =====================================================================
    # 4. CORE PATH
    # =====================================================================
    CORE_HINTS = ["B.1", "B.2", "B.3", "B.4", "Atlas B", "Atlas L", "Atlas S",
                  "Atlas P", "Atlas Q", "Atlas R", "E.4", "E.6"]
    core = [v for v in rows if v["star"] and any(v["section"].startswith(h) for h in CORE_HINTS)]
    cp = wb.create_sheet("Core Path")
    cp["A1"] = "The core path"; cp["A1"].font = TITLE_FONT
    cp["A2"] = ("The flagged essentials from the foundations, the classical and learned prediction "
                "families, design, benchmarking and performance. If you do nothing else, do these.")
    cp["A2"].font = SUB_FONT; cp.merge_cells("A1:G1"); cp.merge_cells("A2:G2")
    cp.append([]); hdr2 = ["#", "Section", "Title", "Speaker / host", "Duration", "Status", "Watch"]
    cp.append(hdr2); style_header(cp, 4, len(hdr2))
    for i, v in enumerate(core, 1):
        cp.append([i, v["section"], v["title"], v["speaker"], fmt_dur(v["secs"]), "Not started",
                   f'https://www.youtube.com/watch?v={v["vid"]}'])
        rr = i + 4
        lk = cp.cell(rr, 7); lk.hyperlink = lk.value; lk.value = "▶ watch"
        lk.font = Font(color="1A56DB", underline="single")
        for c in range(1, 8):
            cp.cell(rr, c).border = BORDER
            cp.cell(rr, c).alignment = Alignment(vertical="top", wrap_text=(c in (2, 3, 4)))
    cn = len(core) + 4
    widths(cp, {"A": 6, "B": 30, "C": 66, "D": 30, "E": 10, "F": 13, "G": 11})
    cp.freeze_panes = "A5"; cp.auto_filter.ref = f"A4:G{cn}"
    dv2 = DataValidation(type="list", formula1='"Not started,Watching,Done,Skipped"', allow_blank=True)
    cp.add_data_validation(dv2); dv2.add(f"F5:F{cn}")
    cp.conditional_formatting.add(f"F5:F{cn}",
        CellIsRule(operator="equal", formula=['"Done"'],
                   fill=PatternFill("solid", fgColor="C6E7CE"), font=Font(color="14532D", bold=True)))
    cp.sheet_view.showGridLines = False

    # =====================================================================
    # 5. PAIRED READING
    # =====================================================================
    pr = wb.create_sheet("Paired Reading")
    pr["A1"] = "Watch this, then read that"; pr["A1"].font = TITLE_FONT
    pr["A2"] = ("The core study device. Watch the talk, read the paper it narrates, and write the gap "
                "between them. The question in the last column is what to hold while you do it.")
    pr["A2"].font = SUB_FONT; pr.merge_cells("A1:F1"); pr.merge_cells("A2:F2")
    pr.append([]); h3 = ["#", "Part", "Section", "Watch this", "Then read this", "Hold this question", "Done"]
    pr.append(h3); style_header(pr, 4, len(h3))
    for i, p in enumerate(data["paired"], 1):
        pr.append([i, p["part"], p["section"], p["watch"], p["read"], p["question"], ""])
        rr = i + 4
        for c in range(1, 8):
            pr.cell(rr, c).border = BORDER
            pr.cell(rr, c).alignment = Alignment(vertical="top", wrap_text=(c in (3, 4, 5, 6)))
        pr.cell(rr, 2).fill = PatternFill("solid", fgColor=PART_COLOR.get(part_key(p["part"]), "FFFFFF"))
    pn = len(data["paired"]) + 4
    widths(pr, {"A": 6, "B": 20, "C": 26, "D": 46, "E": 46, "F": 54, "G": 9})
    pr.freeze_panes = "D5"; pr.auto_filter.ref = f"A4:G{pn}"
    dv3 = DataValidation(type="list", formula1='"Yes"', allow_blank=True)
    pr.add_data_validation(dv3); dv3.add(f"G5:G{pn}")
    pr.sheet_view.showGridLines = False

    # =====================================================================
    # 6. CHECKPOINTS
    # =====================================================================
    ck = wb.create_sheet("Checkpoints")
    ck["A1"] = "Derivation checkpoints"; ck["A1"].font = TITLE_FONT
    ck["A2"] = ("Things to derive from a blank page. Three states, and only the third counts: "
                "not started, attempted, can reproduce from blank paper.")
    ck["A2"].font = SUB_FONT; ck.merge_cells("A1:E1"); ck.merge_cells("A2:E2")
    ck.append([]); h4 = ["#", "Family", "What to derive", "State", "Date"]
    ck.append(h4); style_header(ck, 4, len(h4))
    for c in sorted(data["checkpoints"], key=lambda x: x["num"]):
        ck.append([c["num"], c["section"], c["text"], "Not started", None])
        rr = ck.max_row
        for col in range(1, 6):
            ck.cell(rr, col).border = BORDER
            ck.cell(rr, col).alignment = Alignment(vertical="top", wrap_text=(col in (2, 3)))
        ck.cell(rr, 5).number_format = "yyyy-mm-dd"
    kn = ck.max_row
    widths(ck, {"A": 6, "B": 34, "C": 108, "D": 22, "E": 12})
    ck.freeze_panes = "A5"; ck.auto_filter.ref = f"A4:E{kn}"
    dv4 = DataValidation(type="list",
        formula1='"Not started,Attempted,Can reproduce from blank paper"', allow_blank=True)
    ck.add_data_validation(dv4); dv4.add(f"D5:D{kn}")
    ck.conditional_formatting.add(f"D5:D{kn}",
        CellIsRule(operator="equal", formula=['"Can reproduce from blank paper"'],
                   fill=PatternFill("solid", fgColor="C6E7CE"), font=Font(color="14532D", bold=True)))
    ck.conditional_formatting.add(f"D5:D{kn}",
        CellIsRule(operator="equal", formula=['"Attempted"'],
                   fill=PatternFill("solid", fgColor="FDF0C8")))
    ck.sheet_view.showGridLines = False

    # =====================================================================
    # 7. CAPSTONES
    # =====================================================================
    cs = wb.create_sheet("Capstones")
    cs["A1"] = "Capstone projects"; cs["A1"].font = TITLE_FONT
    cs["A2"] = "Begin each as soon as its prerequisite families are done. Do not wait until the end."
    cs["A2"].font = SUB_FONT; cs.merge_cells("A1:E1"); cs.merge_cells("A2:E2")
    cs.append([]); h5 = ["#", "Project", "Start after", "What it is", "Status"]
    cs.append(h5); style_header(cs, 4, len(h5))
    for c in data["capstones"]:
        cs.append([c["num"], c["name"], c["when"], c["text"], "Not started"])
        rr = cs.max_row
        for col in range(1, 6):
            cs.cell(rr, col).border = BORDER
            cs.cell(rr, col).alignment = Alignment(vertical="top", wrap_text=(col in (2, 3, 4)))
    sn = cs.max_row
    widths(cs, {"A": 6, "B": 34, "C": 26, "D": 104, "E": 16})
    cs.freeze_panes = "A5"
    dv5 = DataValidation(type="list", formula1='"Not started,In progress,Done"', allow_blank=True)
    cs.add_data_validation(dv5); dv5.add(f"E5:E{sn}")
    cs.sheet_view.showGridLines = False

    # =====================================================================
    # 8. PAPERS
    # =====================================================================
    pp = wb.create_sheet("Papers")
    pp["A1"] = "Paired papers"; pp["A1"].font = TITLE_FONT
    pp["A2"] = "Every citation in the curriculum, with the section that discusses it."
    pp["A2"].font = SUB_FONT; pp.merge_cells("A1:D1"); pp.merge_cells("A2:D2")
    pp.append([]); h6 = ["#", "Part", "Section", "Citation", "Read"]
    pp.append(h6); style_header(pp, 4, len(h6))
    for i, p in enumerate(data["papers"], 1):
        pp.append([i, p["part"], p["section"], p["citation"], ""])
        rr = i + 4
        for c in range(1, 6):
            pp.cell(rr, c).border = BORDER
            pp.cell(rr, c).alignment = Alignment(vertical="top", wrap_text=(c in (3, 4)))
        pp.cell(rr, 2).fill = PatternFill("solid", fgColor=PART_COLOR.get(part_key(p["part"]), "FFFFFF"))
    ppn = len(data["papers"]) + 4
    widths(pp, {"A": 6, "B": 20, "C": 28, "D": 96, "E": 9})
    pp.freeze_panes = "A5"; pp.auto_filter.ref = f"A4:E{ppn}"
    dv6 = DataValidation(type="list", formula1='"Yes"', allow_blank=True)
    pp.add_data_validation(dv6); dv6.add(f"E5:E{ppn}")
    pp.sheet_view.showGridLines = False

    # =====================================================================
    # 9. SECTIONS
    # =====================================================================
    sx = wb.create_sheet("Sections")
    sx["A1"] = "Table of contents"; sx["A1"].font = TITLE_FONT
    sx["A2"] = "Every section, in document order, with what it holds."
    sx["A2"].font = SUB_FONT; sx.merge_cells("A1:E1"); sx.merge_cells("A2:E2")
    sx.append([]); h7 = ["#", "Part", "Section", "Videos", "Hours"]
    sx.append(h7); style_header(sx, 4, len(h7))
    sec_part, sec_secs = {}, collections.Counter()
    for v in rows:
        sec_part.setdefault(v["section"], v["part"])
        sec_secs[v["section"]] += (v["secs"] or 0)
    for i, s in enumerate(sec_order, 1):
        sx.append([i, sec_part[s], s, sec_count[s], round(sec_secs[s]/3600, 1)])
        rr = i + 4
        for c in range(1, 6):
            sx.cell(rr, c).border = BORDER
            sx.cell(rr, c).alignment = Alignment(vertical="top", wrap_text=(c == 3))
        sx.cell(rr, 2).fill = PatternFill("solid", fgColor=PART_COLOR.get(part_key(sec_part[s]), "FFFFFF"))
    widths(sx, {"A": 6, "B": 22, "C": 62, "D": 10, "E": 10})
    sx.freeze_panes = "A5"; sx.auto_filter.ref = f"A4:E{len(sec_order)+4}"
    sx.sheet_view.showGridLines = False

    wb.save(out)
    return len(rows), total_secs, len(sec_order), len(core)

if __name__ == "__main__":
    d = json.loads(pathlib.Path(sys.argv[1]).read_text())
    nv, ts, ns, nc = build(d, sys.argv[2])
    print(f"workbook written: {nv:,} videos | {ts/3600:,.0f} h | {ns} sections | core path {nc}")
