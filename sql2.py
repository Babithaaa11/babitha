import mysql.connector

def update_people(name,password,id):
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           password = "roottoor",
           database = "tablepeople_ece"
    )

    mycursor = mydb.cursor()

    sql = "update people set name = %s,password = %s where id = %s"
    val = (name,password,id)
    mycursor.execute(sql,val)

    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")

id = input("enter the id")
name = input("enter the name")
password = input("enter the password")
update_people(name,password,id)