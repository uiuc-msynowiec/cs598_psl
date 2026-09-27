#!/usr/bin/env python3
"""Export a Jupyter notebook to HTML with code/output lines forced to wrap,
so printing the result to PDF from a browser doesn't cut off long lines.

Usage: python scripts/export_notebook_html.py path/to/notebook.ipynb. This makes an html doc.
Open in your browser and print to pdf. Code lines should wrap. There's a better way to
do this but I'm not sure it's worth the time to figure it out.

Works on macOS, Linux, and Windows (unlike the bash equivalent).
"""
import subprocess
import sys
from pathlib import Path

CSS = """<style>
/* force long code/output lines to wrap instead of being cut off when printing to PDF */
.cm-editor.cm-s-jupyter .highlight pre,
.cm-line,
.jp-OutputArea-output pre {
  white-space: pre-wrap !important;
  overflow-wrap: anywhere !important;
  word-break: break-word !important;
}
</style>
"""


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path/to/notebook.ipynb", file=sys.stderr)
        return 1

    notebook = Path(sys.argv[1])
    html_path = notebook.with_suffix(".html")

    subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert", "--to", "html", str(notebook)],
        check=True,
    )

    html = html_path.read_text(encoding="utf-8")
    if "force long code/output lines to wrap" not in html:
        html = html.replace("</head>", CSS + "</head>", 1)
        html_path.write_text(html, encoding="utf-8")

    print(f"Wrote {html_path} (open it in a browser and Print > Save as PDF)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
