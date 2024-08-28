import sqlite3

# Connect to the database
conn = sqlite3.connect('test_db.sqlite')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

# Commit the transaction
conn.commit()

# Query the database
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Update a record
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))
conn.commit()

# Delete a record
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Alice',))
conn.commit()

# Close the connection
conn.close()
