'''
import time

codigo=[]

print("use a função print pra exibir hola mundo\n")
while True:
    try:
        tex=input()
        if tex== "p":
            print(codigo)
            codigo_str = "\n".join(codigo)
            exec(codigo_str)
            break
        else:
            codigo.append(tex)
    except Exception as e:
        print(f'codigo errado {e}\n ')
        time.sleep(2)            

        """"[]
#ai depois questoes 

print('pergunta do curso exemplo ?')

print('a resposta \nb resposta \nc resposta \nd resposta \ne resposta \n\n')

resposta = input('qual e a resposta certa').lower().strip()

#teste se a resposta ta certa
# if resposta == respsta_certa 
if resposta != 'd' :
     print('a resposta certa e D ---------------#colocar o modivo#')
else:
    print('certa resposta')
    acertos+=1
    
#media delas para nota
media= acertos/quant_per*10


print("Digite uma linha de código Python aprendido no curso (ex: print('Olá Mundo!')): ")
#por enquanto so aceita uma linha


# Executar o código fornecido pelo usuário
while True:
    try:
        
        codigo_usuario = input()
        if  codigo_usuario == 'f5':
            break
            print('a saida do codigo colocado e ')
        else:
            exec(codigo_usuario)
    except Exception as e:
        print('codigo errado ')
"""


nome_busca = input("Digite o nome do aluno que quer procurar: ").strip().lower()

for aluno in a.lista_aluno:
    if aluno["nome"] == nome_busca:
        print(f"Aluno encontrado! ID: {aluno['id']}, Idade: {aluno['idade']} anos")
        '''
from classs import aluno
a = aluno()
'''
while True:

    aluno_email = input('qual e sel email')
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
                operacao = input('oque voce deseja alterar\n1 nome\n2 idade\n3 email\n4 senha\n')
                if operacao == '1':
                    novo_nome == input('Digite o novo nome  ')
                    aluno_encontrado['nome'] = novo_nome
                elif operacao == '2':
                    nova_idade == inpot('Digite a nova idade  ')
                    aluno_encontrado['idade'] == nova_idade
                elif operacao == '3':
                    novo_email['Digite o novo email']
                    if '@' in novo_email and '.' in novo_email :
                        aluno_encontrado['email'] == novo_email
                elif operacao == '4':
                    while True:
                        nova_senha  = input('sua senha incluir numero e caracter especial  ')
                        tem_especial = '!@#$%&*_+*/-+[]{^}~ç:.,<>\?;|'
                        tem_especial = any(char in especiais for char in senha)
                        tem_numero = any(char.isdigit() for char in nova_senha)
                        if  iss and tem_numero: 
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
'''
