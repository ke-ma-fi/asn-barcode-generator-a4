# ASN Barcode Generator

This Python script generates A4 sheets of ASN barcodes in PDF format. These barcodes can be used for archiving scanned documents, such as with [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx).

## Features
- Automatically generates a series of barcodes based on user input.
- Flexible layout for defining the number of rows and columns per A4 page.
- Outputs a PDF with customizable barcodes, ideal for use in document archiving or labeling.
- Supports Code 128 barcodes.

## Prerequisites

- Python 3.x installed on your system.
- The `reportlab` library to handle PDF generation and barcode creation.

## Setup Instructions

### 1. Install Python

Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).

### 2. Install Dependencies

You need the `reportlab` package to generate PDFs and barcodes. Install it using `pip`:

```bash
pip install reportlab
```

### 3. Clone or Download the Repository

You can clone this repository using the following command or download it as a zip file:

```bash
git clone https://github.com/ke-ma-fi/asn-barcode-generator-a4
```

### 4. Run the Script

Run the Python script in your terminal or command prompt:

```bash
python barcodes.py
```

The script will prompt you for the following inputs:
- **Starting number**: The first number for the barcode sequence.
- **Ending number**: The last number for the barcode sequence.
- **Number of columns**: The number of columns on each A4 page.
- **Number of rows**: The number of rows on each A4 page.

Once you provide this information, a PDF file containing the barcodes will be generated.

## Usage

When you run the script, it generates a PDF file named `ASNLabels_<start>to<end>_<cols>x<rows>_barcodes.pdf`. The PDF will contain barcodes arranged in the number of rows and columns specified by the user.

This is useful for:
- Creating barcode sheets for document management systems like paperless-ngx.
- Labeling archived documents with unique barcode identifiers.

### Example

If you enter the following inputs:
- **Starting Number**: 1
- **Ending Number**: 100
- **Number of Columns**: 5
- **Number of Rows**: 10

The script will generate a PDF with 100 barcodes arranged 5 columns by 10 rows on each page.

## Code Overview

Here’s a brief overview of how the code works:

```python
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib import colors
```

1. **get_user_input**: Prompts the user for input and validates it.
2. **calculate_sheets**: Calculates how many sheets of labels are needed.
3. **create_labels_pdf**: Generates the PDF with barcodes based on the user's input.
4. **main**: The main function that ties everything together and runs the script.

The script formats the barcode values with leading zeros (e.g., `ASN000001`) and generates a barcode using the Code128 standard. Each label has a margin, and the barcode is scaled to fit within the label's size.

### Example Usage of Functions

- `get_user_input()`: This function collects the starting and ending numbers, as well as the layout (rows and columns).
- `create_labels_pdf()`: This function generates the PDF output based on the input, creating barcodes and positioning them correctly within each label.

### Output

The script outputs a PDF file with barcodes in a grid format (columns x rows) on A4 paper.

## Customization

You can modify the script to adjust:
- Barcode formats.
- Font size for the text below the barcode.
- Page size (currently set to A4).
- Barcode margins and sizes.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this script.

---

Happy barcoding!