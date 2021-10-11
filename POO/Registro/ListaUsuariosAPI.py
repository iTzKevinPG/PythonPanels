import tkinter as tk
from tkinter import * 
from tkinter import ttk
import requests


def loadData(data):

    for user in data['data']:

        userExtraData = []
        idUsuario = user['id']
        userExtraData.append(f"{user['name']}")
        userExtraData.append(f"{user['email']}")
        treeViewTable.insert("",END, text=idUsuario, values=userExtraData, tags=('gr',))

    pass

def getApi(pageId):
    
    apiRequest = requests.get(f'https://gorest.co.in/public/v1/users?page={pageId}')

    return apiRequest

def getUsers():

    for item in treeViewTable.get_children():
        treeViewTable.delete(item)

    paginaUsuarios = pageVariable.get()

    if paginaUsuarios == '':
        paginaUsuarios = 1
        pass

    apiRequest = getApi(paginaUsuarios)
    data = apiRequest.json()

    loadData(data)

    numberPage.delete(0,END)

    pass


mainWindow = tk.Tk()
mainWindow.geometry("700x500")
mainWindow.title("Ingreso Usuarios")
mainWindow.resizable(False, False)
mainWindow.iconbitmap("POO\Imagenes\github.ico")
mainWindow.config(background = "#484848")

title = Label(text="Formulario de Ingreso Usuarios", font=("Cambria", 13), bg="#FFC500", fg="black", width="450", height="2")
title.pack()

pageText = Label(text="Pagina:", font=("Cambria", 10), bg="#B5B5B5")
pageText.place(x=100, y=70)

pageVariable = StringVar()

numberPage = Entry(textvariable=pageVariable, font=("Cambria", 10), width="70", bg="#D1D1D1")
numberPage.place(x=100, y=100)

buttonLoad = Button(mainWindow, text="Cargar", command=getUsers,font=("Cambria", 11), width="20", height="2", bg="#FFC500")
buttonLoad.place(x=250, y=140)

style = ttk.Style(mainWindow)
style.theme_use("clam")
style.configure("Treeview", background="#D1D1D1", fieldbackground="#D1D1D1", foreground="#D1D1D1", font=("Cambria", 10), anchor=CENTER)

treeViewTable = ttk.Treeview(mainWindow, columns="#0, #1")
treeViewTable.tag_configure('gr', background='#D1D1D1')
treeViewTable.place(x=50, y=220)
treeViewTable.heading("#0", text="Id", anchor=CENTER)
treeViewTable.heading("#1", text="Nombre", anchor=CENTER)
treeViewTable.heading("#2", text="Email", anchor=CENTER)

mainWindow.mainloop()