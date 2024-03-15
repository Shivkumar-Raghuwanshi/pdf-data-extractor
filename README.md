# Watch the PDF Data Extractor video by clicking on the thumbnail below:

[![YouTube Video Thumbnail](https://img.youtube.com/vi/pkbzKx2h1u0/maxresdefault.jpg)](https://www.youtube.com/embed/pkbzKx2h1u0?si=x9hFrVCdB44NnmZx)


# PDF Data Extractor

The PDF Data Extractor is a Python project that allows you to extract table data from PDF files and insert it into a PostgreSQL database. It also provides functionality to remove duplicate entries from the database and perform various SQL operations on the data.

## Prerequisites

- Python 3.x
- PostgreSQL

## Installation

1. Clone the repository:
  git clone https://github.com/Shivkumar-Raghuwanshi/pdf-data-extractor.git
2. Navigate to the project directory: cd pdf-data-extractor
3. Install the required Python packages:
- **pdfplumber**: For extracting table data from PDF files.
- **pandas:** For data manipulation and conversion.
- **psycopg2:** For interacting with the PostgreSQL database.
  

4. Set up the PostgreSQL database:
- Create a new database named koshai.
- Update the database connection string in database_utils.py with your PostgreSQL credentials.
conn = psycopg2.connect("dbname=koshai user=your_username password=your_password")

## Usage
Place the PDF file(s) you want to extract data from in the project directory.
- Run the main.py script: python main.py
This will:
- Extract table data from the PDF file(s)
- Insert the data into the transactions table in the PostgreSQL database
- Remove any duplicate entries from the transactions table
- You can execute the SQL queries from sql_queries.sql on the transactions table to perform various operations and generate reports.

# Files
**data_extractor.py:** Contains functions to extract table data from PDF files.

**database_utils.py:** Contains functions to interact with the PostgreSQL database.

**main.py:** The main entry point of the application.

**sql_queries.sql:** Contains various SQL queries for data analysis and reporting.


