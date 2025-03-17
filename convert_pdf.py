from pdf2image import convert_from_path
import os

pdf_path = "C:/Users/user/Desktop/ImageProcessingProject/technical_diagram.pdf"
output_dir = "C:/Users/user/Desktop/ImageProcessingProject/dataset/images/"
os.makedirs(output_dir, exist_ok=True)

# Convert PDF to PNG images
pages = convert_from_path(pdf_path, dpi=300)
for i, page in enumerate(pages):
    page.save(f"{output_dir}/diagram_{i}.png", "PNG")

print("✅ PDF converted to images for processing!")
