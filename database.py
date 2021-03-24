import sqlite3 as sql
from sqlite3 import Error

def __create_connection(path):
    connection = None
    try:
        connection = sql.connect(path)
        print("Connection to database successful!")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection

def create_cursor(path):
    con = __create_connection(path)
    return con.cursor()

def add_plant(cur):
    name = input('Plant name: ')
    type = input('Type: ')
    cur.execute("INSERT INTO plants (name, type) VALUES (?,?)", (name, type))