from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from sqlite3 import*
from telaEntrada import *

#Conexão com banco
banco = sqlite3.connect('dados.db')
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 Name TEXT NOT NULL,
 Email TEXT NOT NULL,
 User TEXT NOT NULL,
 Password TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")

#Criar Janela
jan = Tk()
jan.title("Tela de Login - Sadic2")
jan.geometry("1000x400+150+150")
jan.configure(background="white")
jan.resizable(width=False, height=False) #não é possivel alterar o tamanho da janela
jan.iconbitmap('images/icon.ico')
jan.attributes("-alpha",0.9) #transparencia na janela
#Carregando Imagens

logo = PhotoImage(file="images/estoque-eficiente.png")#Python e Tkinter trabalham com arquivos de imagens .png

#Widgets
LeftFrame = Frame(jan, width=600, height=400, relief="raise") #Lado esquerdo da janela
LeftFrame.place(x=0, y=0)

RightFrame = Frame(jan, width=600, height=400, bg="MIDNIGHTBLUE" , relief="raise")#Lado direito da janela
RightFrame.place(x=500 , y=0)

#exibir imagem
#Frame da esquerda
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=0, y=0)

#Usuario, Login
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

#Entrada de dados - Username
UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=160, y=110)

#Password
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=12, y=150)

#Entrada de dados - Password
PassEntry = ttk.Entry(RightFrame, width=25, show="*")
PassEntry.place(x=160, y=160)



def q(event):
        telaDeEntrada2()
def w(event):
        telaSeparacao() 
def e(event):
        telaDeConferencia()
def r(event):
        telaDeMovimentacao()
def t(event):
        ConsultarEndereco()
def y(event):
        ConsultarProduto()

