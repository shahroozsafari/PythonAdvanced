
import sqlite3
from sys import path

database = sqlite3.connect(path[0]+"/database_SQLite.db",check_same_thread=False)
cursor = database.cursor()

def create_car_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS car_table(car_id INTEGER PRIMARY KEY, maker TEXT, model TEXT, year INTEGER, price FLOAT, color TEXT)")
    database.commit()
def create_checkup() :
    cursor.execute("PRAGMA foreign_key=OFF")
    cursor.execute("CREATE TABLE checkup_table(car_id INTEGER,chekup_date TEXT,oil BOOLEAN,tire BOOLEAN,airfilter BOOLEAN,FOREIGN KEY (car_id) REFERENCES car_table(car_id))")
    database.commit()
    cursor.execute("PRAGMA foreign_key=ON")

def create_userpass():
    cursor.execute("CREATE TABLE IF NOT EXISTS userpass(username TEXT PRIMARY KEY, password TEXT)")
    database.commit()

def insert_car(car_id,maker,model,year,price,color):
    cursor.execute("INSERT INTO car_table VALUES(?,?,?,?,?,?)",(car_id,maker,model,year,price,color))
    database.commit()

def insert_user(user, passwd):
    cursor.execute("INSERT INTO userpass VALUES(?,?)",(user,passwd))
    database.commit()

def insert_checkup(carID,date,oil,tire,airfilter):
    cursor.execute("INSERT INTO checkup_table VALUES(?,?,?,?,?)",[carID,date,oil,tire,airfilter])
    database.commit()

def findcar(carid):
    records = list(cursor.execute("SELECT * FROM car_table WHERE car_id=?",[carid]))
    return records

def update_price(carid,price):
    try:
        cursor.execute("UPDATE car_table SET price=? WHERE car_id=?",[price,carid])
        database.commit()
    except(sqlite3.OperationalError):
        print("Update was not successfull !")
    finally :
        print("Update successfully")

def delete_car(carid):
    cursor.execute("DELETE FROM car_table WHERE car_id =?",(carid,))
    database.commit()

def carslist():
    return list(cursor.execute("SELECT * FROM car_table"))

def check_userpass(username, password):
    check = list(cursor.execute("SELECT * FROM userpass WHERE username=? AND password=?",(username,password)))
    if len(check) == 0 :
        return False
    return True
