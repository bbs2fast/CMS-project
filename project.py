import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Contacts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
