# pdf_merge

Merge multiple PDF files into one using Python.

## Requirements

```bash
pip install pypdf
```

## Usage

```python
import pypdf

writer = pypdf.PdfWriter()
for file_name in ["pdf1.pdf", "pdf2.pdf"]:
    writer.append(file_name)

with open("combined.pdf", "wb") as out:
    writer.write(out)
```

Just update the `file_names` list with your own PDF paths and run the script.

## Notes

- Uses [`pypdf`](https://pypdf.readthedocs.io/) — the actively maintained successor to the deprecated PyPDF2
- Output file is written safely via a context manager