# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo.
OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.
'''

a = int(input('Primeiro lado do triângulo: '))
b = int(input('Segundo lado do triângulo: '))
c = int(input('Terceiro lado do triângulo: '))

if a>=b+c or b>=c+a or c>=a+b:
	print('Não formam um triângulo')
else:
	print('Formam um triângulo')