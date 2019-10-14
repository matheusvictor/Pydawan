# -*- coding: utf-8 -*- [Define a utilização de alguns
# caracteres especiais, como ~, ^, etc.]

'''
Escreva um programa em Python que armazene o valor 10 em uma
variável A e o valor 20 em uma variável B.
A seguir (utilizando apenas atribuições entre variáveis)
troque os seus conteúdos fazendo com que o valor que está
em A passe para B e vice-versa.
Ao final, escrever os valores que ficaram armazenados nas variáveis.
'''

# A recebendo 10
A = 10
# B recebendo 20
B = 20
# Usando auxiliar para receber o valor de A
auxiliar = A
# A recebendo o valor de B
A = B
# B recebendo o valor que estava em A
B = auxiliar
# Printando na tela os valores trocados de A e B
print('O valor atual de A: ', A)
print('O valor atual de B: ', B)
