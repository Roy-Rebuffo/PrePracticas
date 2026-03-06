import mysql.connector
from mysql.connector import Error
def insertar(nombre,fecha):
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Cumpleaños',user='root',password='root')
        query = """INSERT INTO CUMPLEAÑOS VALUES(%s, %s)"""
        record = (nombre,fecha)

        cursor = connection.cursor()
        result = cursor.execute(query,record)
        connection.commit()
        print(cursor.rowcount,"Record inserted succesfully into cumpleaños table")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error inserting into cumpleaños: ",e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MYSQL connnection is closed")

if (__name__ == "__main__"):
    insertar("Mar", '2001-01-27')
    insertar("Roy", '1998-06-19')
    insertar("Fabian", '2005-04-22')
    insertar("Rafa", '2003-05-15')

