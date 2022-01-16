# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

def calcular_quadrado_soma_tres_numeros(A, B, C):
	return (A + B + C) ** 2

if __name__ == "__main__":
	a = float(input("Digite o primeiro numero: "))
	b = float(input("Digite o segundo numero: "))
	c = float(input("Digite o terceiro numero: "))
	print(calcular_quadrado_soma_tres_numeros(a, b, c))
