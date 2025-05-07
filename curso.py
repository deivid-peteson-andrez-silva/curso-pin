import time
from classes import Cod 
from classes import Aluno
from quiz import Quiz
from quiz import Tarefa_p
from quiz import Apostila


quant_per = 10    
acertos = 0
curso = Aluno()
tarefa= input('\n1 cadastrar\n2 logar\n')

if tarefa == '1' :
    nome   = input('seu nome  ')
    idade  = input('sua idade  ')
    email_n  = input('seu email  ') 
    senha_n  = input('sua senha incluir numero e caracter especial como @#$%&  ')
    curso.cadastro(nome,idade,email_n,senha_n)
    
elif tarefa=='2':
    while True:
        aluno_email = input('qual e sel email ')
        senha_av = input('insira sua senha ')
        aluno_email_logar = curso.logar(senha_av,aluno_email)
        if aluno_email_logar:
            break    
    
    if aluno_email==aluno_email_logar:
        inicio = time.perf_counter()
        while True :
            tarefa_l= float(input('\n1 apostila\n2 prova\n3 atividade\n4 alterar dados de cadastro\n5 sair\n'))
            
            if tarefa_l == 1:
                apos = Apostila()
                while True: 
                    txt_ex = float(input('\nsobre o que deseja saber\n1 string\n2 input\n3 if else\n4 for\n5 função\n6 sair\n'))
                    if txt_ex <= 5 :
                        print(apos.txt_apos(txt_ex))
                    elif txt_ex== 6 :
                        break
                
            
            elif tarefa_l == 2:
            
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
            elif tarefa_l == 3:
                
                print("Digite seu código linha por linha.")
                print("Comandos especiais disponíveis:")
                print("  [executar] → Executa o código digitado.")
                print("  [remover]  → Remove a última linha de código.")
                print("  [limpar]   → Limpa todo o código digitado.")
                print("  [sair]     → Sai sem executar o código.\n")

                
                a = Tarefa_p()
                texper = a.ati()
                Cod(texper)
                

            
            
            elif tarefa_l == 4 : 
                while True:
                    operacao = float(input('\noque voce deseja alterar\n1 nome\n2 idade\n3 email\n4 senha\n5 sair\n'))
                    if operacao <=4:
                        curso.alterar(operacao,aluno_email_logar)
                    elif operacao==5:
                        break
            
            elif tarefa_l==5:
                fim = time.perf_counter()
                temp_acesso = (fim - inicio) / 60
                temp_acesso =round(temp_acesso, 2)
                
                curso.registrar_tempo(aluno_email, temp_acesso)
                break