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
'''
from classs import aluno
alunoo =aluno()
alunoo.deletar_aluno()