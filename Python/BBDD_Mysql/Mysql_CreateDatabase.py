import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',port=3307,database='sys',user='root',password='root')
    query = "CREATE DATABASE Electronics"
    cursor = connection.cursor()
    result = cursor.execute(query)
    print("BBDD CREADA CON EXITO!")
except Error as e:
    print("Error conectando a MYSQL: ",e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL connnection is closed")