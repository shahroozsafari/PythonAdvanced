
import pyodbc

database= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=./cars_project/database_access.accdb")
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
        cursor.execute("INSERT INTO car_table VALUES(?,?,?,?,?,?)",(car_id,maker,model,year,price,color))
        database.commit()
    except(pyodbc.IntegrityError):
        print("This Car ID already exists in database !")

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
    except(pyodbc.OperationalError):
        print("Update was not successfull !")
    finally :
        print("Update successfully")

def delete_car(carid):
    cursor.execute(f"DELETE FROM car_table WHERE car_id=?",(carid,))
    database.commit()

