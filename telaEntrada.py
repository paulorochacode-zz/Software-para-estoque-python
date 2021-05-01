from tkinter import*
from sqlite3 import*
import sqlite3
from tkinter.font import BOLD
from tkinter import ttk

banco = sqlite3.connect('sesvtrambit.db')
cursor = banco.cursor()


def telaDeEntrada2():
    telaDeEntrada = Tk()
    telaDeEntrada.title("Entrada - Sadic2")
    telaDeEntrada.geometry("1000x400+150+150")
    telaDeEntrada.configure(background="white")
    telaDeEntrada.iconbitmap('images/icon.ico')
    frameentrada = Frame(telaDeEntrada, height=100,width=100)
    frameentrada.place(x=100,y=60)
    sesv = ttk.Entry(frameentrada)
    sesv.grid(row=0, column =1)
    label = Label(frameentrada, text="SESV :",bg="white", fg= "black", font=("Century Gothic", 13, BOLD),padx=8)
    label.grid(row=0, column=0)
    telaDeEntrada.focus_force
    consulta = sesv.get()
    print (sesv.get())
    
    

    def consultarsesv():
        print (sesv.get())
        consulta = sesv.get()
        if (sesv.get() != '' or NONE):
            try :
                banco = sqlite3.connect('sesvtrambit.db')
                cursor.execute("SELECT * FROM '"+consulta+"' ")
                consultado = cursor.fetchall()
                altura = 170
                for consults in consultado:
                    labelconsulta = Label(telaDeEntrada, text=consults,bg="white", fg= "black", font=("Century Gothic", 13, BOLD), relief="solid", borderwidth=1)
                    sesv.delete(0, 'end')
                    labelconsulta.place(x= 100, y=altura)
                    altura = altura + 30
            except :
                labelconsultado = Label(telaDeEntrada, text="Nenhuma SESV Encontrada     " ,bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
                labelconsultado.place(x=100, y=100)
        else:
            labelconsultado2 = Label(frameentrada, text="Insira uma SESV            " ,bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
            labelconsultado2.place(x= 125, y= 100)
    botãoconsulta = ttk.Button(frameentrada, text="Consultar",command=consultarsesv)
    botãoconsulta.grid(row=0, column=3)
