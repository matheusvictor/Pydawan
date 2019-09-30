# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Escreva um programa em Python que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
Ao final, escrever os valores que ficaram armazenados nas variáveis.
'''
A = 10
B = 20
print('Original A:', A)
print('Original B:', B)
A, B = B, A # swapping the values
print('After Swap A:', A)
print('After Swap B:', B)
