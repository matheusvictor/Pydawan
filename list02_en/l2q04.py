# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais,
# como ~, ^, etc.]
# resolvidos problemas de pep8
'''
Ler o ano atual e o ano de nascimento de uma pessoa.
Escrever uma mensagem que diga se ela poderá ou não votar este ano
(não é necessário considerar o mês em que a pessoa nasceu).
A pessoa poderá votar se tiver 16 anos ou mais.
'''
nascimento = int(input("Ano de nascimento: "))
# variável para armazenar ano de nascimento
ano_atual = int(input("Ano atual: "))
# variável para armazenar ano atual
diferenca = (ano_atual - nascimento)
# variável para armazenar a diferença entre o ano atual e o ano de nascimento
# caso essa diferença seja ao menos 16 anos, poderá votar este ano
if (diferenca >= 16):
    print("Poderá votar este ano.")
else:
    print("Não poderá votar este ano.")
