import mysql.connector
from mysql.connector import Error
def insertar(id,name,price,purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
        query = """INSERT INTO laptop VALUES( %s, %s, %s, %s)"""
        record = (id, name, price, purchase_date)



        cursor = connection.cursor()
        result = cursor.execute(query,record)
        connection.commit()
        print(cursor.rowcount,"Record inserted succesfully into Laptop table")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error inserting into Laptop: ",e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MYSQL connnection is closed")

if (__name__ == "__main__"):
    insertar(1,"ryzen 9", 500, '2020-10-09')
    insertar(2,"ryzen 8", 300, '2018-08-21')