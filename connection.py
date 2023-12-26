import mysql.connector

# Establish connection
connection = connection.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="your_database"
)

# Perform database operations
# ...

# Close connection
connection.close()