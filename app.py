from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector
from PIL import Image, ImageTk

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'escola_ete'
)
cursor = conexao.cursor()

def limpar():
    e_name.delete(0, END)
    e_cpf.delete(0, END)
    e_rg.delete(0, END)
    e_matricula.delete(0, END)
    e_sexo.delete(0, END)
    e_telefone.delete(0, END)
    e_endereço.delete(0, END)
    e_responsavel.delete(0, END)
    e_datanascimento.delete(0, END)
    

#funções botões
def insert ():
    name = e_name.get()
    cpf = e_cpf.get()
    rg = e_rg.get()
    matricula = e_matricula.get()
    sexo = e_sexo.get()
    telefone = e_telefone.get()
    endereço = e_endereço.get()
    responsavel = e_responsavel.get()
    datanascimento = e_datanascimento.get()
    if(name=="" or cpf =="" or rg=="" or matricula =="" or sexo=="" or telefone =="" or endereço=="" or responsavel =="" or datanascimento==""):
        MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
    else:
        try:
            cursor.execute("select cpf from aluno where cpf  = '"+ e_cpf.get() +"'")
            teste = cursor.fetchall()
            if e_cpf.get() == (f"{teste[0][0]}"):
                e_cpf.delete(0, 'end')
                MessageBox.showinfo("ERRO!", "Usúario Já cadastrado")
                limpar()

        except:    
            comando = f"INSERT INTO aluno(nome, cpf, rg, matricula, sexo, telefone, endereço, responsavel, data_nascimento) VALUES ('{name}','{cpf}','{rg}','{matricula}','{sexo}','{telefone}','{endereço}','{responsavel}','{datanascimento}')"
            MessageBox.showinfo("Sucesso!", "Aluno inserido com sucesso!")
            cursor.execute(comando)
            conexao.commit()
            limpar()

def delete ():
    name = e_name.get()
    cpf = e_cpf.get()
    rg = e_rg.get()
    matricula = e_matricula.get()
    sexo = e_sexo.get()
    telefone = e_telefone.get()
    endereço = e_endereço.get()
    responsavel = e_responsavel.get()
    datanascimento = e_datanascimento.get()
    if(name=="" or cpf =="" or rg=="" or matricula =="" or sexo=="" or telefone =="" or endereço=="" or responsavel =="" or datanascimento==""):
        MessageBox.showinfo("Erro", "Selecione um registro para deletar!")

    else:
        comando = f'DELETE FROM aluno WHERE cpf = {cpf}' 
        cursor.execute(comando)
        conexao.commit()
        MessageBox.showinfo("Sucesso!", "Registro excluido com sucesso!")
        cursor.execute(comando)
        conexao.commit()
        limpar()

def update ():
    name = e_name.get()
    cpf = e_cpf.get()
    rg = e_rg.get()
    matricula = e_matricula.get()
    sexo = e_sexo.get()
    telefone = e_telefone.get()
    endereço = e_endereço.get()
    responsavel = e_responsavel.get()
    datanascimento = e_datanascimento.get()
    if(name=="" or cpf =="" or rg=="" or matricula =="" or sexo=="" or telefone =="" or endereço=="" or responsavel =="" or datanascimento==""):
        MessageBox.showinfo("Erro", "Selecione um registro para atualizar!")
   
    else:
        comando = f"UPDATE aluno SET nome= '{name}',cpf= '{cpf}',rg= '{rg}',matricula= '{matricula}',sexo= '{sexo}',telefone= '{telefone}',endereço= '{endereço}',responsavel ='{responsavel}' ,data_nascimento='{datanascimento}' WHERE cpf = {cpf}"
        cursor.execute(comando)
        conexao.commit()
        MessageBox.showinfo("Sucesso!", "Registro alterado com sucesso!")
        limpar()
    
def buscar ():    
    cpf = e_cpf.get()
    if(cpf==''):
        MessageBox.showinfo("campo obrigatorio!", "Por favor digite o CPF para realizar a pesquisa")
    
    else:
        comando = f"SELECT * FROM aluno WHERE cpf = {cpf}"
        cursor.execute(comando)
        tabela = cursor.fetchall() 
        tv.delete(*tv.get_children())
        for (id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento) in tabela:
            tv.insert("","end", values=(id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento))

#mostrar dados na tabela
def sincronizar ():
    comando = 'SELECT * FROM aluno'
    cursor.execute(comando)
    tabela = cursor.fetchall()    

    for (id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento) in tabela:
        tv.insert("","end", values=(id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento))

