# Vaibhav Hiwase — Resume

This repository holds the source files and build scripts for Vaibhav Hiwase's resume and cover letter.

## Files

| File | Description |
| --- | --- |
| `Vaibhav-Hiwase-Resume.md` | Resume source. Edit this file. |
| `Vaibhav-Hiwase-Resume.pdf` | Resume PDF, built from the source. |
| `build-resume-pdf.py` | Converts the resume source to HTML for printing. |
| `Vaibhav-Hiwase-Cover-Letter.md`, `Vaibhav-Hiwase-Cover-Letter.pdf` | Cover letter source and PDF. |
| `build-letter-pdf.py` | Converts the cover letter source to HTML for printing. |
| `Gemini_Generated_Image_2.png` | Photo for the resume header. |

The other files are earlier resume versions and supporting assets.

## Build the PDFs

Run these commands in PowerShell from the repository folder.

To build the resume:

```powershell
python build-resume-pdf.py Vaibhav-Hiwase-Resume.md "$env:TEMP\resume.html" Gemini_Generated_Image_2.png
(Get-Content "$env:TEMP\resume.html" -Raw -Encoding UTF8) -replace 'font-family: Roboto, "Segoe UI"', 'font-family: "Segoe UI"' | Set-Content "$env:TEMP\resume-print.html" -Encoding UTF8
& "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --disable-remote-fonts --no-pdf-header-footer --print-to-pdf="$PWD\Vaibhav-Hiwase-Resume.pdf" "$env:TEMP\resume-print.html" | Out-Null
```

To build the cover letter, which has no photo:

```powershell
python build-letter-pdf.py Vaibhav-Hiwase-Cover-Letter.md "$env:TEMP\letter.html"
(Get-Content "$env:TEMP\letter.html" -Raw -Encoding UTF8) -replace 'font-family: Roboto, "Segoe UI"', 'font-family: "Segoe UI"' | Set-Content "$env:TEMP\letter-print.html" -Encoding UTF8
& "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --disable-remote-fonts --no-pdf-header-footer --print-to-pdf="$PWD\Vaibhav-Hiwase-Cover-Letter.pdf" "$env:TEMP\letter-print.html" | Out-Null
```

- The second command in each block sets the font to Segoe UI. Without it, Edge downloads the Roboto font and embeds it in a format that changes line breaks and that some applicant tracking systems read poorly.
- `| Out-Null` makes PowerShell wait until Edge finishes writing the PDF.

## Changelog

### 2026-10-19: Aptia Group update

**Experience: Innovecture (Client: Aptia Group)**

- Rewrote the entry from a summary of the Foundry change history.
- Grouped the work into five areas: GenAI Benefits Assistant, AI Evaluation & Testing, Document Verification Automation, Data Engineering & Pipelines, and Platform Engineering & DevOps.
- Wrote every bullet in plain language that any reader can follow, in Google's X-Y-Z format (result, metric, method). Technical terms get a short explanation, such as "made-up answers (hallucinations)".
- Kept every bullet to one or two lines.
- Kept the existing job title and dates.

**Technical Skills**

- Split the single Palantir line into three: Palantir AIP, Foundry Ontology & Apps, and Foundry Data & DevOps.
- Added OSDK, Global Branching, Code Workspaces, streaming and CDC syncs, Media Sets, Restricted Views and Markings, interfaces, function-backed actions, Slate, Contour, Foundry ML, and AI FDE.
- Added Gemini, DuckDB, and schema evolution.

**Cover letter**

- Rewrote the body to match the updated resume, in the same plain language.
- Replaced the earlier figures (about 14 routing paths, 800+ test questions, about 80 action types, and the roughly 95% cost reduction) with results from the resume.
- Updated the date to 19 October 2026.

**Removed**

- Removed the earlier Aptia bullets, including the roughly 95% cost reduction, the guardrail latency, and the about 37,000 verification decisions. To restore any of them, see commit `24d4ced`.
- Removed the change-proposal count from the role summary.
- Removed the duplicate Aptia entry under Projects.

**Confidentiality**

- Left out internal system and client names.
- Replaced exact internal counts with rounded figures or ratios.
- Described data-security findings in general terms only.

**PDFs**

- Rebuilt both PDFs in Segoe UI. The resume is still three pages, and the cover letter is still one page.

**Repository**

- Removed `RESUME.png`, an October 2020 resume image whose name clashed with `Resume.png` on Windows. It is still in the Git history.
