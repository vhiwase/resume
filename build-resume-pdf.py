"""Render Vaibhav-Hiwase-Resume.md to a Google-style HTML resume.

Usage:  python build-resume-pdf.py <input.md> <output.html> [photo.png]
Then:   msedge --headless --disable-gpu --no-pdf-header-footer
                --print-to-pdf="out.pdf" "file:///<abs-path>/out.html"
"""
import re, io, html, sys, base64, pathlib

md_path, out_path = sys.argv[1], sys.argv[2]
photo_path = sys.argv[3] if len(sys.argv) > 3 else None
src = pathlib.Path(md_path).read_text(encoding="utf-8")

DATE_RE = re.compile(
    r"^(.*?)\s*·\s*((?:[A-Z][a-z]{2,4}\.?\s*)?\d{4}\s*[–-]\s*"
    r"(?:Present|(?:[A-Z][a-z]{2,4}\.?\s*)?\d{4}))\s*$"
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return LINK_RE.sub(r'<a href="\2">\1</a>', s)


def split_dates(text):
    m = DATE_RE.match(text)
    return (m.group(1), m.group(2)) if m else (text, None)


def photo_tag(path):
    """Downscale to a small square JPEG and embed as a data URI."""
    if not path or not pathlib.Path(path).exists():
        return ""
    try:
        from PIL import Image
    except ImportError:
        return ""
    img = Image.open(path).convert("RGB")
    side = min(img.size)
    left, top = (img.width - side) // 2, (img.height - side) // 2
    img = img.crop((left, top, left + side, top + side)).resize(
        (340, 340), Image.LANCZOS
    )
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=84, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f'<img class="photo" src="data:image/jpeg;base64,{b64}" alt="">'


body, in_list, prev, section, para_no = [], False, None, "", 0
hdr = {"h1": "", "title": "", "contact": ""}


def close_list():
    global in_list
    if in_list:
        body.append("</ul>")
        in_list = False


for raw in src.split("\n"):
    line = raw.rstrip()
    if not line.strip() or line.strip() == "---":
        close_list()
        continue

    if line.startswith("### "):
        close_list()
        title, dates = split_dates(line[4:])
        body.append(
            '<div class="rolehead"><h3>%s</h3><span class="dates">%s</span></div>'
            % (inline(title), html.escape(dates or ""))
        )
        prev = "h3"
    elif line.startswith("## "):
        close_list()
        section = line[3:].strip().lower()
        body.append(f"<h2>{inline(line[3:])}</h2>")
        prev = "h2"
    elif line.startswith("# "):
        close_list()
        hdr["h1"] = inline(line[2:])
        prev, para_no = "h1", 0
    elif line.startswith("- "):
        if not in_list:
            body.append("<ul>")
            in_list = True
        body.append(f"<li>{inline(line[2:])}</li>")
        prev = "li"
    else:
        close_list()
        text = line.strip()

        if prev == "h1" or (para_no < 2 and not section):
            para_no += 1
            hdr["title" if para_no == 1 else "contact"] = inline(text)
        elif prev == "h3":
            left, dates = split_dates(text)
            body.append(
                '<div class="rolehead sub"><span class="company">%s</span>'
                '<span class="dates">%s</span></div>' % (inline(left), html.escape(dates or ""))
            )
        elif section == "education":
            left, dates = split_dates(text)
            body.append(
                '<div class="rolehead edu"><span class="eduline">%s</span>'
                '<span class="dates">%s</span></div>' % (inline(left), html.escape(dates or ""))
            )
        elif re.fullmatch(r"\*\*.+\*\*", text):
            body.append(f'<p class="projname">{inline(text)}</p>')
        else:
            body.append(f'<p class="para">{inline(text)}</p>')
        prev = "p"

close_list()

header = (
    '<header class="header"><div class="headtext">'
    f'<h1>{hdr["h1"]}</h1>'
    f'<p class="title">{hdr["title"]}</p>'
    f'<p class="contact">{hdr["contact"]}</p>'
    f"</div>{photo_tag(photo_path)}</header>"
)

CSS = """
@page { size: A4; margin: 11mm 12mm 10mm 12mm; }
* { box-sizing: border-box; }
html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Roboto, "Segoe UI", Arial, Helvetica, sans-serif;
  font-size: 8.9pt; line-height: 1.34; color: #202124; margin: 0;
  background: #fff; -webkit-font-smoothing: antialiased;
}
/* Make the on-screen view match the printed page instead of running edge-to-edge. */
@media screen {
  body { width: 210mm; margin: 0 auto; padding: 11mm 12mm 10mm 12mm; }
}

.header {
  display: flex; align-items: center; gap: 14px;
  padding-bottom: 9px; border-bottom: 2px solid #1a73e8;
}
.headtext { flex: 1 1 auto; min-width: 0; }
.photo {
  width: 25mm; height: 25mm; flex: 0 0 auto;
  border-radius: 50%; object-fit: cover; border: 2px solid #1a73e8;
}
h1 { font-size: 23pt; font-weight: 500; letter-spacing: -.4px; margin: 0 0 2px 0; }
p.title {
  margin: 0 0 4px 0; font-size: 9.6pt; font-weight: 500;
  color: #1a73e8; letter-spacing: .1px;
}
p.contact { margin: 0; font-size: 8.4pt; color: #5f6368; }

h2 {
  font-size: 8.6pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1.25px; color: #1a73e8;
  margin: 13px 0 6px 0; padding-bottom: 3px;
  border-bottom: 1px solid #dadce0;
  page-break-after: avoid; break-after: avoid;
}

.rolehead {
  display: flex; justify-content: space-between; align-items: baseline;
  gap: 16px; page-break-after: avoid; break-after: avoid;
}
.rolehead h3 { font-size: 10.1pt; font-weight: 700; color: #202124; margin: 0; }
.rolehead:not(.sub):not(.edu) { margin: 9px 0 0 0; }
.rolehead.sub { margin: 0 0 4px 0; }
.rolehead.edu { margin: 0 0 5px 0; }
.company, .eduline { font-size: 8.7pt; color: #5f6368; flex: 1 1 auto; min-width: 0; }
.company strong, .eduline strong { color: #3c4043; font-weight: 600; }
.dates { font-size: 8.2pt; color: #5f6368; white-space: nowrap; flex: 0 0 auto; }

p.projname {
  margin: 8px 0 2px 0; font-size: 9.2pt; color: #3c4043;
  page-break-after: avoid; break-after: avoid;
}
p.projname strong { color: #202124; font-weight: 700; }
p.para { margin: 0 0 5px 0; color: #3c4043; }

ul { margin: 0 0 1px 0; padding-left: 14px; }
li {
  margin: 0 0 2.8px 0; color: #3c4043;
  page-break-inside: avoid; break-inside: avoid;
}
li::marker { color: #9aa0a6; }
strong { font-weight: 600; color: #202124; }
a { color: #1a73e8; text-decoration: none; }
.company a, .eduline a { color: #1a73e8; }
"""

doc = (
    "<!doctype html><html><head><meta charset='utf-8'>"
    "<title>Vaibhav Hiwase — Resume</title>"
    "<link rel='preconnect' href='https://fonts.googleapis.com'>"
    "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
    "<link href='https://fonts.googleapis.com/css2?"
    "family=Roboto:wght@300;400;500;700&display=swap' rel='stylesheet'>"
    "<style>" + CSS + "</style></head><body>\n"
    + header + "\n" + "\n".join(body) + "\n</body></html>"
)
pathlib.Path(out_path).write_text(doc, encoding="utf-8")
print("wrote", out_path, len(doc), "bytes", "| photo:", bool(photo_path))
