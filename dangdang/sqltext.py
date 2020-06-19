import pymysql

conn = pymysql.connect("localhost", "root", "root", "dangdang")
# a = "lakjnjoin"
# b = "1234567"
# c = "5677689"
# sql = "insert into books(title,link,comment) values('" + a + "','" + b + "','" + c + "')"
# conn.query(sql)
# conn.close()
cursor = conn.cursor()
sql = 'insert into books(title,link,comment) values("nunlonju","123435","123356");'

cursor.execute(sql)
conn.commit()

# results = cursor.fetchall()
# for row in results:
#     title = row[0]
#     link = row[1]
#     comment = row[2]
#     print(title + " " + link + " " + comment + "")
cursor.close()
conn.close()


