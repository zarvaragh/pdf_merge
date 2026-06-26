import pypdf

writer = pypdf.PdfWriter()
file_names = ["pdf1.pdf", "pdf2.pdf"]
for file_name in file_names:
    writer.append(file_name)

with open("combined.pdf", "wb") as out:
    writer.write(out)