# AMT_Pull_scpt
Python script to read in puller data. (AMT)
In this project, I developed a Python script to automate the processing of large datasets stored in CSV format. The script begins by defining paths to the CSV file and SQLite database, along with specific configurations such as the table name and columns of interest. Utilizing pandas, it reads the data, skipping initial rows for proper parsing, and selects specified columns. It includes data cleaning steps, such as renaming columns for clarity, converting date and time information to datetime objects, handling missing values, and converting numeric data with error coercion. The processed data is then sorted, indexed, and uploaded to an SQLite database for persistent storage. The script is designed with flexibility to adjust to various datetime formats and includes a calculation of the average value of a specified column, showcasing my ability to manage and analyze data efficiently.

Building on the initial data processing and storage, the second phase of the project involves querying the SQLite database to retrieve relevant data for analysis. This phase utilizes pandas for efficient data handling and matplotlib for data visualization. After connecting to the database, a SQL query is executed to select specific columns, with a focus on 'DATE & TIME' and 'Main coil power'. The script ensures the 'DATE & TIME' column is properly parsed into datetime objects, extracting hours for detailed temporal analysis.

The key feature of this phase is the generation of a line plot, illustrating the variation of 'Main coil power' across different days/hours, providing valuable insights into power usage patterns. The visualization process includes configuring the plot's appearance for clarity and comprehensiveness, such as labeling axes, adding titles, and adjusting tick marks for better readability. The resulting plot is saved as an image file, offering a tangible output that can be easily shared or included in reports.
