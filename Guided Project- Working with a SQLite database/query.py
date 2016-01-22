import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('SELECT * FROM facts ORDER BY population ASC LIMIT 10;')
print(c.fetchall())