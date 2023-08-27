## PDF Text Extraction Tool

### Description

This tool is designed to extract text from PDF files using the pdfminer library. It provides a simple and convenient way to process multiple PDF files in a specified folder and save the extracted text into separate text files.

### Requirements

- Python 3.x
- pdfminer.six
- tqdm

### Installation

Before using the tool, make sure you have installed the required dependencies. You can install them by running the following command:

```
pip install pdfminer.six tqdm
```

### Usage

1. Place the PDF files you want to process inside the 'PDFS' folder in the current directory.

2. Run the script by executing the following command in the terminal:

```
python pdf_extraction_tool.py
```

3. The tool will perform the following steps:

   - Check if the 'TXTS' folder exists. If not, it will create it.
   - Check if the 'PDFS' folder exists. If not, it will display an error message and terminate the process.
   - Iterate through all the files in the 'PDFS' folder.
   - For each PDF file, it will perform the following operations:
     - Retrieve the filename and clean it by replacing spaces with underscores and removing unwanted characters.
     - Rename the PDF file in the 'PDFS' folder with the cleaned filename.
     - Extract text from the PDF file using pdfminer.
     - Clean the extracted text by removing unnecessary characters and multiple whitespaces.
     - Save the cleaned text to a text file with the same name (except for the extension) in the 'TXTS' folder.
     - Display a message indicating the successful processing of the file.

4. After the tool finishes processing all the PDF files, you can find the extracted text files in the 'TXTS' folder.

### Functionality

- `clean_filename(filename)`: This function cleans the input filename by replacing spaces with underscores and removing unwanted characters. It returns the cleaned filename as a string.
- `clean_extracted_text(text)`: This function cleans the extracted text by removing unnecessary characters and multiple whitespaces. It returns the cleaned text as a string.
- `extract_text_from_pdf(pdf_path, output_path)`: This function extracts text from a given PDF file using pdfminer and writes the extracted text to an output file specified by the `output_path` parameter.
- `process_pdfs()`: This function processes the PDF files in the 'PDFS' folder. It renames the files, extracts text from them, and saves the text files in the 'TXTS' folder.

### Example

Suppose you have three PDF files in the 'PDFS' folder: `document1.pdf`, `document2.pdf`, and `document3.pdf`.

After running the script, the tool will perform the following operations:

1. Create the 'TXTS' folder if it doesn't exist.
2. Rename `document1.pdf` to `document1.pdf`.
3. Extract text from `document1.pdf` and save it as `document1.txt` in the 'TXTS' folder.
4. Display a message indicating the successful processing of `document1.pdf`.
5. Repeat the above steps for `document2.pdf` and `document3.pdf`.

Finally, you will find the extracted text files `document1.txt`, `document2.txt`, and `document3.txt` in the 'TXTS' folder.

### Limitations

- The tool relies on the pdfminer library for text extraction, which may not handle certain PDF formats or complex layouts perfectly.
- The cleaning functions utilize regular expressions to remove unwanted characters and multiple whitespaces, but it may not cover all possible cases. Adjustments may be required based on specific needs.

For more details and the source code, please refer to the [GitHub repository](https://github.com/your-repo-url).

### Acknowledgements

- This tool uses the pdfminer library for text extraction.
- The tqdm library is used to display a progress bar during the PDF processing.

Feel free to contribute to this project or provide feedback for further improvements.

Please note that this tool is provided as-is without any warranties. Use it at your own risk.## PDF Text Extraction Tool

### Description

This tool is designed to extract text from PDF files using the pdfminer library. It provides a simple and convenient way to process multiple PDF files in a specified folder and save the extracted text into separate text files.

### Requirements

- Python 3.x
- pdfminer.six
- tqdm

### Installation

Before using the tool, make sure you have installed the required dependencies. You can install them by running the following command:

```
pip install pdfminer.six tqdm
```

### Usage

1. Place the PDF files you want to process inside the 'PDFS' folder in the current directory.

2. Run the script by executing the following command in the terminal:

```
python pdf_extraction_tool.py
```

3. The tool will perform the following steps:

   - Check if the 'TXTS' folder exists. If not, it will create it.
   - Check if the 'PDFS' folder exists. If not, it will display an error message and terminate the process.
   - Iterate through all the files in the 'PDFS' folder.
   - For each PDF file, it will perform the following operations:
     - Retrieve the filename and clean it by replacing spaces with underscores and removing unwanted characters.
     - Rename the PDF file in the 'PDFS' folder with the cleaned filename.
     - Extract text from the PDF file using pdfminer.
     - Clean the extracted text by removing unnecessary characters and multiple whitespaces.
     - Save the cleaned text to a text file with the same name (except for the extension) in the 'TXTS' folder.
     - Display a message indicating the successful processing of the file.

4. After the tool finishes processing all the PDF files, you can find the extracted text files in the 'TXTS' folder.

### Functionality

- `clean_filename(filename)`: This function cleans the input filename by replacing spaces with underscores and removing unwanted characters. It returns the cleaned filename as a string.
- `clean_extracted_text(text)`: This function cleans the extracted text by removing unnecessary characters and multiple whitespaces. It returns the cleaned text as a string.
- `extract_text_from_pdf(pdf_path, output_path)`: This function extracts text from a given PDF file using pdfminer and writes the extracted text to an output file specified by the `output_path` parameter.
- `process_pdfs()`: This function processes the PDF files in the 'PDFS' folder. It renames the files, extracts text from them, and saves the text files in the 'TXTS' folder.

### Example

Suppose you have three PDF files in the 'PDFS' folder: `document1.pdf`, `document2.pdf`, and `document3.pdf`.

After running the script, the tool will perform the following operations:

1. Create the 'TXTS' folder if it doesn't exist.
2. Rename `document1.pdf` to `document1.pdf`.
3. Extract text from `document1.pdf` and save it as `document1.txt` in the 'TXTS' folder.
4. Display a message indicating the successful processing of `document1.pdf`.
5. Repeat the above steps for `document2.pdf` and `document3.pdf`.

Finally, you will find the extracted text files `document1.txt`, `document2.txt`, and `document3.txt` in the 'TXTS' folder.

### Limitations

- The tool relies on the pdfminer library for text extraction, which may not handle certain PDF formats or complex layouts perfectly.
- The cleaning functions utilize regular expressions to remove unwanted characters and multiple whitespaces, but it may not cover all possible cases. Adjustments may be required based on specific needs.

For more details and the source code, please refer to the [GitHub repository](https://github.com/your-repo-url).

### Acknowledgements

- This tool uses the pdfminer library for text extraction.
- The tqdm library is used to display a progress bar during the PDF processing.

Feel free to contribute to this project or provide feedback for further improvements.

Please note that this tool is provided as-is without any warranties. Use it at your own risk.
