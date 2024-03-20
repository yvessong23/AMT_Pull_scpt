import sqlite3
import pandas as pd
import amt_parse
import matplotlib.pyplot as plt

# Defining SQLite database path
db_path = 'amt_sql_data.db'

# Connecting to the SQLite database
conn = sqlite3.connect(db_path)

# Query to select data from table (from SQL database)
query = "SELECT `DATE & TIME`, `Main coil power` FROM data_table ORDER BY `DATE & TIME`"

# Use Pandas to execute the query and load the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the SQLite connection
conn.close()



# Generating a line plot (Date & time over Main coil power)
plt.figure(figsize=(10, 6))
plt.plot(df['DATE & TIME'], df['Main coil power'], label='Main Coil Power')
plt.xlabel('DATE & HOUR')
plt.ylabel('Main Coil Power')
plt.title('Main Coil Power Per Hour')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('coil_power_over_hour.png')

# Optionally, displaying plot if running in a Jupyter notebook or similar environment
plt.show()
