import time
from sistema_aluno import Cod 
from sistema_aluno import Aluno
from quiz import Quiz
from quiz import Tarefa_p
from quiz import Apostila


  
curso = Aluno()
tarefa = '0'
email_dell = True
while True:

    if tarefa == '0':
        tarefa= input('\n1 - Cadastrar\n2 - Logar\n3 - sair \nEscolha uma opção:   ')

    else:
        break
    
    if tarefa == '1' :
        nome   = input('seu nome:  ')
        while True:
            try:    
                idade  = int(input('sua idade:  '))
                break
            except:
                print('Idade inválida. Tente novamente.')
        email_n  = input('seu email:  ') 
        senha_n  = input('Sua senha (inclua número e caractere especial):  ')
        curso.cadastro(nome,idade,email_n,senha_n) # Chama função de cadastro da classe Aluno \ funcao no arquivo sistema_aluno.py linha 21
        tarefa = '2'
    if tarefa=='2':
        while True:
            aluno_email = input('qual e seu email? ')
            senha_av = input('insira sua senha:  ')
            aluno_email_logar = curso.logar(senha_av,aluno_email)# Valida login com os dados json / funcao no arquivo sistema_aluno.py linha 72
            if aluno_email_logar:
                break    
    
        if aluno_email==aluno_email_logar:
            inicio = time.perf_counter()
            while True :
               
                if email_dell == 'email_dell':
                    break # Sai do sistema se o aluno tiver deletado a conta
                
                
                tarefa_l= input('\n1 - Apostila\n2 - Prova\n3 - Atividade\n4 - Alterar dados de cadastro\n5 - Sair\nEscolha uma opção: ')

                if tarefa_l == '1':
                    apos = Apostila()
                    while True: 
                        txt_ex = float(input('\nSobre o que deseja saber:\n1 - String\n2 - Input\n3 - If/Else\n4 - For\n5 - Função\n6 - Sair\nEscolha uma opção: '))
                        if txt_ex <= 5 :
                            print(apos.txt_apos(txt_ex))#funçao para Exibir o conteúdo do tema escolhido / funcao no arquivo quiz.py linha 235
                        elif txt_ex== 6 :
                            break
                        else:
                            print('comando não encontrado')
        
                
                        
                elif tarefa_l == '2':
                
                    acertos = 0
                    quiz = Quiz()
                    perguntas_selecionadas = quiz.selecionar_perguntas()# Seleciona perguntas aleatórias / funcao no arquivo quiz.py linha  194





                    for i, (pergunta, resposta_correta) in enumerate(perguntas_selecionadas, 1):
                        print(f'Pergunta {i}: {pergunta}')
                        resposta = input('Qual é a sua resposta: ').lower().strip()

                        if resposta == resposta_correta:
                            print('Certa resposta!\n')
                            acertos += 1
                        else:
                            print(f'A resposta certa é {resposta_correta}.\n')

                    curso.registrar_nota(aluno_email,acertos)# Salva nota do aluno / funcao no arquivo sistema_aluno.py linha 109
                    acertos = 0
                elif tarefa_l == '3':

                    print("Digite seu código linha por linha.")
                    print("Comandos especiais disponíveis:")
                    print("  [executar] → Executa o código digitado.")
                    print("  [remover]  → Remove a última linha de código.")
                    print("  [limpar]   → Limpa todo o código digitado.")
                    print("  [sair]     → Sai sem executar o código.\n")


                    a = Tarefa_p()
                    texper = a.ati()# Gera texto da atividade  /funcao no arquivo quiz.py linha 207
                    Cod(texper)# Executa o  codigo / funcao no arquivo sistema_aluno.py linha 193




                elif tarefa_l == '4' : 
                    while True:
                        operacao = input('\nO que você deseja alterar?\n1 - Nome\n2 - Idade\n3 - E-mail\n4 - Senha\n5 - deletar conta\n6 - Sair\nEscolha uma opção: ')
                        if operacao <='5':
                            email_dell = curso.alterar(operacao,aluno_email_logar)# funcao para alterar dados / funcao no arquivo sistema_aluno.py linha 126
                            if email_dell == 'email_dell':
                                break# Sai se a conta foi deletada
                        elif operacao == '6':
                            break
                            
                        
                elif tarefa_l == '5':
                    fim = time.perf_counter()
                    temp_acesso = (fim - inicio) / 60
                    temp_acesso =round(temp_acesso, 2)

                    curso.registrar_tempo(aluno_email, temp_acesso)# Salva tempo de uso \ funcao no arquivo sistema_aluno.py linha 101
                    tarefa = '0'
                    break
                else:
                    print('comando não encontrado')
        
                