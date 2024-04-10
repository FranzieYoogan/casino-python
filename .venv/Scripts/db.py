import MySQLdb

mydb = MySQLdb.connect(
  host="127.0.0.1",
  user="root",
  password="",
  db="casino-python"
)

cursor = mydb.cursor()

get = cursor.execute("select * from casinousers")

for row in cursor.fetchall():
 print(row)
