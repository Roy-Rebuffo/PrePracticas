#CREAR UNA BBDD QUE SE LLAME CUMPLEAÑOS
#DENTRO DE ELLA CREAR UNA TABLA CUMPLEAÑOS: NOMBRE, FECHA(DATE)

#INSERTAR DENTRO DE LOS CUMPLEAÑOS -> CADA UNO LA FECHA DE LOS 5 AÑOS SIGUIENTES A LOS DEL SISTEMA(aumentar 5 años a cada uno)

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',port=3307,database='sys',user='root',password='root')
    query = "CREATE DATABASE Cumpleaños"
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