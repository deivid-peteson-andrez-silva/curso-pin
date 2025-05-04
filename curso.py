import time
from classs import cod 
from classs import aluno
from quiz import Quiz
quant_per = 10    
acertos = 0
curso = aluno()
aluno_email = curso.logar()
if aluno_email:
    inicio = time.perf_counter()
    quiz = Quiz()
    perguntas_selecionadas = quiz.selecionar_perguntas()

    # Lógica para exibir as perguntas
    inicio = time.perf_counter()

    for i, (pergunta, resposta_correta) in enumerate(perguntas_selecionadas, 1):
        print(f'Pergunta {i}: {pergunta}')
        resposta = input('Qual é a sua resposta: ').lower().strip()

        if resposta == resposta_correta:
            print('Certa resposta!\n')
            acertos += 1
        else:
            print(f'A resposta certa é {resposta_correta}.\n')


    cod('use a função print pra exibir hola mundo\n')
    
    curso.registrar_nota(aluno_email,acertos)
    fim = time.perf_counter()
    temp_acesso = (fim - inicio) / 60
    temp_acesso =round(temp_acesso, 2)
    
    curso.registrar_tempo(aluno_email, temp_acesso)
    curso.registrar_nota(aluno_email, acertos)