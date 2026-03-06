import mysql.connector
from mysql.connector import Error
def insertarTuplas(record):
    #Record lista de tuplas
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
        query = """INSERT INTO laptop VALUES( %s, %s, %s, %s)"""


        cursor = connection.cursor()
        result = cursor.executemany(query,record)
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
    insertarTuplas(record = [(5, 'HP Pavilion Power', 1999, '2019-01-11'),
                    (6, 'MSI WS75', 5799, '2019-02-27')])