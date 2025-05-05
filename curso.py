import time
from classs import Cod 
from classs import Aluno
from quiz import Quiz


quant_per = 10    
acertos = 0
curso = Aluno()
tarefa= input('1 cadastrar\n2 logar\n')

if tarefa == '1' :
    nome   = input('seu nome  ')
    idade  = input('sua idade  ')
    email_n  = input('seu email  ') 
    senha_n  = input('sua senha incluir numero e caracter especial como @#$%&  ')
    curso.cadastro(nome,idade,email_n,senha_n)
    
elif tarefa=='2':
    while True:
        aluno_email = input('qual e sel email ')
        senha_av = input('insira sua senha')
        aluno_email_logar = curso.logar(senha_av,aluno_email)
        if aluno_email_logar:
            break    
    
    if aluno_email==aluno_email_logar:
        inicio = time.perf_counter()
        while True :
            tarefa_l= float(input('1 prova\n2 questoes\n3 alterar dados de cadastro\n4 sair\n'))
            if tarefa_l == 1:
            
                quiz = Quiz()
                perguntas_selecionadas = quiz.selecionar_perguntas()

                
                # Lógica para exibir as perguntas

                for i, (pergunta, resposta_correta) in enumerate(perguntas_selecionadas, 1):
                    print(f'Pergunta {i}: {pergunta}')
                    resposta = input('Qual é a sua resposta: ').lower().strip()

                    if resposta == resposta_correta:
                        print('Certa resposta!\n')
                        acertos += 1
                    else:
                        print(f'A resposta certa é {resposta_correta}.\n')

                curso.registrar_nota(aluno_email,acertos)
                acertos = 0
            elif tarefa_l == 2:
                Cod('use a função print pra exibir hola mundo\n')
                

            
            
            elif tarefa_l == 3 : 
                while True:
                    operacao = float(input('oque voce deseja alterar\n1 nome\n2 idade\n3 email\n4 senha\n5 sair\n'))
                    if operacao <=4:
                        curso.alterar(operacao,aluno_email_logar)
                    elif operacao==5:
                        break
            
            elif tarefa_l==4:
                fim = time.perf_counter()
                temp_acesso = (fim - inicio) / 60
                temp_acesso =round(temp_acesso, 2)
                
                curso.registrar_tempo(aluno_email, temp_acesso)
                break