def loged():
        jan.title("Logado - Sadic2")
        jan.configure(background="white")

        frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
        frameBranco.pack()        
        frame = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame.place(x=120, y=24)
        frame2 = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame2.place(x=120, y=87)
        frame3 = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame3.place(x=120, y=150) 
        frame4 = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame4.place(x=120, y=213)  
        frame5 = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame5.place(x=120, y=276)
        frame6 = LabelFrame(jan,bg="MIDNIGHTBLUE",bd=5, relief="ridge")
        frame6.place(x=120, y=339)

                        
        PassLabel1 = Label(frame,padx=10, text="Recebimento", font=("Century Gothic", 13, BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel1.grid(row=1, column=1)
        PassLabel = Label(frame, text="                       ", font=("Century Gothic", 13),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)
        PassLabel = Label(frame2,padx=10, text="Separar", font=("Century Gothic", 13,BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=1)
        PassLabel = Label(frame2, text="                                ", font=("Century Gothic", 13),  anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)
        PassLabel = Label(frame3,padx=10, text="Conferir", font=("Century Gothic", 13,BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=1)
        PassLabel = Label(frame3, text="                                ", font=("Century Gothic", 13),  anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)
        PassLabel = Label(frame4,padx=10, text="Movimentar", font=("Century Gothic", 13,BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=1)
        PassLabel = Label(frame4, text="                         ", font=("Century Gothic", 13),  anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)
        PassLabel = Label(frame5,padx=10, text="Consultar Endereço", font=("Century Gothic", 13,BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=1)
        PassLabel = Label(frame5, text="             ", font=("Century Gothic", 13),  anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)
        PassLabel = Label(frame6,padx=10, text="Consultar Produto", font=("Century Gothic", 13,BOLD),anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=1)
        PassLabel = Label(frame6, text="                ", font=("Century Gothic", 13),  anchor=W, bg="MIDNIGHTBLUE", fg="white",justify =LEFT)
        PassLabel.grid(row=1, column=2)


        PassLabel = Label(jan,padx=10,pady=10, text="Q", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=15)
        PassLabel = Label(jan,padx=10,pady=10, text="W", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=79)
        PassLabel = Label(jan,padx=14,pady=10, text="E", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=143)
        PassLabel = Label(jan,padx=13,pady=10, text="R", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=207)
        PassLabel = Label(jan,padx=15,pady=10, text="T", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=271)
        PassLabel = Label(jan,padx=13,pady=10, text="Y", font=("Century Gothic", 15,BOLD), bg="MIDNIGHTBLUE", fg="white",bd=5, relief="ridge")
        PassLabel.place(x=80, y=335)


        jan.bind("<q>", q)
        jan.bind("<w>", w)
        jan.bind("<e>", e)
        jan.bind("<r>", r)
        jan.bind("<t>", t)
        jan.bind("<y>", y)
    
def telaSeparacao():
    frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
    frameBranco.place(x=0,y=0)
    jan.title("Separação - Sadic2")
    jan.configure(background="white")
    frameentrada = Frame(jan, height=100,width=100)
    frameentrada.place(x=100,y=60)
    lista = ttk.Entry(frameentrada)
    lista.grid(row=0, column=1)
    lista.focus()
    label = Label(frameentrada, text="Lista :",bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label = label.grid(row=0, column=0)
    botãoconsulta = ttk.Button(frameentrada, text="Consultar",)
    botãoconsulta.grid(row=0,column=2)

def telaDeConferencia():
    jan.title("Conferencia - Sadic2")
    frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
    frameBranco.place(x=0,y=0)
    frameentrada = Frame(jan, height=100,width=100)
    frameentrada.place(x=100,y=60)
    lista = ttk.Entry(frameentrada)
    lista.grid(row=0,column=1)
    lista.focus()
    label = Label(frameentrada, text="Lista :",bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label = label.grid(row=0,column=0)
    botãoconsulta = ttk.Button(frameentrada, text="Consultar",)
    botãoconsulta.grid(row=0,column=2)

def telaDeMovimentacao():
    jan.title("Movimentação - Sadic2")
    frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
    frameBranco.place(x=0,y=0)
    def consulta():
        endereco1 = lista1.get()
        ean = lista2.get()
        quantidade =  lista3.get()
        endereco2 = lista4.get()
        

        if (endereco1 == ""):
            labelean = Label(jan, text= 'Insira o EAN*',bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
            labelean.place(x=400, y=60)
            if (ean == ""):
                labelend = Label(jan, text= 'Insira o Endereço Origem*', bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
                labelend.place(x=400, y=35)
                if (quantidade == ""):
                    labelqtd = Label(jan, text= 'Insira a Quantidade*',bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
                    labelqtd.place(x=400, y=85)
                    if (endereco2 == ""):
                        labeldest = Label(jan, text= 'Insira o Endereço Destino*',bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
                        labeldest.place(x=400, y=110)
        else :
            try :
                cursor.execute("SELECT saldo FROM enderecamento WHERE endereco = '"+endereco1+"' AND id = '"+ean+"'")
                print(cursor.fetchone()[0])
                chave = 1
            except :
                print('endereco de origem nao existe')
                chave = 0
            try :
                cursor.execute("SELECT saldo FROM enderecamento WHERE endereco = '"+endereco1+"' AND id = '"+ean+"'")
                var9 = (int(cursor.fetchone()[0]) < int(quantidade))
                if (var9 == True):
                    print ('saldo do endereco menor que a quantidade')
                    chave2 = 0
                else :
                    chave2 = 1     
            except :
                    chave2 = 0
                    print("Nao ha saldo suficiente no endereço origem")

                
            try :
                cursor.execute("SELECT saldo FROM enderecamento WHERE endereco = '"+endereco1+"' AND id = '"+ean+"'")
                var8 = (int(cursor.fetchone()[0]) == 0)
                if (var8 == False):
                    print (var8)
                    chave3 = 1
                else :
                    print ('saldo do endereco origem igual a 0')
                    chave3 = 0
                      
            except: 
                print("Nao ha saldo no endereco origem")
                chave3 = 0
            
            if (chave and chave2 and chave3 == 1):    
                #inserir registro caso tiver saldo, mas não tiver registro
                try:
                    #verificando se existe linha
                    cursor.execute("SELECT saldo FROM enderecamento WHERE endereco = '"+endereco2+"' AND id = '"+ean+"' ")
                    var7 = (int(cursor.fetchone()[0]))
                    print ("existe linha")


                except:            
                    cursor.execute(" INSERT INTO enderecamento VALUES ( '"+endereco2+"', '"+ean+"' , '"+quantidade+"')")
                    banco.commit()        
                    print ("insercao")
                        
                #caso o endereço 1 tenha saldo
                cursor.execute("SELECT saldo FROM enderecamento WHERE id = '"+ean+"' AND saldo > 0 AND endereco ='"+endereco1+"' ")
                var = int(cursor.fetchone()[0])
                print ('essa é' + str(var))
                var2 = int(var) - int(quantidade)
                var2 = str(var2)
                print (var2)                
                cursor.execute("UPDATE enderecamento SET saldo = '"+var2+"' WHERE endereco = '"+endereco1+"' AND id = '"+ean+"' ")
                banco.commit()

                                                
                cursor.execute("SELECT saldo FROM enderecamento WHERE endereco = '"+endereco2+"' AND id = '"+ean+"' AND saldo >= 0 ")
                var3 = int(cursor.fetchone()[0])
                var4 = int(var3) + int(quantidade)
                var4 = str(var4)
                cursor.execute("UPDATE enderecamento SET saldo = '"+var4+"' WHERE endereco = '"+endereco2+"' AND id = '"+ean+"' ")
                banco.commit()
                                                

                lista1.delete(0, 'end')
                lista2.delete(0, 'end')
                lista3.delete(0, 'end')
                lista4.delete(0, 'end')
                print ('movimentacao concluida')                                        
            else:
                print('movimentacao nao concluida.')

    lista1 = ttk.Entry(jan)
    lista1.place(x=270, y=35)
    lista2 = ttk.Entry(jan)
    lista2.place(x=270, y=60)
    lista3 = ttk.Entry(jan)
    lista3.place(x=270, y=85)
    lista4 = ttk.Entry(jan)
    lista4.place(x=270, y=110)
        
    label1 = Label(jan, text="Endereço Origem:", bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label1 = label1.place(x= 100, y=35)
    label2 = Label(jan, text="EAN:", bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label2 = label2.place(x= 100, y=60)
    label3 = Label(jan, text="Quantidade:", bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label3 = label3.place(x= 100, y=85)
    label4 = Label(jan, text="Endereço Destino:", bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label4 = label4.place(x= 100, y=110)
    lista1.focus()
    botãoconsulta = ttk.Button(jan, text="Movimentar", command= consulta)
    botãoconsulta.place(x = 400, y = 150)

def ConsultarEndereco():
    jan.title("Consulta de endereço - Sadic2")
    frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
    frameBranco.place(x=0,y=0)
    mainFrame = Frame(jan,height=500,width=100,relief = "solid", borderwidth= 2, padx=5,pady=5)
    mainFrame.place(x=70,y=20)
    frameentrada = Frame(mainFrame, height=100,width=330,relief = "solid", borderwidth=2, padx=17,pady=5, bg= "white")
    frameentrada.grid(row=0,column=0)
    frameintermedio = Frame(mainFrame,height=40,width=330,relief= "solid",borderwidth=2, padx=5,bg= "white")
    frameintermedio.grid(row=1,column=0)
    framesaida = Frame(mainFrame,height=250,width=330,relief = "solid", borderwidth=2,bg= "white")
    framesaida.grid(row=2,column=0)
    lista = ttk.Entry(frameentrada)
    lista.grid(row=0,column=1)
    def consulta():    
        
        if lista.get() != '':
            try :
                consulta = lista.get()
                cursor.execute("SELECT * FROM enderecamento WHERE endereco = '"+consulta+"' AND saldo >= 1")
                consultado = cursor.fetchall()
                altura = 110
                for consults in consultado:
                    labelEAN = Label(jan, text=consults[1],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1)
                    labelEAN.place(x=250, y=altura)
                    labelendereco = Label(jan, text=consults[0],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1)
                    labelendereco.place(x=80, y=altura)
                    labelQuantidade = Label(jan, text=consults[2],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1,padx=7)
                    labelQuantidade.place(x=370, y=altura)
                    altura = altura + 30
                    print(consults)
                labelCabecalho = Label(jan, text="ENDEREÇO         EAN        SALDO",bg="white", fg= "black", font=("Century Gothic", 15, BOLD),)
                labelCabecalho.place(x=80, y=70)
                lista.delete(0, 'end')
            except :
                labelconsultado = Label(jan, text="Nenhum Endereço Encontrado     ",bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
                labelconsultado.place(x= 100, y= 70)
        else : 
            labelconsulted = Label(jan, text="Campo Vazio               ",bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
            labelconsulted.place(x= 100, y= 70)


    lista = ttk.Entry(frameentrada)
    lista.grid(row=0,column=1)
    label = Label(frameentrada, text="Endereço:",bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label.grid(row=0,column=0)
    btnconsulta = ttk.Button(frameentrada, text="Consultar", command=consulta)
    btnconsulta.grid(row=0,column=2)

def ConsultarProduto():
    jan.title("Consulta de produto - Sadic2")
    frameBranco = Frame(jan,width=1000,height=1000, bg= "white")
    frameBranco.place(x=0,y=0)
    mainFrame = Frame(jan,height=500,width=100,relief = "solid", borderwidth= 2, padx=5,pady=5)
    mainFrame.place(x=70,y=20)
    frameentrada = Frame(mainFrame, height=100,width=330,relief = "solid", borderwidth=2, padx=5,pady=5, bg= "white")
    frameentrada.grid(row=0,column=0)
    frameintermedio = Frame(mainFrame,height=40,width=330,relief= "solid",borderwidth=2, padx=5,bg= "white")
    frameintermedio.grid(row=1,column=0)
    framesaida = Frame(mainFrame,height=250,width=330,relief = "solid", borderwidth=2,bg= "white")
    framesaida.grid(row=2,column=0)
    lista = ttk.Entry(frameentrada)
    lista.grid(row=0,column=1)
    
    def consulta(): 
        
        if (lista.get() != ''):
            global chave01
            chave01 = True
            try :
                consulta = (lista.get())
                cursor.execute("SELECT * FROM enderecamento WHERE id = '"+consulta+"' AND saldo >= 1 ")
                consultado = cursor.fetchall()
                print(consultado)
                altura = 110
                for consults in consultado:
                    labelEAN = Label(jan, text=consults[1],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1)
                    labelEAN.place(x=90, y=altura)
                    labelendereco = Label(jan, text=consults[0],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1)
                    labelendereco.place(x=180, y=altura)
                    labelQuantidade = Label(jan, text=consults[2],bg="white", fg= "black", font=("Century Gothic", 13, BOLD),relief="solid", borderwidth=1,padx=7)
                    labelQuantidade.place(x=370, y=altura)
                    altura = altura + 25
                labelCabecalho = Label(jan, text=" EAN          ENDEREÇO      SALDO",bg="white", fg= "black", font=("Century Gothic", 15, BOLD),)
                labelCabecalho.place(x=80, y=70)
                lista.delete(0, 'end')
                global chave02
                chave02 = False
            except :
                labelconsultado = Label(jan, text="Nenhum EAN Encontrado    ", bg="white", fg= "red", font=("Century Gothic", 13, BOLD),width=300)
                labelconsultado.place(x=100, y=70)
                chave02 = False
        else:
            labelconsultadoNa = Label(jan, text="Campo Vazio             ", bg="white", fg= "red", font=("Century Gothic", 13, BOLD),)
            labelconsultadoNa.place(x=100, y=70)
            chave01 = False

        if (chave01 and chave02 == True ):
            labelconsultado = Label(jan, text="Nenhum EAN Encontrado    ", bg="white", fg= "red", font=("Century Gothic", 13, BOLD))
            labelconsultado.place(x=100, y=70)
        else:
            pass
    
    label = Label(frameentrada, text="EAN Produto:", bg="white", fg= "black", font=("Century Gothic", 13, BOLD),)
    label.grid(row=0,column=0)
    botãoconsulta = ttk.Button(frameentrada, text="Consultar", command=consulta)
    botãoconsulta.grid(row=0,column=2)



def loginbotao():
    User = UserEntry.get()
    Pass = PassEntry.get()
    cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Logado")
    verifylogin = cursor.fetchone()
    try: 
        if (User in verifylogin and Pass in verifylogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo!")
            loged()
    except:
            messagebox.showinfo(title="Login Info", message="Acesso Negado, Verifique se está cadastrado no sistema")    

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=25, command=loginbotao)
LoginButton.place(x=160, y=225)



def register():
    #Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=65, y=5)
    
    NomeEntry = ttk.Entry(RightFrame, width=25)
    NomeEntry.place(x=160, y=10)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=65, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=25)
    EmailEntry.place(x=160, y=60)

    def registertodatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os Campos")
        else:
            cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            banco.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com Sucesso")
        
    Register = ttk.Button(RightFrame, text="Registrar", width=15, command=registertodatabase)
    Register.place(x=10,y=225)

    def backtologin():
        #removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os widgets de login
        LoginButton.place(x=150, y=225)
        RegisterButton.place(x=150, y=260)

    Back = ttk.Button(RightFrame, text="Voltar", width=15, command=backtologin)
    Back.place(x=10, y=260)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=25, command=register)
RegisterButton.place(x=160, y=260)
jan.mainloop()
