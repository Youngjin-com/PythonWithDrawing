import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS product")

c.execute("CREATE TABLE product(name CHAR(20), num INT)")
c.execute("INSERT INTO product VALUES('귤', 80)")
c.execute("INSERT INTO product VALUES('딸기', 60)")
c.execute("INSERT INTO product VALUES('사과', 22)")
c.execute("INSERT INTO product VALUES('복숭아', 50)")
c.execute("INSERT INTO product VALUES('밤', 75)")

conn.commit()

itr = c.execute("SELECT * FROM product")

for row in itr:
    print(row)

conn.close()
