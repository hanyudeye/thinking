from pdf_craft import PDFPageExtractor, MarkDownWriter

extractor = PDFPageExtractor(
  device="cpu", # If you want to use CUDA, please change to device="cuda" format.
  model_dir_path=r"F:\models\pdfmodels", # The folder address where the AI ​​model is downloaded and installed
)
with MarkDownWriter(markdown_path, "images", "utf-8") as md:
  for block in extractor.extract(pdf=r"F:\1.pdf"):
    md.write(block)