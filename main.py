import mysql.connector
from realtime_face_recognition import func
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="kriti"
)

mycursor = mydb.cursor()

v = func()

sql = "UPDATE student SET attend = %s WHERE name =%s "


t= ('Present',v)


mycursor.execute(sql,t)
'''
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  '''

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
