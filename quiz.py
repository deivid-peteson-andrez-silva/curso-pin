
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
b ) Quando o programa fecha.
c ) Quando uma variável for criada.
d ) Quando a condição especificada for verdadeira.
e ) Quando o usuário pressiona Enter.
''', "d"),
                ('''Qual operador é usado para comparar igualdade em um if?
a ) +
b ) =
c ) !=
d ) <>
e ) ==
''', "e"),
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
a ) Para repetir blocos de código em uma sequência.
b ) Para declarar variáveis.
c ) Para comparar duas condições.
d ) Para receber dados do usuário.
e ) Para criar novas funções.
''', "a"),
                ('''Qual função é mais usada junto com for para criar uma sequência de números?
a ) input()
b ) str()
c ) range()
d ) print()
e ) int()
''', "c"),
                ('''O que o comando for x in range(5): faz?
a ) Cria uma variável com valor 5.
b ) Cria uma função chamada x.
c ) Exibe 5 mensagens de erro.
d ) Lê 5 entradas do usuário.
e ) Repete o bloco de código 5 vezes.
''', "e"),
                ('''O que acontece se usamos break dentro de um for?
a ) O loop é ignorado.
b ) Nada acontece.
c ) O loop é reiniciado.
d ) Um erro é gerado.
e ) O loop é interrompido imediatamente.
''', "e"),
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
c ) 45.6
d ) "Olá Mundo"
e ) None
''', "d"),
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
c ) Para criar listas.
d ) Para agrupar códigos que podem ser reutilizados.
e ) Para definir variáveis automaticamente.
''', "d"),
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
            perguntas_selecionadas.extend(random.sample(perguntas,2))
        
        random.shuffle(perguntas_selecionadas) 
        return perguntas_selecionadas
    
    

class Tarefa_p :
        
    def ati(self):
        atividade_random = [
            'Como você usaria um if na prática para verificar se uma pessoa pode entrar em um evento com idade mínima de 18 anos?',
            'Como você usaria o if para decidir se um número é positivo ou negativo?',
            'Escreva um exemplo usando if para comparar dois números e dizer qual é maior.',
            'Dê um exemplo de uso de if e else para verificar se um aluno foi aprovado com nota mínima 7',
            'Descreva como você usaria um if para checar se uma senha digitada está correta.',
            'Como você usaria um for para imprimir os números de 1 a 10?',
            'Mostre como você usaria o range() com for para criar uma contagem regressiva de 10 até 1.',
            'Faça um exemplo de for para exibir cada letra da palavra "Python".',
            'Explique como você usaria o break para parar um loop quando um número específico for encontrado.',
            'Dê um exemplo de for para percorrer os itens de uma lista de compras.',
            'Escreva um exemplo de input() para pedir o nome do usuário.',
            'Como você converteria a entrada do input() para um número inteiro?',
            'Faça um exemplo que pede a idade do usuário usando input().',
            'Mostre como você pediria um número para o usuário e depois somaria 10 a esse número.',
            'Crie um exemplo onde o usuário digita um número e o programa calcula o dobro.',
            'Faça um exemplo declarando uma string chamada fruta com valor "maçã".',
            'Crie uma string que guarde o nome da sua cidade.',
            'juntar duas strings: nome e sobrenome.'
            ]
        
        atividade_es= random.choice(atividade_random)
        return atividade_es
      
      
class Apostila:
    def txt_apos(self,txt_ex):
        if txt_ex==1:
            ex_str =  '''
Em Python, str é o tipo usado para representar textos, ou seja, qualquer sequência de caracteres como
nomes, frases, letras ou até números escritos como texto. Você pode criar uma string colocando o conteúdo
entre aspas simples ou duplas, como "Olá" ou 'mundo'. Strings são imutáveis, o que significa que você
não pode mudar um caractere direto nela depois que foi criada, mas pode gerar uma nova string modificada
usando métodos como .upper() para deixar tudo em maiúsculo, .lower() para minúsculo, .replace()
para trocar partes do texto, ou .strip() para remover espaços extras do início e fim. Também é possível
acessar partes da string usando colchetes com um índice, como texto[0] para pegar o primeiro caractere.
Para juntar strings, usa-se o operador +, e para inserir valores dentro de um texto, é comum usar f-strings,
como em f"Olá, {nome}".
'''
            return ex_str
        elif txt_ex ==2:
            ex_input = '''
A função input() em Python serve para capturar o que o usuário digita durante a execução do programa.
Quando input() é chamado, o Python mostra uma mensagem (se você quiser) e espera o usuário digitar
alguma coisa e apertar Enter. O valor que o usuário digita sempre é retornado como uma string, mesmo que
ele digite um número. Por isso, se você quiser trabalhar com números, precisa converter esse valor usando
int() para inteiros ou float() para números com ponto. Essa função é muito usada para tornar
programas interativos, permitindo que o usuário forneça informações como nome, idade, respostas de um
quiz, entre outros. Além disso, você pode armazenar esse valor em uma variável para usá-lo depois no seu código.
            '''
            return ex_input
        elif txt_ex ==3:
            ex_elif = '''
Em Python, o if é uma estrutura condicional usada para tomar decisões no programa. Ele verifica se uma
condição é verdadeira e, se for, executa um bloco de código. Caso a condição seja falsa, o código dentro do
if é ignorado. Isso permite que o programa tenha comportamentos diferentes dependendo dos dados ou
da situação. É possível adicionar o else para executar um outro bloco quando a condição não for satisfeita,
ou ainda usar elif para testar outras possibilidades antes de chegar ao else. Essas estruturas tornam o
programa mais inteligente, permitindo reações diferentes com base nas escolhas do usuário, nos valores das
variáveis ou em qualquer outra verificação lógica que o programador deseje fazer.
            '''
            return ex_elif
        elif txt_ex == 4:
            ex_for = '''
Em Python, o for é usado para repetir um bloco de código várias vezes, percorrendo uma sequência de
valores, como uma lista, string ou intervalo de números. Cada vez que o laço roda, ele pega um valor da
sequência e executa o bloco com esse valor. Isso é muito útil quando você quer fazer algo várias vezes de
forma controlada, como mostrar todos os nomes de uma lista ou contar de 1 a 10. Uma das formas mais
comuns de usar o for é com a função range(), que gera uma sequência de números. Assim, o for se
torna uma maneira simples e clara de fazer repetições, evitando códigos repetidos e deixando o programa
mais organizado.
            '''
            return ex_for
        
        elif txt_ex == 5:
            ex_funcao = '''
Em Python, uma função é um bloco de código que você cria para executar uma tarefa específica. Ela serve
para organizar o programa, evitar repetição de código e tornar tudo mais fácil de entender e manter. Para
criar uma função, você usa a palavra-chave def, seguida do nome da função e, entre parênteses, os
parâmetros que ela pode receber. Dentro da função, você escreve o que ela deve fazer. Quando quiser usar
essa função, basta "chamar" ela pelo nome.

Por exemplo, você pode criar uma função chamada saudar() que imprime uma mensagem. Depois, sempre
que quiser dar essa saudação, você chama a função sem precisar reescrever o mesmo código.

Funções também podem receber valores (chamados de parâmetros) e devolver um resultado usando a
palavra return. Isso deixa o código mais poderoso e flexível, porque você pode fazer a mesma função
funcionar com dados diferentes.
            '''
            return ex_funcao