#configuração
root = Tk()
root.geometry("1000x680+200+50");
root.title("GERENCIAMENTO DE ALUNOS");
#FRAME TELA PRINCIPAL
tela_principal = Frame(root, bg="#57ded0")
tela_principal.place(x=0,y=0,width=1000,height=680)

#TITULO
texto = Label(tela_principal, text="GERENCIAMENTO DE ALUNOS", font=("Arial Black",25),bg="#57ded0", fg="black")
texto.place(x=230, y=20)


#botão adicionar
im_ml_botao = Image.open('adicionar.png')
im_ml_botao  = im_ml_botao .resize((60,50), Image.ANTIALIAS)
im_ml_botao  = ImageTk.PhotoImage(im_ml_botao )

l_ml_botao= Button(tela_principal, image=im_ml_botao, compound=LEFT, anchor='nw', 
bg="#57ded0",bd=0,activebackground="#3b3b3b", command=insert)
l_ml_botao.place(x=30,y=349)

adicionar = Label(tela_principal, text="ADICIONAR", font =('Arial Black', 9), bg="#57ded0",fg="black")
adicionar.place(x=20,y=400)


#botão deletar
im_ml_botao1 = Image.open('apagar.png')
im_ml_botao1  = im_ml_botao1.resize((60,50), Image.ANTIALIAS)
im_ml_botao1  = ImageTk.PhotoImage(im_ml_botao1)

l_ml_botao1= Button(tela_principal, image=im_ml_botao1, compound=LEFT, anchor='nw', 
bg="#57ded0",bd=0,activebackground="#3b3b3b", command=delete)
l_ml_botao1.place(x=205,y=349)

deletar = Label(tela_principal, text="DELETAR", font =('Arial Black', 9), bg="#57ded0",fg="black")
deletar.place(x=200,y=400)

#botão editar
im_ml_botao2 = Image.open('editar.png')
im_ml_botao2  = im_ml_botao2.resize((60,50), Image.ANTIALIAS)
im_ml_botao2  = ImageTk.PhotoImage(im_ml_botao2 )

l_ml_botao2= Button(tela_principal, image=im_ml_botao2, compound=LEFT, anchor='nw', 
bg="#57ded0",bd=0,activebackground="#3b3b3b", command=update)
l_ml_botao2.place(x=370,y=349)

editar = Label(tela_principal, text="EDITAR", font =('Arial Black', 9), bg="#57ded0",fg="black")
editar.place(x=370,y=400)

#botão sincronizar
im_ml_botao4 = Image.open('sincronizar.png')
im_ml_botao4  = im_ml_botao4.resize((60,50), Image.ANTIALIAS)
im_ml_botao4  = ImageTk.PhotoImage(im_ml_botao4 )

l_ml_botao4= Button(tela_principal, image=im_ml_botao4, compound=LEFT, anchor='nw', 
bg="#57ded0",bd=0,activebackground="#3b3b3b", command=sincronizar)
l_ml_botao4.place(x=700,y=349)

sincronizar = Label(tela_principal, text="SINCRONIZAR", font =('Arial Black', 9), bg="#57ded0",fg="black")
sincronizar.place(x=685,y=400)


#botão buscar
im_ml_botao3 = Image.open('buscar.png')
im_ml_botao3  = im_ml_botao3.resize((60,50), Image.ANTIALIAS)
im_ml_botao3  = ImageTk.PhotoImage(im_ml_botao3 )

l_ml_botao3= Button(tela_principal, image=im_ml_botao3, compound=LEFT, anchor='nw', 
bg="#57ded0",bd=0,activebackground="#3b3b3b", command=buscar)
l_ml_botao3.place(x=550,y=349)

buscar = Label(tela_principal, text="BUSCAR", font =('Arial Black', 9), bg="#57ded0",fg="black")
buscar.place(x=550,y=400)


#campos para inserir
#--------------------------
name = Label(tela_principal, text="NOME", font =('Arial Black', 12), bg="#57ded0",fg="black")
name.place(x=20,y=100)
#--------------------------
endereço = Label(tela_principal, text="ENDEREÇO", font =('Arial Black', 12), bg="#57ded0",fg="black")
endereço.place(x=20,y=140)
#--------------------------
responsavel = Label(tela_principal, text="RESPONSAVEL", font =('Arial Black', 12), bg="#57ded0",fg="black")
responsavel.place(x=20,y=180)
#--------------------------
matricula = Label(tela_principal, text="MATRICULA", font =('Arial Black', 12), bg="#57ded0",fg="black")
matricula.place(x=20,y=220)
#--------------------------
sexo = Label(tela_principal, text="SEXO", font =('Arial Black', 12), bg="#57ded0",fg="black")
sexo.place(x=20,y=260)
#--------------------------
telefone = Label(tela_principal, text="TELEFONE", font =('Arial Black', 12), bg="#57ded0",fg="black")
telefone.place(x=20,y=300)
#--------------------------
cpf = Label(tela_principal, text="CPF", font =('Arial Black', 12), bg="#57ded0",fg="black")
cpf.place(x=315,y=220)
#--------------------------
rg = Label(tela_principal, text="RG", font =('Arial Black', 12), bg="#57ded0",fg="black")
rg.place(x=315,y=260);
#--------------------------
datanascimento = Label(tela_principal, text="DATA DE NASCIMENTO", font =('Arial Black', 12), bg="#57ded0",fg="black")
datanascimento.place(x=315,y=300)
#--------------------------


