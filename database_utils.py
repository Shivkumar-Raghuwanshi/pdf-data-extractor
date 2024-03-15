import psycopg2


# Connect to PostgreSQL database
conn = psycopg2.connect("dbname=koshai user=postgres password=Shiv56@#@")
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        app_id INT,
        xref INT,
        settlement_date DATE,
        broker TEXT,
        sub_broker TEXT,
        borrower_name TEXT,
        description TEXT,
        total_loan_amount FLOAT,
        commission_rate FLOAT,
        upfront FLOAT,
        upfront_incl_gst FLOAT
    )
""")

# Insert data into table
def insert_transactions(df):
    for _, row in df.iterrows():
        transaction_data = tuple(row)  # Convert Series to tuple

        app_id, xref, settlement_date, broker, sub_broker, borrower_name, description, total_loan_amount, commission_rate, upfront, upfront_incl_gst = transaction_data

        # Convert string values to float for columns with FLOAT data type
        total_loan_amount = float(total_loan_amount.replace(',', ''))
        commission_rate = float(commission_rate.replace(',', '').replace(' ', ''))
        upfront = float(upfront.replace(',', ''))
        upfront_incl_gst = float(upfront_incl_gst.replace(',', ''))

        transaction_data = (app_id, xref, settlement_date, broker, sub_broker, borrower_name, description, total_loan_amount, commission_rate, upfront, upfront_incl_gst)

        cur.execute("""
            INSERT INTO transactions (app_id, xref, settlement_date, broker, sub_broker, borrower_name, description, total_loan_amount, commission_rate, upfront, upfront_incl_gst)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, transaction_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    
# Remove duplicates
def remove_duplicates():
    cur.execute("""
        DELETE FROM transactions
        WHERE ctid NOT IN (
            SELECT max(ctid)
            FROM transactions
            GROUP BY xref, total_loan_amount
        )
    """)

    # Commit changes and close connection
    conn.commit()
    conn.close()