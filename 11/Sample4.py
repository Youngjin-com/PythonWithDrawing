import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

itr = c.execute("SELECT * FROM product WHERE name LIKE '%우%'")

for row in itr:
    print(row)

conn.close()
