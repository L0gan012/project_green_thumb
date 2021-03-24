import sqlite3 as sql
from sqlite3 import Error

class database:
    def __init__(self, path):
        self._connection = None
        self._cursor = None
        self.__create_connection(path)
        self.__create_cursor()

    def __create_connection(self, path):
        try:
            self._connection = sql.connect(path)
            print("Connection to database successful!")
        except Error as e:
            print(f"The error '{e}' occured")

    def __create_cursor(self):
        self._cursor = self._connection.cursor()

    def add_plant(self):
        name = input('Plant name: ')
        type = input('Type: ')
        self._cursor.execute("INSERT INTO plants (name, type) VALUES (?,?)", (name, type))
        self._connection.commit()

    def get_plants(self):
        self._cursor.execute("SELECT * FROM plants")
        print(self._cursor.fetchall())