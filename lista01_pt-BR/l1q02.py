# -*- coding: utf-8 -*- [Define a utilização de alguns
#  caracteres especiais, como ~, ^, etc.]

'''
Faça um programa em Python que leia três notas de um aluno, calcule
 e escreva a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.
Fórmula para o cálculo da média final é:
 mediaFinal = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10
'''

# Lendo notas do aluno
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

# Fazendo o cálculo da média final
media_final = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

# Printando a média final do aluno
print('Sua média final: ', media_final)
