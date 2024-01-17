# Python and MySQL: Database  Manipulation

This Python script demonstrates basic database manipulation operations using the 'mysql.connector' module to interact with a MySQL database. The script covers essential tasks such as creating a database, creating tables, inserting data, querying data, updating records, and deleting records.

# Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system.
- mysql-connector-python library installed. If not installed, you can install it using:

      pip install mysql-connector-python

- A MySQL server running locally or on a remote server.
- MySQL credentials (host, user, password) and a database name (in this script, the database name is "pilotdb").

# Usage

1. Open the script in a Python environment.
2. Update the MySQL connection details (host, user, password, database) in the script.
   
       host="localhost"
       user="root"
       passwd="bronzebunny"
       database="pilotdb"

# Script Overview

1. Connecting to MySQL Database:
 Establishes a connection to the MySQL server using the provided credentials.

2. reating a Database:
 Creates a new database named "pilotdb."

3. Creating a Table:
 Defines a table named "students" with columns for name and age.

4.Inserting Data:
 Populates the "students" table with sample data.

5. Querying Data:
 Executes various SELECT queries to retrieve and display data.

6. Updating Records:
 Demonstrates updating records in the "students" table.

7. Deleting Records:
 Illustrates deleting records from the "students" table.

8. Dropping Table and Database:
 Drops the "students" table and the "pilotdb" database.
