import mysql.connector
from mysql.connector import Error
def select(precio_l, precio_h):
#un def y pasarles dos valores que sean los precios y que devuelva todos los portatiles que esten en ese rango de precio
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
        query = "SELECT * FROM laptop where price between %s and %s"
        


        tid = (precio_l, precio_h)
        cursor = connection.cursor()
        cursor.execute(query,tid)

        for r in cursor.fetchall():
            print(r[0],r[1],r[2],r[3])

    except Error as e:
        print("Error selecting into Laptop: ",e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MYSQL connnection is closed")

if (__name__ == "__main__"):
    select(100,500)