#campos
#--------------------------
e_name = Entry(tela_principal, width=50,font=1)
e_name.place(x=160, y=100)
#--------------------------
e_endereço = Entry(tela_principal, width=50,font=1)
e_endereço.place(x=160, y=140)
#--------------------------
e_responsavel = Entry(tela_principal, width=50,font=1)
e_responsavel.place(x=160, y=180)
#--------------------------
e_matricula = Entry(tela_principal, width=13,font=1)
e_matricula.place(x=160, y=220)
#--------------------------
e_sexo = Entry(tela_principal, width=13,font=1)
e_sexo.place(x=160, y=260)
#--------------------------
e_telefone = Entry(tela_principal, width=13,font=1)
e_telefone.place(x=160, y=300)
#--------------------------
e_cpf = Entry(tela_principal, width=15,font=1)
e_cpf.place(x=475, y=220)
#--------------------------
e_rg = Entry(tela_principal, width=15, font=1)
e_rg.place(x=475, y=260)
#--------------------------
e_datanascimento = Entry(tela_principal, width=10,font=1)
e_datanascimento.place(x=523, y=300)

#Função de pegar da tv e colocar nas caixas de texto
def GetValue(event):
    e_name.delete(0, END)
    e_cpf.delete(0, END)
    e_rg.delete(0, END)
    e_matricula.delete(0, END)
    e_sexo.delete(0, END)
    e_telefone.delete(0, END)
    e_endereço.delete(0, END)
    e_responsavel.delete(0, END)
    e_datanascimento.delete(0, END)
    
    

    row_id = tv.selection()[0]
    select = tv.set(row_id)
    
    e_name.insert(0,select['nome'])
    e_cpf.insert(0,select['cpf'])
    e_rg.insert(0,select['rg'])
    e_matricula.insert(0,select['matricula'])
    e_sexo.insert(0,select['sexo'])
    e_telefone.insert(0,select['telefone'])
    e_endereço.insert(0,select['endereço'])
    e_responsavel.insert(0,select['responsavel'])
    e_datanascimento.insert(0,select['dataNascimento'])
    
    



#tabela
tv=ttk.Treeview(tela_principal,columns=("id","nome","cpf","rg","matricula","sexo",
                                        "telefone","endereço","responsavel","dataNascimento"), show='headings')
tv.place(x=20, y=430)
#coluna
tv.column('id',minwidth=0,width=30)
tv.column('nome',minwidth=0,width=150)
tv.column('cpf',minwidth=0,width=80)
tv.column('rg',minwidth=0,width=60)
tv.column('matricula',minwidth=0,width=77)
tv.column('sexo',minwidth=0,width=65)
tv.column('telefone',minwidth=0,width=100)
tv.column('endereço',minwidth=0,width=150)
tv.column('responsavel',minwidth=0,width=100)
tv.column('dataNascimento',minwidth=0,width=150)

#cabeçalho
tv.heading('id',text='ID')
tv.heading('nome',text='NOME')
tv.heading('cpf',text='CPF')
tv.heading('rg',text='RG')
tv.heading('matricula',text='MATRICULA')
tv.heading('sexo',text='SEXO')
tv.heading('telefone',text='TELEFONE')
tv.heading('endereço',text='ENDEREÇO')
tv.heading('responsavel',text='RESPONSAVEL')
tv.heading('dataNascimento',text='DATA DE NASCIMENTO')

#linha
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=20,y=452,  width=960)



#mostrar dados na tabela
def sincronizar():
    comando = 'SELECT * FROM aluno'
    cursor.execute(comando)
    tabela = cursor.fetchall()    
    for (id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento) in tabela:
        tv.insert("","end", values=(id,nome,cpf,rg,matricula,sexo,telefone,endereço,responsavel,datanascimento))
    



tv.bind('<Double-Button-1>',GetValue)
root.mainloop()
cursor.close()
conexao.close()