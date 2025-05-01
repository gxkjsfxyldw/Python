import pymssql
conn = pymssql.connect(host='PC-201904150842', user='sa', password='123456', database='ss')
cur = conn.cursor()
cur.execute('CREATE TABLE persons4 (id INT NOT NULL,name VARCHAR(100),salesrep VARCHAR(100),PRIMARY KEY(id))')
conn.commit()

conn.close()