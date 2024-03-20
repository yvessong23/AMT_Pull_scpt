import pandas as pd
from datetime import datetime
import sqlite3

# Define the path to your CSV file
file_path = '34146-01.CSV'
db_path = 'amt_sql_data.db'  # Define the SQLite database path
table_name = 'data_table'  # Define a table name for SQLite

skip_rows = 9  # Skipping first 9 rows of file (for parsing reasons)
use_cols = [":DEV_COMMENT", "Main coil power"]  # Columns to use

# Connecting to SQLite database
conn = sqlite3.connect(db_path)

# Read the data from CSV, skipping initial rows
df = pd.read_csv(file_path, skiprows=skip_rows, encoding='ISO-8859-1', usecols=use_cols, low_memory=False)

# Rename column for clarity
df = df.rename(columns={':DEV_COMMENT': 'DATE & TIME'})


# Converting csv file to pandas dataframe for SQL database readibilty
df['DATE & TIME'] = pd.to_datetime(df['DATE & TIME'], errors='coerce', format=None)
df['HOUR'] = df['DATE & TIME'].dt.hour

# Convert 'Main coil power' to numeric, coercing errors
df['Main coil power'] = pd.to_numeric(df['Main coil power'], errors='coerce')

# Drop rows where 'DATE & TIME' conversion failed (if any)
df.dropna(subset=['DATE & TIME'], inplace=True)
df.dropna(subset=['HOUR'], inplace=True)

# Ensure the DataFrame is sorted by 'DATE & TIME'
df.sort_values('DATE & TIME', inplace=True)

# Reset index after processing
df.reset_index(drop=True, inplace=True)

# Optionally, calculate the mean of 'Main coil power' and print it
row_avg = df['Main coil power'].mean()
print(f"Average Main coil power: {row_avg}")

# Upload the DataFrame to SQLite, specifying the table name
df.to_sql(table_name, conn, if_exists='replace', index=True, index_label='id')

# Close the SQLite connection
conn.close()
