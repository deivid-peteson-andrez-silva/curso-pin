import time
import json
import os

class aluno:
    def __init__(self):
        numaluno=0
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
        nome   = input('sua nome  ')
        idade  = input('sua idade  ')
        email  = input('sua email  ') 
        senha  = input('sua senha  ')

        alunos= {'id':numaluno,
                "nome":nome,
                'idade':idade,
                'email':email,
                'senha':senha
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
            with open('arquivos/dados.json', 'w') as arquivo:
                json.dump(nova_lista, arquivo, indent=4)
            print(f"Aluno com ID {id_deletar} foi deletado com sucesso.")



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

