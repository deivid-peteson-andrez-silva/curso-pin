import time
from classes import Cod 
from classes import Aluno
from quiz import Quiz
from quiz import Tarefa_p
from quiz import Apostila
import customtkinter
curso=Aluno()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")


def tela1():

    janela = customtkinter.CTk()
    janela.geometry('500x300')

    txt = customtkinter.CTkLabel(janela,text='o que deseja' ,)

    botao_cadastro = customtkinter.CTkButton(janela, text='fazer  cadastro', command=lambda:janela_cadastro(janela))
    botao_cadastro.pack(padx=10, pady=10 )
    botao_login = customtkinter.CTkButton(janela, text='fazer  login', command=lambda:janela_login(janela))
    botao_login.pack(padx=10, pady=10 )
    janela.mainloop()

#fun da tela 1 

def janela_cadastro(cadastro_f):
    cadastro_f.destroy()
    cadastro = customtkinter.CTk()
    cadastro.geometry('500x300')
    
    txt = customtkinter.CTkLabel(cadastro,text='insira seus dados')
    txt.pack(padx=10, pady=10 )
    nome_c  = customtkinter.CTkEntry(cadastro, placeholder_text= 'nome')
    nome_c.pack(padx=10, pady=10 )
    idade_c  = customtkinter.CTkEntry(cadastro, placeholder_text= 'idade')
    idade_c.pack(padx=10, pady=10 )
    email_c  = customtkinter.CTkEntry(cadastro, placeholder_text= 'email')
    email_c.pack(padx=10, pady=10 )
    senha_c  = customtkinter.CTkEntry(cadastro, placeholder_text= 'senha')
    senha_c.pack(padx=10, pady=10 )
    def cadastrar():
        nome = nome_c.get()
        idade = idade_c.get()
        email = email_c.get()
        senha = senha_c.get()
        curso.cadastro(nome,idade,email,senha)
        tela1()        
    botao_c = customtkinter.CTkButton(cadastro, text='cadastrar', command=cadastrar)
    botao_c.pack(padx=10, pady=10 )
    
   
    cadastro.mainloop()

def janela_login(tela1_f):
    tela1_f.destroy()
    login = customtkinter.CTk()
    login.geometry('500x300')

    txt = customtkinter.CTkLabel(login,text='insira seus dados')
    txt.pack(padx=10, pady=10 )

    aluno_email = customtkinter.CTkEntry(login, placeholder_text= 'seu email')
    aluno_email.pack(padx=10, pady=10 )


    senha_av  = customtkinter.CTkEntry(login, placeholder_text= 'seu senha')
    senha_av.pack(padx=10, pady=10 )

    def tarefa_tela():
        login.destroy()
        tarefa_tela = customtkinter.CTk()
        tarefa_tela.geometry('700x500')
        
        botao = customtkinter.CTkButton(tarefa_tela, text='atividade', command=lambda:atividade(tarefa_tela))
        botao.pack(padx=10, pady=10 )
        
        botao = customtkinter.CTkButton(tarefa_tela, text='apostila', command=lambda:apostila(tarefa_tela))
        botao.pack(padx=10, pady=10 )
               
        
        tarefa_tela.mainloop()
    
    def apostila(tarefa_f):
        tarefa_f.destroy()
        apostila = customtkinter.CTk()
        apostila.geometry('700x500')
        
        apos = Apostila()
        txt = customtkinter.CTkLabel(apostila,text='sobre o que deseja saber')
        txt.pack(padx=10, pady=10 )        
        botoes = [
            ("String", 1),
            ("Input", 2),
            ("If/Else", 3),
            ("For", 4),
            ("Função", 5),
        ]
        def apostila_mostrar(txt_ex):
            apostila.destroy()
            apostila_mostrar = customtkinter.CTk()
            apostila_mostrar.geometry('700x500')
        
            txt =    apos.txt_apos(txt_ex)
            txt = customtkinter.CTkLabel(apostila_mostrar,text=txt)
            txt.pack(padx=10, pady=10 )  

        
            apostila_mostrar.mainloop()

        for nome, id_tema in botoes:
            b = customtkinter.CTkButton(apostila, text=nome, command=lambda i=id_tema: apostila_mostrar(i))
            b.pack(padx=10, pady=10)

        
                    
        
        apostila.mainloop()
        

        

    
    
    
    def atividade(login):
        login.destroy()
        atividade = customtkinter.CTk()
        atividade.geometry('700x500')
        
        a = Tarefa_p()
        txt = customtkinter.CTkLabel(atividade,text=a.ati())
        txt.pack(padx=10, pady=10 )
        
        caixa = customtkinter.CTkTextbox(atividade, width=300, height=200)
        caixa.pack(padx=10, pady=10)
        
        def codar():
            texper = texper = caixa.get("0.0", "end")
            Cod(texper)
        botao = customtkinter.CTkButton(atividade, text='rodar', command=codar)
        botao.pack(padx=10, pady=10 )
        
        atividade.mainloop()
    def clik():
        email = aluno_email.get()
        senha = senha_av.get()
        aluno_email_logar = curso.logar(senha,email)
        if aluno_email_logar:
            tarefa_tela()
        
    botao = customtkinter.CTkButton(login, text='login', command=clik)
    botao.pack(padx=10, pady=10 )
    
        
        

   
   
    
    


    login.mainloop()

















tela1()