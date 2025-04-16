

#ME AVISA ANTES TE FAZER commit





#eu fiz uma classe pro cadastro de aluno, e o arquivo classs.py na pasta
#resumindo porcamente classe e tipo usar um print ou uma funçao qualquer, 
#so que eu que programei pra fazer os cadastros como o trabalho pede
 
from classs import aluno

#area de alteraçao
#por enquanto pra cadastrar e deletar aluno nao mexe no codigo mas cadastra uns alunos ai

a = aluno()
cadastro = input('que cadastrar um aluno s/n ').lower().strip()
if cadastro =='s':
    a.cadastro() 
dell = input('quer deletar um aluno usando o id s/n')
if dell == 's':
    a.deletar_aluno()
    
# vc pode mudar apartir da qui
print(a.lista_aluno)
#esse e o nome da variavel que ta os cadastros, e como se fosse lista_aluno[] que vc viu na aula 
# mas nao funciona sem o ( a. )
#    a.lista_aluno
#essa lista ta no arquivos/dados.json
''' 
e isso que tem no cadastro
lista_aluno = [{'id': 1, 'nome': 'deivid', 'idade': '20', 'email': 'deivid@gmail.com', 'senha': '123'},]
'''


# um exemplo de como usar
nome_busca = input("Digite o nome do aluno que quer procurar: ").strip().lower()

for aluno in a.lista_aluno:
    if aluno["nome"] == nome_busca:
        print(f"Aluno encontrado! ID: {aluno['id']}, Idade: {aluno['idade']} anos")
        
        
#caso vc queira algo que altere nao velifique pode codar e deixar comentado que eu tepois 
#ajeito e coloco na area de alteraçao