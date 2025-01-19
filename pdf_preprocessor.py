import os
from PyPDF2 import PdfReader


def extract(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            txt_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            try:
                reader = PdfReader(pdf_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)
                print(f"متن از {filename} با موفقیت استخراج شد.")

            except Exception as e:
                print(f"خطا در استخراج متن از {filename}: {e}")


input_folder = "books"
output_folder = "data"
extract(input_folder, output_folder)
