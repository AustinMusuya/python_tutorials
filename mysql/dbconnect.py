# connecting to database

# 1. install and import mysql.connector
import mysql.connector

# 2.Set up connection with your database details

mydb = mysql.connector.connect(
    host='localhost', user='root', password='Chrislil1!', database='newdb')

# 3. Test the connection
print(f'Server Succesfully connected. Server Version: {
      mydb.get_server_info()}')


# 4. Create cursor object & execute sql statements

mycursor = mydb.cursor()

# show table data
mycursor.execute("SHOW TABLES")
myresult1 = mycursor.fetchall()

mycursor.execute('SELECT * FROM orders')
myresult2 = mycursor.fetchall()


# sql queries
sql_query = 'INSERT INTO orders (CustomerID, OrderDate, Total) VALUES (%s, %s, %s)'
values = (4, '2024-01-02', '8')

mycursor.execute(sql_query, values)
mydb.commit()
myresult3 = mycursor.fetchall()


mycursor.execute('SELECT * FROM orders')
myresult4 = mycursor.fetchall()

for row in myresult1, myresult2, myresult3, myresult4:
    print(row)


# Close the connection
mycursor.close()
mydb.close()
