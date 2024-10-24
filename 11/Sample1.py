import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS product")

c.execute("CREATE TABLE product(name CHAR(20), price INT)")
c.execute("INSERT INTO product VALUES('연필', 80)")
c.execute("INSERT INTO product VALUES('지우개', 50)")
c.execute("INSERT INTO product VALUES('자', 200)")
c.execute("INSERT INTO product VALUES('콤파스', 300)")
c.execute("INSERT INTO product VALUES('볼펜', 100)")

conn.commit()

itr = c.execute("SELECT * FROM product")

for row in itr:
    print(row)

conn.close()
