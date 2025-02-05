import os
from pdf2image import convert_from_path
from tqdm import tqdm

# sciezka do gazetki
pdf_path = "gazetka.pdf"
x1, y1, x2, y2 = 165, 369, 1177, 1350

output_folder = "output_folder"
os.makedirs(output_folder, exist_ok=True)

print("Loading pages, this may take a while...")

pages = convert_from_path(pdf_path, poppler_path=r'C:\poppler\library\bin')

for page_number, page_image in enumerate(tqdm(pages, desc="Processing pages")):
    cropped_img = page_image.crop((x1, y1, x2, y2))
    output_image_path = os.path.join(output_folder, f"product_{page_number + 1}.png")
    cropped_img.save(output_image_path)
