# Desafio 1 - Gerador de Email

O desafio proposto envolve a implementação do processo de criação de contas de e-mail para os alunos de uma universidade. O objetivo é ler um arquivo CSV que contenha os dados dos alunos e, com base em seus nomes e status, apresentar um conjunto de opções de e-mail para que possam selecionar. Após a escolha, o aluno receberá uma mensagem confirmando que sua conta será criada em breve, juntamente com a informação de que receberá uma senha inicial através de SMS para acessá-la.

Regras
Apenas alunos ativos podem criar um UFFMail
As opções de UFFMail devem ser geradas de acordo com o nome do aluno
Um aluno só pode ter um UFFMail
Utilizar Orientação a Objetos para resolver o problema
Livre escolha para a linguagem a ser utilizada

Dicas
Quais classes são necessárias para resolver este problema?
Desenvolva sempre buscando o menor acoplamento possível entre as classes
Seu software deve estar preparado para eventuais mudanças
A geração de opções para o usuário fica a seu critério
Não é necessário consumir nenhuma API para resolver o problema, basta retornar as mensagens e fingir que o e-mail foi criado, faça o mesmo para o SMS
Você pode atualizar o csv preenchendo a coluna de uffmail quando um e-mail for criado, mas isso é opcional

Exemplo
Digite sua matrícula:
105457

Laura, por favor escolha uma das opções abaixo para o seu UFFMail
1 - laura_azevedo@universidade.br
2 - lauraac@universidade.br
3 - lauracunha@universidade.br
4 - lcunha@universidade.br
5 - lazevedocunha@universidade.br

1

A criação de seu e-mail (laura_azevedo@universidade.br) será feita nos próximos minutos.
Um SMS foi enviado para 99999-9971 com a sua senha de acesso.
