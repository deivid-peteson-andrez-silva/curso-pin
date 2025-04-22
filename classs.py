import time
import json
import os

class aluno:
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
    
    def cadastro(self):    
 
        if self.lista_aluno:
            ids_existentes = [aluno['id'] for aluno in self.lista_aluno]
            numaluno = max(ids_existentes) + 1
        else:
          numaluno = 1
        nome   = input('seu nome  ')
        idade  = input('sua idade  ')
        
        while True:
            email_n  = input('seu email  ') 
            if '@' in email_n and '.' in email_n :
                email = email_n
                break
            else:
                print('email invalido ')
       

        while True:
            senha_n  = input('sua senha incluir numero e caracter especial como @#$%&  ')
            especiais = r'!@#$%&*_+*/-+[]{^}~ç:.,<>\?;|'
            tem_especial = any(char in especiais for char in senha_n)
            tem_numero = any(char.isdigit() for char in senha_n)
            if  tem_especial and tem_numero: 
                senha=senha_n
                break
            else:
                print('senha invalida')

        acesso = int(0)    
        temp_acesso = int(0)
        alunos= {'id':numaluno,
                "nome":nome,
                'idade':idade,
                'email':email,
                'senha':senha,
                'acesso':acesso,
                'temp_acesso':temp_acesso
                }
        self.lista_aluno.append(alunos)
        with open('arquivos/dados.json','w') as arquivo:
                json.dump(self.lista_aluno , arquivo,indent=4)
        with open('arquivos/dados.json','r') as arquivo:
            texto=arquivo.read()
            dados= json.loads(texto)
    
      
    def deletar_aluno(self):
        id_deletar = input("Digite o ID do aluno para deletar: ")
        nova_lista = []
        for aluno in self.lista_aluno:
            if str(aluno.get('id')) != id_deletar:
                nova_lista.append(aluno)

        if len(nova_lista) == len(self.lista_aluno):
            print("Aluno não encontrado.")
        else:
            self.lista_aluno = nova_lista
            with open('arquivos/dados.json', 'w') as arquivo:
                json.dump(nova_lista, arquivo, indent=4)

            print(f"Aluno com ID {id_deletar} foi deletado com sucesso.")

    def logar(self):
        aluno_email = input('qual e sel email ')
        aluno_encontrado = None
        for aluno in self.lista_aluno :
            if aluno['email'] == aluno_email:
                aluno_encontrado = aluno
                break
                
        if aluno_encontrado:
            while True:   
                senha_av = input('insira sua senha')
                if senha_av == aluno_encontrado['senha']:
                    print('Login realizado ')

                    aluno_encontrado['acesso'] +=1 
                    with open('arquivos/dados.json', 'w') as arquivo:
                        json.dump(self.lista_aluno, arquivo, indent=4)

                    return aluno_email
                    break
                else:
                    print('senha invalida')
       
        else:
            print('email nao encontrado.')
    
    
    def registrar_tempo(self,email,tempo):
            for aluno in self.lista_aluno:
                if aluno['email'] == email:
                    aluno['temp_acesso'] += tempo
                    break
            with open('arquivos/dados.json', 'w') as arquivo:
                json.dump(self.lista_aluno, arquivo, indent=4)

    
    
    
    def alterar(self):
                
        while True:

            aluno_email = input('qual e sel email ')
            aluno_encontrado = None
            for aluno in self.lista_aluno :
                if aluno['email'] == aluno_email:
                    aluno_encontrado = aluno
                    break
                    
            if aluno_encontrado:
                while True:   
                    senha_av = input('insira sua senha ')
                    if senha_av == aluno_encontrado['senha']:
                        print('Login realizado ')
                        operacao = input('oque voce deseja alterar\n1 nome\n2 idade\n3 email\n4 senha\n')
                        if operacao == '1':
                            novo_nome = input('Digite o novo nome  ')
                            aluno_encontrado['nome'] = novo_nome
                        elif operacao == '2':
                            nova_idade = input('Digite a nova idade  ')
                            aluno_encontrado['idade'] = nova_idade
                        elif operacao == '3':
                            while True:    
                                novo_email = input('Digite o novo email ')
                                if '@' in novo_email and '.' in novo_email :
                                    aluno_encontrado['email'] = novo_email
                                    break
                                else:
                                    print('email invalido')
                        elif operacao == '4':
                            while True:
                                nova_senha  = input('sua senha incluir numero e caracter especial  ')
                                especiais = r'!@#$%&*_+*/-+[]{^}~ç:.,<>\?;|'
                                tem_especial = any(char in especiais for char in nova_senha)
                                tem_numero = any(char.isdigit() for char in nova_senha)
                                if  tem_especial and tem_numero: 
                                    aluno_encontrado['senha'] = nova_senha 
                                    break
                                else:
                                    print('senha invalida')
                        
                        with open('arquivos/dados.json', 'w') as arquivo:
                            json.dump(self.lista_aluno, arquivo, indent=4)

                        print('Informações atualizadas com sucesso.')                
                        break
                    else:
                        print('senha invalida')
                break
            else:
                print('email nao encontrado.')


class cod:
    def __init__(self,texper):
        self.texper=texper
        print(f"{self.texper}\n")
        codigo=[]
        while True:
            try:
                tex=input().strip().lower()
                if tex== "p":
                    print(codigo)
                    codigo_rodar = "\n".join(codigo)
                    exec(codigo_rodar)
                    break
                elif tex == 'dele':
                    del codigo[-1]
                elif tex == "linpar":
                    codigo.clear()
                
                else:
                    codigo.append(tex)
            except Exception as e:
                print(f'codigo errado {e}\n ')
                time.sleep(2)            

