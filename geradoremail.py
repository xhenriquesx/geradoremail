import csv
import string
#import unidecode
#import unicodedata

dados = []
with open('alunos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        dados.append(linha)

matricula = int(input("Digite sua matrícula: "))

for i in dados:
    while (i['matricula'] != str(matricula)) and (i['status'] != "ativo"):
        print("Matrícula incorreta ou status inativo. Tente novamente!")
        matricula = int(input("Digite sua matrícula novamente: "))
    else:
        nomec = i['nome']
        break
mail = "id.uff.br"
opcao = 0
nome = nomec.split()[0]

print(nome +', por favor escolha uma das opções abaixo para o seu UFFMail:' + '\n')

email_opcoes = {
        '1':f" - {nomec.lower().split()[0]}{nomec.lower().split()[1]}@{mail}",
        '2':f" - {nomec.lower().split()[0]}.{nomec.lower().split()[1]}@{mail}",
        '3':f" - {nome.lower()}_{nomec.lower().split()[2]}@{mail}",
        '4':f" - {nome.lower().split()[0]}{nomec.lower().split()[1]}@{mail}",
        '5':f" - {nome.lower()}{nomec.split()[1][0].lower()}{nomec.split()[2][0].lower()}@{mail}"
    } 
for x,v in email_opcoes.items():
    print(x,v)
opcao = input("\n")#faz leitura da escolha
for c,v in email_opcoes.items():
    if c == opcao:
        print("\nA criação de seu e-mail", v.replace(" - ",""), "será feita nos próximos minutos. Um SMS foi enviado para 99999-9971 com a sua senha de acesso.")