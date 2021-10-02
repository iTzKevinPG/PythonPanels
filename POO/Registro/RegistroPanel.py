import tkinter as tk
from tkinter import * 
from tkinter import ttk
from datetime import date
from datetime import datetime

def sendData():

    contacts = []
    today = date.today()
    now = datetime.now()

    userNameData = username.get()
    contacts.append(f'{today.strftime("%b-%d-%Y")}')
    contacts.append(f'{now.strftime("%H:%M:%S")}')

    tableList.insert("",END, text=userNameData, values=contacts, tags=('gr',))

    userNameEntry.delete(0,END)

    pass

myWindow = tk.Tk()

myWindow.geometry("650x450")
myWindow.title("Git Hub Page")
myWindow.resizable(False, False)
myWindow.iconbitmap("POO\Imagenes\github.ico")
myWindow.config(background = "#484848")

main_title = Label(text="Formulario de registro", font=("Cambria", 13), bg="#FFC500", fg="black", width="450", height="2")
main_title.pack()

userNameLabel = Label(text="Nombre Usuario", font=("Cambria", 10), bg="#B5B5B5")
userNameLabel.place(x=200, y=70)

username = StringVar()

userNameEntry = Entry(textvariable=username, width="40", bg="#D1D1D1")

userNameEntry.place(x=200, y=100)

btnRegister = Button(myWindow, text="Registrar", command=sendData, width="30", height="2", bg="#FFC500")
btnRegister.place(x=200, y=150)

style = ttk.Style(myWindow)
style.theme_use("clam")
style.configure("Treeview", background="#D1D1D1", fieldbackground="#D1D1D1", foreground="#D1D1D1")

tableList = ttk.Treeview(myWindow, columns="#0, #1")
tableList.tag_configure('gr', background='#D1D1D1')
tableList.place(x=25, y=200)
tableList.heading("#0", text="Nombre", anchor=CENTER)
tableList.heading("#1", text="Fecha", anchor=CENTER)
tableList.heading("#2", text="Hora", anchor=CENTER)

myWindow.mainloop()