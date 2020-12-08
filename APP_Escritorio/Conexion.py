import pymysql
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *

import sqlite3
import requests
import json
import datetime

I = 0

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='dbserver', #ip
            user='root',
            password='mysqlpw',
            db='cripto'
        )
        self.cursor = self.connection.cursor()

    def consulta(self):
        query = "Select * From Usuario Where Usuario = '{}' and Contraseña = '{}'".format("Michael", "1234")
        
        try:

            result = self.run_query(query)
            x = 'no entro'
            for row  in result:
                x = 'si entro'
                showinfo(title = "Login true", message = "Ingreso Correctamente")
            if x == "no entro":
                showinfo(title = "Login true", message = "El usuario no es correcto")

        except Exception as e:
            raise
        
    def run_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        self.connection.commit()
        return result

database = Database()
database.consulta()
