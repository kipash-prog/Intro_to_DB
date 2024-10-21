import mysql.connector

    # Establish the connection
conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="@147896AB"
    )

mycursor = conn.cursor()
try:
    if mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store"):
        print(f"Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
  print(f"Error: {e}")

conn.close()
mycursor.close()
        

    
