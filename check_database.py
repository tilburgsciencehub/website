import sqlite3

# Create the database connection and cursor
conn = sqlite3.connect('tsh.db')
cursor = conn.cursor()

# Execute the query to select all records from the 'topics' table
cursor.execute('SELECT type, title, path FROM articles')

# Fetch all the results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
