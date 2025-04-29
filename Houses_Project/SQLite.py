import sqlite3
from sys import path

connection = sqlite3.connect(path[0]+"/house_db.db")
cursor = connection.cursor()

