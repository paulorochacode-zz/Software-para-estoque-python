
from tkinter import*
from sqlite3 import*
import sqlite3
from tkinter.font import BOLD
from tkinter import filedialog
import xmltodict
from tkinter import ttk

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
    
    print('mamação')
    def abrirxml():
        filenames1 = filedialog.askopenfilenames(filetypes=[("Arquivo XML", (".xml",)), ("arquivo de texto", ".txt")])
        print (filenames1)
        caminhoXML= str(filenames1[0])
        
        #insere no banco
        def retornaDicionario (xml):
            return xmltodict.parse(xml)
        
        #mostrarsesv

        def inserirNoBanco(dicionario):
            sesv1 = "00001"
            enderecoraiz = "REC.R00.P00.N00"
            #cursor.execute(" CREATE TABLE '"+sesv1+"' (endereco text,ean integer,quantidade integer)")
            #cursor.execute(" INSERT INTO '"+sesv1+"' ('endereco' , 'ean', 'quantidade') VALUES ( '"+enderecoraiz+"', '"+dicionario['ean']+"' , '"+dicionario['quantidade']+"')")
            #banco.commit()

            

        
        if __name__ == '__main__':
            with open (caminhoXML) as f:
                data = f.read()
            
            frameViewSesv = Frame(planejamento,relief="solid", borderwidth=1, width=400,height=400,bg="white",pady=5,padx=5)
            frameViewSesv.place(x=600, y=50)
            dicionario = retornaDicionario(data)
            #print(dicionario)
            linha = 0
            for i in dicionario['sesv']['produtos']:
                varean = i['ean']
                varqtd = i['quantidade']
                
                labelViewSesvean = Label(frameViewSesv,text=varean,font=("Century Gothic", 13, BOLD), padx=10,pady=5,bg='white',relief="solid", borderwidth=1 )
                labelViewSesvean.grid(row=linha,column=0)
                labelViewSesvqtd = Label(frameViewSesv,text=varqtd,font=("Century Gothic", 13, BOLD),padx=36,pady=5,bg='white',relief="solid", borderwidth=1 )
                labelViewSesvqtd.grid(row=linha,column=1,padx=12)
                linha = linha+1
                print("ean --" + i['ean'] + "   ""quantidade --" + i['quantidade'])
                #print("quantidade  -" + i['quantidade'])

              
            labelViewSesveanp = Label(planejamento,text="EAN",relief="solid", borderwidth=1,font=("Century Gothic", 13, BOLD), padx=5,pady=5,anchor =W,width=15,bg='white' )
            labelViewSesveanp.place(x=600, y=20)
            labelViewSesvqtdp = Label(planejamento,text="Quantidade",relief="solid", borderwidth=1,font=("Century Gothic", 13, BOLD), padx=5,pady=5,anchor =W,width=10,bg='white' )
            labelViewSesvqtdp.place(x=760, y=20)
            

        def inserirNoBanco():
            sesv1 = "00001"
            enderecoraiz = "REC.R00.P00.N00"
            #cursor.execute(" CREATE TABLE '"+sesv1+"' (endereco text,ean integer,quantidade integer)")
            cursor.execute(" INSERT INTO '"+sesv1+"' ('endereco' , 'ean', 'quantidade') VALUES ( '"+enderecoraiz+"', '"+dicionario['ean']+"' , '"+dicionario['quantidade']+"')")
            banco.commit()

        
        
        if __name__ == '__main__':
            with open (caminhoXML) as f:
                data = f.read()
            
            dicionario = retornaDicionario(data)
            #print(dicionario)
            for i in dicionario['sesv']['produtos']:
                inserirNoBanco(i)
    

    
    def abrirxlsx():
        filenames2 = filedialog.askopenfilenames(filetypes=[("Arquivo Excel", (".xlsx",)),("Arquivo Excel < 2016",(".xls",))])
        print (filenames2)
    
    Labelprincipal = Label(planejamento, text="Receber Notas", borderwidth=1, relief = "solid", font = ("ArialBlack",19, BOLD),pady=5,padx=5)
    Labelprincipal.place(x=80, y=30)
    botaocarregarSESV = ttk.Button(planejamento, text ="Receber nota")
    botaocarregarSESV.place(x=900, y=350)
    Frameuploud = Frame(planejamento, pady=7, padx=7, bg = "Gainsboro", borderwidth=1,relief = "solid")
    Frameuploud.place(x=50, y=100)
    LabelFrame = Label(Frameuploud, text = "Carregar arquivo XML", borderwidth=1, relief="solid",anchor=N, pady=9,padx=40, font = ("ArialBlack",10, BOLD),)
    LabelFrame.pack(side= "top")
    botaoXML = ttk.Button(Frameuploud, text ="Procurar",command=abrirxml)
    botaoXML.pack(side= "bottom")

    Frameuploud2 = Frame(planejamento, pady=7, padx=10, bg = "Gainsboro", borderwidth=1,relief = "solid")
    Frameuploud2.place(x=50, y=200)
    LabelFrame = Label(Frameuploud2, text = "Carregar Banco de Excel",borderwidth=1, relief="solid",anchor=N,font = ("ArialBlack",10, BOLD),pady=9,padx=28,)
    LabelFrame.pack(side="top")
    botaoExcel = ttk.Button(Frameuploud2, text ="Procurar",command=abrirxlsx)
    botaoExcel.pack(side="bottom")

    
    

my_menu = Menu(planejamento)
planejamento.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Recebimento", menu=file_menu)
file_menu.add_command(label="Carregar Notas", command=telarecebimento)



file_menu.add_command(label="Gerar Lista de Separação")
file_menu.add_command(label="Expedir Carga", command= our_command )
file_menu.add_command(label="Sair",command = planejamento.quit)


planejamento.mainloop()
