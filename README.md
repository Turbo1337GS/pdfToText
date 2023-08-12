# pdfToText
 The script converts PDFs in the 'PDFS' folder to text files in 'TXTS', making them suitable for training natural language processing models.
# Documentation

This documentation provides an overview of the program and explains its functionality.

## Program Description
The program is designed to process PDF files, extract text from them, and save the extracted text as separate text files. It consists of several functions to carry out different tasks.

### Functions
1. `clean_filename(filename)`
   - Description: Cleans the filename by replacing spaces with underscores and removing unwanted characters.
   - Parameters: `filename` (str) - the name of the file to be cleaned.
   - Return Value: `cleaned_name` (str) - the cleaned filename.

2. `extract_text_from_pdf(pdf_path, output_path)`
   - Description: Extracts text from a given PDF and writes the extracted text to an output file.
   - Parameters:
     - `pdf_path` (str) - the path to the input PDF file.
     - `output_path` (str) - the path to the output file where the extracted text will be saved.
   - Return Value: None

3. `process_pdfs()`
   - Description: Processes PDF files in the `PDFS` folder, extracts text from them, and saves the text to the `TXTS` folder.
   - Parameters: None
   - Return Value: None

### Usage
To use the program, follow these steps:

1. Place the PDF files you want to process in the `PDFS` folder.
   - If the `TXTS` folder does not exist, the program will create it automatically.

2. Run the program by executing the `process_pdfs()` function.

3. The program will process each PDF file one by one, extract the text, and save it as a separate text file in the `TXTS` folder.
   - The program skips any files in the `PDFS` folder that do not have a `.pdf` extension.

4. Monitor the console output for progress and information on each file being processed.

5. Once the program finishes, check the `TXTS` folder for the extracted text files.

Note: Make sure you have the necessary dependencies installed (extract_text, tqdm).

## Example Usage

```python
import os
import re
from tqdm import tqdm
from pdfminer.high_level import extract_text

# Functions and program code here...

process_pdfs()
```

## License
This program is released under the [MIT License](LICENSE).
