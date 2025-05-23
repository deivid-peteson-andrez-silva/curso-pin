import time
import json
import os
import  hashlib
import bcrypt
import random

class Aluno:
    def __init__(self):
        if os.path.exists('arquivos/dados.json'):
            with open('arquivos/dados.json', 'r') as arquivo:
                try:
                    self.lista_aluno = json.load(arquivo)
                    if not isinstance(self.lista_aluno, list):
                        self.lista_aluno = []
                except json.JSONDecodeError:
                    self.lista_aluno = []
        else:
            self.lista_aluno = []
    
    def cadastro(self,nome,idade,email_n,senha_n):    
 
        if self.lista_aluno:
            ids_existentes = [aluno['id'] for aluno in self.lista_aluno]
            numaluno = max(ids_existentes) + 1
        else:
          numaluno = 1
        
        while True:
            if '@' in email_n and '.' in email_n :
                email = email_n
                break
            else:
                print('email inválido ')
                email_n  = input('seu email  ') 
       

        while True:
            especiais = r'!@#$%&*_+*/-+[]{^}~ç:.,<>\?;|'
            tem_especial = any(char in especiais for char in senha_n)
            tem_numero = any(char.isdigit() for char in senha_n)
            if  tem_especial and tem_numero: 
                senha=senha_n
                break
            else:
                print('senha inválida')
                senha_n  = input('Sua senha (inclua número e caractere especial como @, #, %, &):   ')

        acesso = int(0)    
        temp_acesso = int(0)
        nota =[]
        media_nota=0
        alunos= {'id':numaluno,
                "nome":nome,
                'idade':idade,
                'email':email,
                'senha':bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode(),
                'acesso':acesso,
                'temp_acesso':temp_acesso,
                'media_nota':media_nota,
                'nota':nota
                }
        self.lista_aluno.append(alunos)
        with open('arquivos/dados.json','w') as arquivo:
                json.dump(self.lista_aluno , arquivo,indent=4)
        with open('arquivos/dados.json','r') as arquivo:
            texto=arquivo.read()
            dados= json.loads(texto)
    
      

    def logar(self,senha_av,aluno_email):
        aluno_encontrado = None

        for aluno in self.lista_aluno :
            if aluno['email'] == aluno_email:
                aluno_encontrado = aluno
                break
                
        if not aluno_encontrado:

            print('Email não encontrado.')
            return None
    
        if bcrypt.checkpw(senha_av.encode(), aluno_encontrado['senha'].encode()):
            print('Login realizado ')

            aluno_encontrado['acesso'] +=1 
            with open('arquivos/dados.json', 'w') as arquivo:
                json.dump(self.lista_aluno, arquivo, indent=4)

            return aluno_email
 
        else:
            print('senha inválida')
            return None


    
    
    def registrar_tempo(self,email,tempo):
            for aluno in self.lista_aluno:
                if aluno['email'] == email:
                    aluno['temp_acesso']= round(aluno['temp_acesso'] + tempo, 2)
                    break
            with open('arquivos/dados.json', 'w') as arquivo:
                json.dump(self.lista_aluno, arquivo, indent=4)
    
    def registrar_nota(self,email,nota):
        for aluno in self.lista_aluno:
            if aluno['email'] == email:
                nova_nota= aluno['nota']
                nova_nota.append(nota)
                aluno['nota']=nova_nota

                media= nova_nota
                quan = len(nova_nota)
                soma = sum(nova_nota)
                media = soma/quan
                aluno['media_nota']= media
                break
        with open('arquivos/dados.json', 'w') as arquivo:
            json.dump(self.lista_aluno, arquivo, indent=4)

    
    def alterar(self,operacao,aluno_email_logar):
        
        aluno_email = aluno_email_logar
        for aluno in self.lista_aluno :
            if aluno['email'] == aluno_email:
                aluno_encontrado = aluno
                break
                    

        if operacao == '1':
            novo_nome = input('Digite o novo nome:  ')
            aluno_encontrado['nome'] = novo_nome
        elif operacao == '2':
            nova_idade = int(input('Digite a nova idade:  '))
            aluno_encontrado['idade'] = nova_idade
        elif operacao == '3':
            while True:    
                novo_email = input('Digite o novo email: ')
                if '@' in novo_email and '.' in novo_email :
                    aluno_encontrado['email'] = novo_email
                    break
                else:
                    print('email inválido')
        elif operacao == '4':
            while True:
                nova_senha  = input('Digite a nova senha (inclua número e caractere especial): ')
                especiais = r'!@#$%&*_+*/-+[]{^}~ç:.,<>\?;|'
                tem_especial = any(char in especiais for char in nova_senha)
                tem_numero = any(char.isdigit() for char in nova_senha)
                if  tem_especial and tem_numero: 
                    nova_senha = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()
                    aluno_encontrado['senha'] = nova_senha 
                    break
                else:
                    print('senha inválida')
        
        
        elif operacao == '5' :
            nova_lista = []
            for aluno in self.lista_aluno:
                if str(aluno.get('email')) != aluno_email_logar:
                    nova_lista.append(aluno)

            if len(nova_lista) == len(self.lista_aluno):
                print("Aluno não encontrado.")
            else:
                self.lista_aluno = nova_lista
                with open('arquivos/dados.json', 'w') as arquivo:
                    json.dump(nova_lista, arquivo, indent=4)

                print(f"Aluno com email {aluno_email_logar} foi deletado com sucesso.")
                email_dell = 'email_dell'
                return email_dell 

        
        
        else:
            print('comando não encontrado')
        
                
        with open('arquivos/dados.json', 'w') as arquivo:
            json.dump(self.lista_aluno, arquivo, indent=4)

        print('Informações atualizadas com sucesso.')                
  


class Cod:
    def __init__(self,texper):
        self.texper=texper
        print(f"{self.texper}\n")
        codigo=[]
        while True:
            try:
                tex=input('>>>')
                if tex== "executar":
                    print("\nCódigo final:")
                    print("\n".join(codigo))
                    print("\nExecutando...\n")
                    t = random.randint(0, 2) 
                    time.sleep(t)
                    exec("\n".join(codigo))
                    break
                elif tex == 'remover':
                    if codigo:
                        removido = codigo.pop()
                        print(f"Linha removida: {removido}")
                    else:
                        print("Nenhuma linha para remover.")
                elif tex == "limpar":
                    print("Código limpo.")
                    codigo.clear()
                elif tex == "sair":
                    print("Saindo sem executar.")
                    break
                else:
                    codigo.append(tex)
            except Exception as e:
                print(f'Código errado: {e}\n')
                time.sleep(2)
