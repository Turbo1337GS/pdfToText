import os
import re
from tqdm import tqdm
from pdfminer.high_level import extract_text

def clean_filename(filename):
    """Cleans the filename by replacing spaces with underscores and removing unwanted characters."""
    cleaned_name = re.sub(r'[^a-zA-Z0-9_.-]', '', filename.replace(" ", "_"))
    return cleaned_name

def clean_extracted_text(text):
    """Cleans the extracted text."""
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'_____','', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_text_from_pdf(pdf_path, output_path):
    """Extracts text from a given PDF and writes the extracted text to an output file using pdfminer."""
    text = extract_text(pdf_path)
    text = clean_extracted_text(text)
    
    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write(text)

def process_pdfs():
    """Processes PDF files in the 'PDFS' folder, extracts text from them, and saves the text to 'TXTS' folder."""
    if not os.path.exists("TXTS"):
        os.makedirs("TXTS")
        print("Folder 'TXTS' has been created.")

    if not os.path.exists("PDFS"):
        print("The folder 'PDFS' does not exist in the current directory.")
        return

    files = os.listdir("PDFS")
    if not files:
        print("The 'PDFS' folder is empty.")
        return

    for filename in tqdm(files, desc="Processing PDF files", unit="file"):
        if filename.endswith(".pdf"):
            print(f"Processing {filename}...")

            new_filename = clean_filename(filename)
            new_path = os.path.join("PDFS", new_filename)
            os.rename(os.path.join("PDFS", filename), new_path)
            print(f"Filename changed to {new_filename}.")

            txt_name = new_filename.replace(".pdf", ".txt")
            txt_path = os.path.join("TXTS", txt_name)

            extract_text_from_pdf(new_path, txt_path)

            print(f"{new_filename} has been processed and saved as {txt_name}!")
        else:
            print(f"Skipping file {filename} (no .pdf extension)")

process_pdfs()
