
import random
# Classe Quiz com perguntas de cada tema
class Quiz:
    def __init__(self):
        self.perguntas = {
            'if': [
                ('''Para que serve a estrutura if na linguagem Python?
a ) Para repetir um bloco de código diversas vezes.
b ) Para tomar decisões baseadas em condições.
c ) Para criar variáveis no programa.
d ) Para exibir mensagens na tela.
e ) Para realizar operações matemáticas.
''', "b"),
                ('''Quando o bloco if é executado em Python?
a ) Sempre que o programa inicia.
b ) Quando a condição especificada for verdadeira.
c ) Quando uma variável for criada.
d ) Quando o usuário pressiona Enter.
e ) Quando o programa fecha.
''', "b"),
                ('''Qual operador é usado para comparar igualdade em um if?
a ) +
b ) ==
c ) =
d ) !=
e ) <>
''', "b"),
                ('''Qual palavra é usada junto com if para oferecer uma alternativa?
a ) while
b ) for
c ) else
d ) elif
e ) input
''', "d"),
                ('''O que acontece se a condição do if for falsa?
a ) O código dentro do if é executado.
b ) O código dentro do if é ignorado.
c ) O programa fecha automaticamente.
d ) Um erro é gerado.
e ) A variável é redefinida.
''', "b")
            ],
            'for': [
                ('''Para que serve a estrutura for na linguagem Python?
a ) Para declarar variáveis.
b ) Para repetir blocos de código em uma sequência.
c ) Para comparar duas condições.
d ) Para receber dados do usuário.
e ) Para criar novas funções.
''', "b"),
                ('''Qual função é mais usada junto com for para criar uma sequência de números?
a ) input()
b ) range()
c ) str()
d ) print()
e ) int()
''', "b"),
                ('''O que o comando for x in range(5): faz?
a ) Cria uma variável com valor 5.
b ) Repete o bloco de código 5 vezes.
c ) Exibe 5 mensagens de erro.
d ) Lê 5 entradas do usuário.
e ) Cria uma função chamada x.
''', "b"),
                ('''O que acontece se usamos break dentro de um for?
a ) O loop é ignorado.
b ) O loop é interrompido imediatamente.
c ) O loop é reiniciado.
d ) Um erro é gerado.
e ) Nada acontece.
''', "b"),
                ('''Qual estrutura o for geralmente percorre?
a ) Strings, listas ou intervalos de números.
b ) Funções e classes.
c ) Números aleatórios.
d ) Apenas variáveis globais.
e ) Apenas operadores matemáticos.
''', "a")
            ],
            'input': [
                ('''Para que serve a função input() em Python?
a ) Para criar loops.
b ) Para receber dados do usuário.
c ) Para comparar variáveis.
d ) Para armazenar dados em arquivos.
e ) Para gerar números aleatórios.
''', "b"),
                ('''Qual tipo de dado é retornado pelo input()?
a ) int
b ) float
c ) str
d ) bool
e ) list
''', "c"),
                ('''O que acontece se usarmos input("Digite seu nome: ")? 
a ) O programa encerra.
b ) O programa exibe a mensagem e espera uma resposta.
c ) O programa gera um erro.
d ) O programa ignora o comando.
e ) O programa cria um loop automático.
''', "b"),
                ('''Como transformar o valor de um input() em número inteiro?
a ) int(input())
b ) float(input())
c ) str(input())
d ) bool(input())
e ) input(int())
''', "a"),
                ('''Se o usuário digitar "123" no input(), o que será armazenado?
a ) O número 123 como inteiro.
b ) A string "123".
c ) O valor booleano True.
d ) Um float 1.23.
e ) Um erro.
''', "b")
            ],
            'string': [
                ('''Como declaramos uma string em Python?
a ) Entre colchetes [].
b ) Entre aspas simples ou duplas.
c ) Entre parênteses ().
d ) Entre chaves {}.
e ) Sem nenhum símbolo especial.
''', "b"),
                ('''Qual exemplo representa uma string válida?
a ) 1234
b ) True
c ) "Olá Mundo"
d ) 45.6
e ) None
''', "c"),
                ('''O que acontece se esquecermos as aspas na declaração de uma string?
a ) O Python ignora.
b ) Um erro de sintaxe acontece.
c ) O valor é convertido para int.
d ) O programa continua.
e ) O Python transforma automaticamente em string.
''', "b"),
                ('''Como podemos combinar duas strings em Python?
a ) Usando o sinal de adição (+).
b ) Usando o sinal de subtração (-).
c ) Usando operadores lógicos.
d ) Usando a função input().
e ) Não é possível combinar strings.
''', "a"),
                ('''Qual função transforma um número em string?
a ) int()
b ) str()
c ) float()
d ) bool()
e ) input()
''', "b")
            ],
            'funcao': [
                ('''Para que serve uma função em Python?
a ) Para repetir loops.
b ) Para armazenar dados.
c ) Para agrupar códigos que podem ser reutilizados.
d ) Para criar listas.
e ) Para definir variáveis automaticamente.
''', "c"),
                ('''Como se declara uma função em Python?
a ) usando function
b ) usando def
c ) usando func
d ) usando create
e ) usando return
''', "b"),
                ('''O que a palavra-chave return faz dentro de uma função?
a ) Cria uma variável global.
b ) Interrompe o programa.
c ) Retorna um valor da função.
d ) Reinicia o loop.
e ) Fecha o programa.
''', "c"),
                ('''Qual exemplo mostra a definição correta de uma função?
a ) func minha_funcao():
b ) create minha_funcao:
c ) def minha_funcao():
d ) define minha_funcao():
e ) return minha_funcao()
''', "c"),
                ('''Como você chama uma função depois de criada?
a ) Apenas escrevendo seu nome seguido de parênteses.
b ) Com a palavra start.
c ) Com a palavra go.
d ) Declarando ela de novo.
e ) Criando uma variável nova.
''', "a")
            ]
        }

    def selecionar_perguntas(self):
        perguntas_selecionadas = []
        # Seleciona 2 perguntas aleatórias de cada tema
        for tema, perguntas in self.perguntas.items():
            perguntas_selecionadas.extend(random.sample(perguntas, 2))
        
        random.shuffle(perguntas_selecionadas)  # Embaralha as perguntas
        return perguntas_selecionadas