import mysql.connector
from mysql.connector import Error

def update_porcentaje(porcentaje):
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
        query = "UPDATE laptop set price = price+(price*(%s/100))"
        input_data = (porcentaje,)
        cursor = connection.cursor()
        
        cursor.execute(query, input_data)
        connection.commit()

        print("RECORD UPDATED")

    except mysql.connector.Error as e:
        print("Error updating into Laptop: ",e)
    finally:
        if connection.is_connected():
            cursor.close()
            print("MYSQL connnection is closed")


def update(id, precio):
    try:
        connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
        query = "UPDATE laptop set price = %s where id = %s"
        input_data = (precio, id)
        cursor = connection.cursor()
        
        cursor.execute(query, input_data)
        connection.commit()

        print("RECORD UPDATED")

    except mysql.connector.Error as e:
        print("Error updating into Laptop: ",e)
    finally:
        if connection.is_connected():
            cursor.close()
            print("MYSQL connnection is closed")

if __name__ == "__main__":
    update(1,480)
    update_porcentaje(20)