import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
    query = """CREATE TABLE LAPTOP(
                ID INT(11) NOT NULL,
                NAME VARCHAR(250) NOT NULL,
                PRICE FLOAT NOT NULL,
                PURCHASE_DATE DATE NOT NULL,
                primary key(ID))"""

    cursor = connection.cursor()
    result = cursor.execute(query)
    print("TABLA CREADA CON EXITO!")
except Error as e:
    print("Error conectando a MYSQL: ",e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL connnection is closed")
