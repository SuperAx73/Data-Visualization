import sqlite3

# Create a database and table
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, product TEXT, amount REAL)''')

# Insert data
data = [('Laptop', 1200.99), ('Mouse', 25.5), ('Keyboard', 75.0)]
cursor.executemany("INSERT INTO sales (product, amount) VALUES (?, ?)", data)
conn.commit()

# Query the database
cursor.execute("SELECT * FROM sales")
for row in cursor.fetchall():
    print(row)

conn.close()