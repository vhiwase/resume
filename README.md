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

## Build the resume PDF

Run these commands in PowerShell from the repository folder:

```powershell
python build-resume-pdf.py Vaibhav-Hiwase-Resume.md "$env:TEMP\resume.html" Gemini_Generated_Image_2.png
(Get-Content "$env:TEMP\resume.html" -Raw -Encoding UTF8) -replace 'font-family: Roboto, "Segoe UI"', 'font-family: "Segoe UI"' | Set-Content "$env:TEMP\resume-print.html" -Encoding UTF8
& "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --disable-remote-fonts --no-pdf-header-footer --print-to-pdf="$PWD\Vaibhav-Hiwase-Resume.pdf" "$env:TEMP\resume-print.html" | Out-Null
```

- The second command sets the font to Segoe UI. Without it, Edge downloads the Roboto font and embeds it in a format that changes line breaks and that some applicant tracking systems read poorly.
- `| Out-Null` makes PowerShell wait until Edge finishes writing the PDF.
- To build the cover letter, run the same steps with `build-letter-pdf.py` and `Vaibhav-Hiwase-Cover-Letter.md`.

## Changelog

### 2026-10-19: Aptia Group update

**Experience: Innovecture (Client: Aptia Group)**

- Rewrote the entry from a summary of the Foundry change history.
- Grouped the work into five areas: GenAI Benefits Assistant, LLM Evaluation & Quality, Document Verification Automation, Data Engineering & Pipelines, and Platform Engineering & DevOps.
- Wrote every bullet in Google's X-Y-Z format (result, metric, method) and kept each one to one or two lines.
- Kept the existing job title and dates.

**Technical Skills**

- Split the single Palantir line into three: Palantir AIP, Foundry Ontology & Apps, and Foundry Data & DevOps.
- Added OSDK, Global Branching, Code Workspaces, streaming and CDC syncs, Media Sets, Restricted Views and Markings, interfaces, function-backed actions, Slate, Contour, Foundry ML, and AI FDE.
- Added Gemini, DuckDB, and schema evolution.

**Removed**

- Removed the earlier Aptia bullets, including the roughly 95% cost reduction, the guardrail latency, and the about 37,000 verification decisions. To restore any of them, see commit `24d4ced`.
- Removed the change-proposal count from the role summary.
- Removed the duplicate Aptia entry under Projects.

**Confidentiality**

- Left out internal system and client names.
- Replaced exact internal counts with rounded figures or ratios.
- Described data-security findings in general terms only.

**PDF**

- Rebuilt `Vaibhav-Hiwase-Resume.pdf` in Segoe UI. It is still three pages.

**To review**

- Update the cover letter, which still cites figures from the earlier version: about 14 routing paths, 800+ test questions, and about 80 action types.
- Confirm that BAT means "business acceptance test", as the resume assumes.
