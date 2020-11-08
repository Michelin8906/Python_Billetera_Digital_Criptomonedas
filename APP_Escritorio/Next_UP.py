
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *

import sqlite3
import requests
import json
import datetime

#Comentario Vs1
class Product:
    db_name = 'Next_U.db'
    _ENDPOINT = "https://api.binance.com"

    def __init__(self, window):

        self.wind = window
        self.wind.geometry ("240x140+100+100")
        self.wind.title('BILLETERA VIRTUAL')

        #Creating a Frame Container
        self.frame = LabelFrame(self.wind, text = 'Iniciar Sesion')
        self.frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #name imput
        Label(self.frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(self.frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Password imput
        Label(self.frame, text = 'Password: ').grid(row = 2, column = 0)
        self.passw = Entry(self.frame, show = "*")
        self.passw.grid(row = 2, column = 1)

        #botton add Sesion
        ttk.Button(self.frame, text = 'Iniciar Sesion', command = self.Iniciar_sesion).grid(row = 3, columnspan = 2, sticky = W + E)
        
    def validation(self):
        return len(self.name.get()) != 0 and len(self.passw.get()) != 0    

    def Iniciar_sesion(self):
        if self.validation():
            query = "Select * From Usuario Where Usuario = ? and Contraseña = ?"
            parameters = (self.name.get(), self.passw.get())
            result = self.run_query(query, parameters)
            I = 0
            for row  in result:
                I = 1
                showinfo(title = "Login true", message = "Ingreso Correctamente")
                self.usu = self.name.get()
                self.frame.destroy()
                self.wind.geometry ("1020x650+50+20")

                #self.usua = Entry(self.wind)
                self.usu_act = Entry(self.wind, textvariable = StringVar(self.wind, value = "Usuario: "+self.usu), state = 'readonly')
                self.usu_act.grid(row = 0, column = 0)
                
                #self.usua.grid(row=0, column = 0)
                
                #botton send Cripto
                ttk.Button(self.wind, text = 'Salir', command = self.Close_App).grid(row = 0,column =6)
                
                #*********************************************************************************************************

                #Creating a Frame Container Send
                self.frame2 = LabelFrame(self.wind, text = 'Enviar Criptomonedas')
                self.frame2.grid(row = 1, column = 1)
                
                #Criptomoneda imput
                Label(self.frame2, text = 'Criptomoneda: ').grid(row = 2, column = 1)
                self.Cripto = ttk.Combobox(self.frame2, state = 'readonly')
                self.Cripto.focus()
                self.Cripto.grid(row = 2, column = 2)
                query = "Select Code FROM Code_Cripto"
                result = self.run_query(query)
                cache2 = list()
                for row  in result:
                    cache2.append(row)
                self.Cripto["values"] = cache2

                #Cantidad imput
                Label(self.frame2, text = 'Cantidad: ').grid(row = 3, column = 1)
                self.Cantidad = Entry(self.frame2)
                self.Cantidad.grid(row = 3, column = 2)

                #Seleccione Usuario
                Label(self.frame2, text = 'Usuario: ').grid(row = 4, column = 1)
                self.Usuario = ttk.Combobox(self.frame2, state = 'readonly')
                self.Usuario.grid(row = 4, column = 2)
                query = "Select Usuario FROM Usuario Where Usuario <> ? ORDER BY Usuario ASC"
                result = self.run_query(query, (self.usu, ))
                cache = list()
                for row  in result:
                    cache.append(row)
                self.Usuario["values"] = cache

                #botton send Cripto
                ttk.Button(self.frame2, text = 'Enviar Cripto', command = self.Enviar_Cripto).grid(row = 5,column =1, columnspan = 2, sticky = W + E)

                #*********************************************************************************************************
                #Creating a Frame Container
                self.frame3 = LabelFrame(self.wind, text = 'Historial De Criptomonedas')
                self.frame3.grid(row = 1, column = 4)
                
                #Criptomoneda imput
                Label(self.frame3, text = 'Criptomoneda: ').grid(row = 2, column = 4)
                self.Cripto2 = ttk.Combobox(self.frame3, state = 'readonly')
                self.Cripto2.focus()
                self.Cripto2.grid(row = 2, column = 5)
                query = "Select Code FROM Code_Cripto"
                result = self.run_query(query)
                cache3 = list()
                for row  in result:
                    cache3.append(row)
                self.Cripto2["values"] = cache3
                
                #botton send Cripto
                ttk.Button(self.frame3, text = 'Ver Quien Envio', command = self.Ver_Historial).grid(row = 3, column = 4, columnspan = 2, sticky = W + E)
                
                #***************************************************************************************************
                #Creating a Frame Container
                self.frame4 = LabelFrame(self.wind, text = 'Informe')
                self.frame4.grid(row = 7, column = 1, columnspan = 5)

                #Boton Delete
                
                #ttk.Button(self.frame4, text= 'DELETE').grid(row = 8, column = 1, sticky = W + E)
                #Boton Editar
                ttk.Button(self.frame4, text= 'Actualizar USD').grid(row = 8, column = 1, columnspan = 5, sticky = W + E)

                #table
                self.tree = ttk.Treeview(self.frame4, columns = ('#1', '#2', '#3'))
                self.tree.heading('#0', text = 'Criptomoneda', anchor = CENTER)
                self.tree.heading('#1', text = 'Cantidad', anchor = CENTER)
                self.tree.heading('#2', text = 'Ultima Actualización', anchor = CENTER)
                self.tree.heading('#3', text = 'USD', anchor = CENTER)
                
                self.tree.grid(row = 9, column = 1, columnspan = 2)
                self.get_Monedas()

            if I == 0:
                showerror(title = "Login False", message = "Usuario o contraseña incorrecta")
        else:
            #self.message1['text'] = 'Name and Password is required'
            showerror(title = "Login False", message = "Ingresa por favor usuario o contraseña")
    
    def validation2(self):
        return len(self.Cripto.get()) != 0 and len(self.Usuario.get()) != 0 and len(self.Cantidad.get()) != 0

    def Enviar_Cripto(self):
        if self.validation2():
            new_name = self.Cripto.get()
            new_usuario = self.Usuario.get()
            query = 'SELECT Cant FROM Criptomonedas WHERE Name_Crip = ? and Cod_Usu = ?'
            parameters = (new_name, self.usu)
            db_rows = self.run_query(query, parameters)
            Canti = 0
            for row in db_rows:
                Canti = row[0]

            if Canti > 0:
                Cantidad2 = int(self.Cantidad.get())
                if Cantidad2 > Canti:
                    showerror(title = "Cantidad supera el limite", message = "La cantidad que se escogió está por encima de lo que se tiene")
                else:
                    new_cantidad = Canti - Cantidad2
                    FechaAct = datetime.datetime.now()
                    query = 'UPDATE Criptomonedas SET Cant = ?, Date = ? WHERE Name_Crip = ? AND Cod_Usu = ?'
                    parameters = (new_cantidad, FechaAct, new_name, self.usu)
                    self.run_query(query, parameters)
                    showinfo(title = "Información", message = "Se a descontado la cantidad enviada de tu saldo")
                    
                    query = 'SELECT Cant FROM Criptomonedas WHERE Name_Crip = ? and Cod_Usu = ?'
                    parameters = (new_name, new_usuario)
                    db_rows = self.run_query(query, parameters)
                    Canti = 0
                    for row in db_rows:
                        Canti = row[0]
                    
                    if Canti == 0:
                        FechaAct = datetime.datetime.now()
                        query = "INSERT INTO Criptomonedas VALUES (?,?,?,?)"
                        parameters = (new_name, Cantidad2, new_usuario, FechaAct)
                        self.run_query(query, parameters)

                        query = "INSERT INTO Historial VALUES (?,?,?,?,?)"
                        parameters = (self.usu, new_usuario, Cantidad2, new_name, FechaAct)
                        self.run_query(query, parameters)

                        showinfo(title = "Información", message = "Se a creado un N registro en Cripto e Historial")
                    else:
                        new_cantidad = Canti + Cantidad2
                        FechaAct = datetime.datetime.now()
                        query = 'UPDATE Criptomonedas SET Cant = ?, Date = ?  WHERE Name_Crip = ? AND Cod_Usu = ?'
                        parameters = (new_cantidad, FechaAct, new_name, new_usuario)
                        self.run_query(query, parameters)

                        query = "INSERT INTO Historial VALUES (?,?,?,?,?)"
                        parameters = (self.usu, new_usuario, Cantidad2, new_name, FechaAct)
                        self.run_query(query, parameters)

                        showinfo(title = "Información", message = "Se a modificado el registro en Cripto e Historial")
                        self.get_Monedas()
            else:
                showerror(title = "Cantidad supera el limite", message = "La cantidad que se escogió está por encima de lo que se tiene")
        else:
            showerror(title = "Error Información", message = "Se debe ingresar información en los campos")
            
    def Ver_Historial(self):
        new_name = self.Cripto2.get()
        query = 'SELECT Cantidad FROM Historial WHERE (Nombre_Envia = ? or Nombre_Recibe = ?) and Nombre_Cripto = ?'
        parameters = (self.usu, self.usu, new_name)
        db_rows = self.run_query(query, parameters)
        Canti = 0
        for row in db_rows:
            Canti = row[0]

        if Canti > 0:
            self.histor_wind = Toplevel()
            self.histor_wind.geometry ("1200x300+100+100")
            self.histor_wind.title = 'Historial de las criptomonedas'
            
            #botton send Cripto
            ttk.Button(self.histor_wind, text = 'Salir', command = self.Close_App2).grid(row = 0,column = 0)

            #Creating a Frame Container Send
            self.frame5 = LabelFrame(self.histor_wind, text = 'Historial')
            self.frame5.grid(row = 1, column = 1)

            #table
            self.tree2 = ttk.Treeview(self.frame5, columns = ('#1', '#2', '#3', '#4'))
            self.tree2.heading('#0', text = 'Nombre De Quien Envia', anchor = CENTER)
            self.tree2.heading('#1', text = 'Nombre De Quien Recibe', anchor = CENTER)
            self.tree2.heading('#2', text = 'Cantidad', anchor = CENTER)
            self.tree2.heading('#3', text = 'Criptomoneda', anchor = CENTER)
            self.tree2.heading('#4', text = 'Fecha de Movimiento', anchor = CENTER)
                
            self.tree2.grid(row = 9, column = 1, columnspan = 2)
            self.get_Monedas2()

        else:
            showerror(title = "Error Información", message = "La critomoneda seleccionada no tiene historial")

    def get_Monedas(self):
        #Limpiar la consulta para una nueva
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            
        #realizamos la consulta
        query = 'SELECT Name_Crip, Cant, Date FROM Criptomonedas WHERE Cod_Usu = ?'
        db_rows = self.run_query(query, (self.usu,))
        #mostramos la consulta
        for row in db_rows:
            moneda = row[0]
            JsonApi = self.get_price(moneda+"USDT").json()
            valor_USD = float(JsonApi["price"]) * row[1]
            #valor_USD = 10
            self.tree.insert("", 0, text = row[0], value = (row[1], row[2], '{:,.2f}'.format(valor_USD)))
    
    def get_Monedas2(self):
        #Limpiar la consulta para una nueva
        records = self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)
            
        #realizamos la consulta
        new_name = self.Cripto2.get()
        query = 'SELECT * FROM Historial WHERE (Nombre_Envia = ? or Nombre_Recibe = ?) and Nombre_Cripto = ?'
        parameters = (self.usu, self.usu, new_name)
        db_rows = self.run_query(query, parameters)
        #mostramos la consulta
        for row in db_rows:
            print(row)
            self.tree2.insert("", 0, text = row[0], value = (row[1], row[2], row[3], row[4]))
    
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def url(self, API):
        return self._ENDPOINT+API
    
    def get_price(self, CRIPTO):
        return requests.get(self.url("/api/v3/ticker/price?symbol="+CRIPTO))
    
    def Close_App(self):
        self.wind.destroy()

    def Close_App2(self):
        self.histor_wind.destroy()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()