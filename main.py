from data_extractor import extract_data_from_pdf
from database_utils import insert_transactions, remove_duplicates
import pandas as pd
# Extract data from PDF
transactions = extract_data_from_pdf('Modified.pdf')
df = pd.DataFrame(transactions)

# Insert data into database
insert_transactions(df)

# Remove duplicates
remove_duplicates()

# SQL Operations
# ... (SQL queries go here)
