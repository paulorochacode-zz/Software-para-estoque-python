from tkinter import*
from sqlite3 import*
import sqlite3
from tkinter.font import BOLD
from tkinter import filedialog
import xmltodict
# coding:utf-8
banco = sqlite3.connect('sesvtrambit.db')
cursor = banco.cursor()



planejamento = Tk()
planejamento.title("Planejamento - Sadic2")
planejamento.geometry("1000x400+150+150")
planejamento.configure(background="white")
planejamento.iconbitmap('images/icon.ico')



def our_command():
    print ('hellow menu')

def telarecebimento():
    Labelprincipal = Label(planejamento, text="RECEBIMENTO", borderwidth=1, relief = "solid", font = ("ArialBlack",19, BOLD))
    Labelprincipal.place(x=200, y=30)
    
    def abrirxml():
        
        def retornaDicionario (xml):
            return xmltodict.parse(xml)
        
        def inserirNoBanco(dicionario):
            sesv1 = "00001"
            #sesv 00001
            banco = sqlite3.connect('sesvtrambit.db')
            cursor = banco.cursor()
            enderecoraiz = "A00.R00.P00.N00"
            #cursor.execute(" CREATE TABLE '"+sesv1+"' (endereco text,ean integer,quantidade integer)")
            cursor.execute(" INSERT INTO '"+sesv1+"' ('endereco' , 'ean', 'quantidade') VALUES ( '"+enderecoraiz+"', '"+dicionario['ean']+"' , '"+dicionario['quantidade']+"')")
            banco.commit()

        if __name__ == '__main__':
            with open ('sesv.xml') as f:
                data = f.read()
            
            dicionario = retornaDicionario(data)
            print(dicionario)
            for i in dicionario['sesv']['produtos']:
                inserirNoBanco(i)

        

        
        
        #filenames1 = filedialog.askopenfilenames(filetypes=[("Arquivo XML", (".xml",)), ("arquivo de texto", ".txt")])
        #print (filenames1)

       




    
    def abrirxlsx():
        filenames2 = filedialog.askopenfilenames(filetypes=[("Arquivo Excel", (".xlsx",)),("Arquivo Excel < 2016",(".xls",))])
        print (filenames2)

    Frameuploud = Frame(planejamento, pady=7, padx=7, bg = "Gainsboro", borderwidth=1,relief = "solid")
    Frameuploud.place(x=50, y=100)
    LabelFrame = Label(Frameuploud, text = "Carregar arquivo XML", borderwidth=1, relief="solid",anchor=N, pady=9,padx=40, font = ("ArialBlack",10, BOLD),)
    LabelFrame.pack(side= "top")
    botaoXML = Button(Frameuploud, text ="Procurar",command=abrirxml)
    botaoXML.pack(side= "bottom")

    Frameuploud2 = Frame(planejamento, pady=7, padx=7, bg = "Gainsboro", borderwidth=1,relief = "solid")
    Frameuploud2.place(x=350, y=100)
    LabelFrame = Label(Frameuploud2, text = "Carregar Banco de dados Excel",borderwidth=1, relief="solid",anchor=N,font = ("ArialBlack",10, BOLD),pady=9,padx=7,)
    LabelFrame.pack(side="top")
    botaoExcel = Button(Frameuploud2, text ="Procurar",command=abrirxlsx)
    botaoExcel.pack(side="bottom")

    
    

my_menu = Menu(planejamento)
planejamento.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="operação", menu=file_menu)
file_menu.add_command(label="Processo de Recebimento", command=telarecebimento)



file_menu.add_command(label="Gerar Lista de Separação")
file_menu.add_command(label="Expedir Carga", command= our_command )
file_menu.add_command(label="Sair",command = planejamento.quit)


planejamento.mainloop()
