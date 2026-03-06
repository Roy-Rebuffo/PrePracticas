import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',port=3307,database='Electronics',user='root',password='root')
    query = "SELECT * FROM laptop"
    cursor = connection.cursor(dictionary=True)
    result = cursor.execute(query)
    record = cursor.fetchall()

    print("Fetching eacj row using columns name")
    for row in record:
        id = row["ID"]
        name = row["NAME"]
        price = row["PRICE"]
        purchase_date = row["PURCHASE_DATE"]
        print(id,name,price,purchase_date)

except Error as e:
    print("Error inserting into Laptop: ",e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MYSQL connnection is closed")
