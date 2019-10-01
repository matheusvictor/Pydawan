# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Elabore um algoritmo que efetue a leitura de três valores (A, B e C) e apresente como resultado final a soma dos quadrados dos três valores lidos.
'''

def calcular_soma_do_quadrado_de_tres_valores(A, B, C):
	return (A**2 + B**2 + C**2)

if __name__ == "__main__":
	a = float(input("Digite o primeiro numero: "))
	b = float(input("Digite o segundo numero: "))
	c = float(input("Digite o terceiro numero: "))
	print(calcular_soma_do_quadrado_de_tres_valores(a, b, c))