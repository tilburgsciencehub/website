import sqlite3
import os
import re
import shutil
import logging

# Create the database and table
conn = sqlite3.connect('tsh.db')
cursor = conn.cursor()

# SELECT statement to find all articles with "Style Guide" in the title
cursor.execute('''
    SELECT title, parent, path FROM articles WHERE title LIKE '%Style and Writing%'
''')

# Fetch all matching records
articles = cursor.fetchall()

# Print the results
for article in articles:
    print(article)

# Close the connection
conn.close()