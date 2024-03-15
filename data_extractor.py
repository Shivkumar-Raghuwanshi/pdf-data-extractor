import pdfplumber
import pandas as pd

def extract_data_from_pdf(pdf_file):
    """
    Extract table data from a PDF file, skipping the first row of the first page.

    Args:
        pdf_file (str): Path to the PDF file.

    Returns:
        list: List of table rows extracted from the PDF, excluding the first row of the first page.
    """
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Initialize an empty list to store table data
        table_data = []

        # Flag to keep track of whether the first page has been processed
        first_page_processed = False

        # Iterate through each page in the PDF
        for page in pdf.pages:
            # Extract table data from the current page
            page_tables = page.extract_tables()

            # Assuming there's only one table per page
            if page_tables:
                # Skip the first row of the first page
                if not first_page_processed:
                    table_rows = page_tables[0][1:]
                    first_page_processed = True
                else:
                    table_rows = page_tables[0]

                table_data.extend(table_rows)

    return table_data

transactions = extract_data_from_pdf('Modified.pdf')
df = pd.DataFrame(transactions)

print(df)
