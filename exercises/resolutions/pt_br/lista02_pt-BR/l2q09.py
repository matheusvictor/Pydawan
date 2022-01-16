# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

a = int(input('Primeiro lado do triângulo: '))
b = int(input('Segundo lado do triângulo: '))
c = int(input('Terceiro lado do triângulo: '))

if a>=b+c or b>=c+a or c>=a+b:
	print('Não formam um triângulo')
else:
	print('Formam um triângulo')
