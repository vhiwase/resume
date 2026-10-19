"""Render Vaibhav-Hiwase-Cover-Letter.md to a styled HTML letter.

Shares the resume's letterhead and palette so the two read as a set.

Usage:  python build-letter-pdf.py <input.md> <output.html> [photo.png]
Then:   msedge --headless --disable-gpu --no-pdf-header-footer
                --print-to-pdf="out.pdf" "file:///<abs-path>/out.html"
"""
import re, io, html, sys, base64, pathlib

md_path, out_path = sys.argv[1], sys.argv[2]
photo_path = sys.argv[3] if len(sys.argv) > 3 else None
src = pathlib.Path(md_path).read_text(encoding="utf-8")

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return LINK_RE.sub(r'<a href="\2">\1</a>', s)


def photo_tag(path):
    if not path or not pathlib.Path(path).exists():
        return ""
    try:
        from PIL import Image
    except ImportError:
        return ""
    img = Image.open(path).convert("RGB")
    side = min(img.size)
    left, top = (img.width - side) // 2, (img.height - side) // 2
    img = img.crop((left, top, left + side, top + side)).resize((340, 340), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=84, optimize=True)
    return ('<img class="photo" src="data:image/jpeg;base64,%s" alt="">'
            % base64.b64encode(buf.getvalue()).decode())


hdr = {"h1": "", "title": "", "contact": ""}
body, recipient = [], []
para_no, in_header, signed = 0, True, False

for raw in src.split("\n"):
    line = raw.rstrip()

    if not line.strip():
        continue
    if line.strip() == "---":
        in_header = False
        continue

    if line.startswith("# "):
        hdr["h1"] = inline(line[2:])
        continue

    if line.startswith("> "):
        recipient.append(inline(line[2:]))
        continue

    text = line.strip()

    if in_header:
        para_no += 1
        hdr["title" if para_no == 1 else "contact"] = inline(text)
        continue

    # Flush any collected recipient block before the next element.
    if recipient:
        body.append('<p class="recipient">%s</p>' % "<br>".join(recipient))
        recipient = []

    if not body and not signed:
        body.append(f'<p class="letterdate">{inline(text)}</p>')
    elif text.lower().startswith("dear"):
        body.append(f'<p class="salutation">{inline(text)}</p>')
    elif re.match(r"^(sincerely|regards|best regards|yours)", text, re.I):
        body.append(f'<p class="signoff">{inline(text)}</p>')
        signed = True
    elif signed:
        body.append(f'<p class="signature">{inline(text)}</p>')
    else:
        body.append(f'<p class="btext">{inline(text)}</p>')

if recipient:
    body.append('<p class="recipient">%s</p>' % "<br>".join(recipient))

header = (
    '<header class="header"><div class="headtext">'
    f'<h1>{hdr["h1"]}</h1>'
    f'<p class="title">{hdr["title"]}</p>'
    f'<p class="contact">{hdr["contact"]}</p>'
    f"</div>{photo_tag(photo_path)}</header>"
)

CSS = """
@page { size: A4; margin: 16mm 18mm; }
* { box-sizing: border-box; }
html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Roboto, "Segoe UI", Arial, Helvetica, sans-serif;
  font-size: 10pt; line-height: 1.52; color: #202124; margin: 0; background: #fff;
  -webkit-font-smoothing: antialiased;
}
@media screen { body { width: 210mm; margin: 0 auto; padding: 16mm 18mm; } }

.header {
  display: flex; align-items: center; gap: 14px;
  padding-bottom: 10px; border-bottom: 2px solid #1a73e8; margin-bottom: 22px;
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
p.contact { margin: 0; font-size: 8.6pt; color: #5f6368; }

p.letterdate { margin: 0 0 18px 0; font-size: 9.4pt; color: #5f6368; }
p.recipient { margin: 0 0 22px 0; font-size: 9.6pt; color: #3c4043; line-height: 1.45; }
p.salutation { margin: 0 0 14px 0; }
p.btext { margin: 0 0 13px 0; color: #3c4043; }
p.signoff { margin: 20px 0 0 0; color: #3c4043; }
p.signature {
  margin: 4px 0 0 0; font-weight: 600; font-size: 11pt; color: #202124;
}
strong { font-weight: 600; color: #202124; }
a { color: #1a73e8; text-decoration: none; }
"""

doc = (
    "<!doctype html><html><head><meta charset='utf-8'>"
    "<title>Vaibhav Hiwase — Cover Letter</title>"
    "<link rel='preconnect' href='https://fonts.googleapis.com'>"
    "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
    "<link href='https://fonts.googleapis.com/css2?"
    "family=Roboto:wght@300;400;500;700&display=swap' rel='stylesheet'>"
    "<style>" + CSS + "</style></head><body>\n"
    + header + "\n" + "\n".join(body) + "\n</body></html>"
)
pathlib.Path(out_path).write_text(doc, encoding="utf-8")
print("wrote", out_path, len(doc), "bytes | photo:", bool(photo_path))
