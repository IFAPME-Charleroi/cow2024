import csv

# Define your CSV and SQL file paths
csv_file_path = 'dataset_charleroi.csv'
sql_file_path = 'dataset_charleroi.sql'

# Open the CSV file and the SQL file for writing
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file, \
        open(sql_file_path, mode='w', encoding='utf-8') as sql_file:
    # Create a CSV reader specifying the semicolon delimiter
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    # Check if 'timestamp' column exists to prevent KeyError
    if 'timestamp' not in csv_reader.fieldnames:
        raise ValueError("The column 'timestamp' was not found in the CSV file.")

    # Iterate through each row in the CSV
    for row in csv_reader:
        # Construct the SQL INSERT statement with proper escaping for string values
        insert_statement = f"INSERT INTO proximus (timestamp, zone, total, wkt) VALUES ('{row['timestamp']}', '{row['zone']}', {row['total']}, '{row['wkt']}');\n"

        # Write the INSERT statement to the SQL file
        sql_file.write(insert_statement)

print("SQL file has been created with INSERT statements.")