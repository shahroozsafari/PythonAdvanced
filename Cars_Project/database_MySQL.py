
import pymysql

database = pymysql.connect(host="127.0.0.1",user="root",password="",db="database_MySQL")
cursor = database.cursor()


def create_car_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS car_table(car_id INTEGER PRIMARY KEY, maker TEXT, model TEXT, year INTEGER, price FLOAT, color TEXT)")
    database.commit()

def create_checkup() :
    cursor.execute("PRAGMA foreign_key=OFF")
    cursor.execute("CREATE TABLE checkup_table(car_id INTEGER,chekup_date TEXT,oil BOOLEAN,tire BOOLEAN,airfilter BOOLEAN,FOREIGN KEY (car_id) REFERENCES car_table(car_id))")
    database.commit()
    cursor.execute("PRAGMA foreign_key=ON")

def insert_car(car_id,maker,model,year,price,color):
    try:
        cursor.execute("INSERT INTO car_table VALUES(%s,%s,%s,%s,%s,%s)",(car_id,maker,model,year,price,color))
        database.commit()
    except(pymysql.err.IntegrityError):
        print("This Car ID already exists in database !")

def insert_checkup(carID,date,oil,tire,airfilter):
    cursor.execute("INSERT INTO checkup_table VALUES(%s,%s,%s,%s,%s)",[carID,date,oil,tire,airfilter])
    database.commit()

def findcar(carid):
    records = list(cursor.execute("SELECT * FROM car_table WHERE car_id=%s",[carid]))
    return records

def update_price(carid,price):
    try:
        cursor.execute("UPDATE car_table SET price=%s WHERE car_id=%s",[price,carid])
        database.commit()
    except(pymysql.err.OperationalError):
        print("Update was not successfull !")
    finally :
        print("Update successfully")

def delete_car(carid):
    cursor.execute("DELETE FROM car_table WHERE car_id =%s",(carid,))
    database.commit()
