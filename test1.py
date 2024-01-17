# import mysql.conneector
import mysql.connector

# pass the first three variables host, user and password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="pilotdb"
)
# print to see whether the connection works
print(mydb)

# initialize cursor which oonnects with the entire mysql server
mycursor = mydb.cursor()

# create database
mycursor.execute("CREATE DATABASE pilotdb")

# show all available databases
mycursor.execute("SHOW DATABASES")

# print all databases in mycursor
for db in mycursor:
     print(db)

# create a table in my database
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# show tables
mycursor.execute("SHOW TABLES")

# print all tables in mycursor
for tb in mycursor:
    print(tb)


# populating table with values
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

# create a tuple
student1 = ("Rachel", 22)

# execute the sql formula
mycursor.execute(sqlFormula, student1)

# commit the changes
mydb.commit()

# Create a students array
students = [("Bob", 12),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 28),
            ("Michelle", 17)]

# Execute the sql formula for multiple rows
mycursor.executemany(sqlFormula, students)

# Commit the changes
mydb.commit()

# selecting all students
mycursor.execute("SELECT * FROM students")

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print all students in myresults
for row in myresult:
    print(row)

#  selecting age from students
mycursor.execute("SELECT age FROM students")

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print age of  students in myresluts
for row in myresult:
    print(row)

# selecting age from students
mycursor.execute("SELECT age FROM students")

# fetchone function displays one output
myresult = mycursor.fetchone()

# print age of  students in myresluts
for row in myresult:
      print(row)

# using where command to specify age
sql = "SELECT * FROM students WHERE age = 17"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
      print(result)

# using where command to specify name
sql = "SELECT * FROM students WHERE name = 'Michelle'"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
    print(result)

# using wildcard character % where name starts with Mi
sql = "SELECT * FROM students WHERE name LIKE 'Mi%'"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
      print(result)

# using wildcard character % where name has ac in the middle
sql = "SELECT * FROM students WHERE name LIKE '%ac%'"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
     print(result)

# using wildcard character %s
sql = "SELECT * FROM students WHERE name = %s"

# execute the sql
mycursor.execute(sql, ("Bob", ))

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
      print(result)

# updating age
sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

# execute the sql
mycursor.execute(sql)

# Commit the changes
mydb.commit()

# limiting values to 5
mycursor.execute("SELECT * FROM students LIMIT 5")

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
     print(result)

# offseting the values by 2 where the values that are displayed will not include the first 2
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for result in myresult:
     print(result)

# order the results by ascending order
sql = "SELECT * FROM students ORDER BY name"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for r in myresult:
     print(r)

# order the results by ascending order
sql = "SELECT * FROM students ORDER BY age"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for r in myresult:
     print(r)

# ordering by descending order
sql= "SELECT * FROM students ORDER BY name DESC"

# execute the sql
mycursor.execute(sql)

# display the results using fetchall function it displays the last executed statement
myresult = mycursor.fetchall()

# print the results
for r in myresult:
     print(r)

# deleting a record from the table
sql= "DELETE FROM students WHERE name = 'Jacob'"

# execute the sql
mycursor.execute(sql)

# Commit the changes
mydb.commit()

# deleting a record from the table
sql= "DELETE FROM students WHERE age = 13"

# execute the sql
mycursor.execute(sql)

# Commit the changes
mydb.commit()

# deleting the table using drop command
sql= "DROP TABLE students"

# execute the sql
mycursor.execute(sql)

# Commit the changes
mydb.commit()

# dropping table using if exists command
sql= "DROP TABLE IF EXISTS students"

# execute the sql
mycursor.execute(sql)

# Commit the changes
mydb.commit()
