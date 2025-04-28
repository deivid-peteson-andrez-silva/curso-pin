import time
from classs import cod 
from classs import aluno
quant_per = 1    
acertos = 0
curso = aluno()
curso.cadastro()
aluno_email = curso.logar()
if aluno_email:
    inicio = time.perf_counter()
    
    print('Para que serve a função print() na linguagem Python? ')

    print('''
        a ) Para receber dados do usuário durante a execução do programa.
        b ) Para exibir mensagens, valores de variáveis ou resultados no console.
        c ) Para realizar cálculos matemáticos complexos.
        d ) Para armazenar dados em arquivos no sistem 
        
        ''')

    resposta = input('qual e a resposta certa: ').lower().strip()

    if resposta != 'b' :
        print('a resposta certa e b a função print exibi mensagens na tela\n')
    else:
        print('certa resposta\n')
        acertos+=1
        
    media= acertos/quant_per*10


    cod('use a função print pra exibir hola mundo\n')
    fim = time.perf_counter()
    temp_acesso = (fim - inicio) / 60
    
    curso.registrar_tempo(aluno_email, temp_acesso)