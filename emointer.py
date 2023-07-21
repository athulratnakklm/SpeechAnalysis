import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="speech"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE speech")
#print("created")
#mycursor.execute("CREATE TABLE login(userid varchar(20), password varchar(20))")
#print("created")
#sql = "INSERT INTO login values('admin', '123')";
sql = "INSERT INTO login values('guest', '1234')";
mycursor.execute(sql)
mydb.commit()
print("record inserted.")