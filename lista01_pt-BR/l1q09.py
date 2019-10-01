# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Elaborar um programa que calcule e apresente o volume de uma caixa retangular.
Use a fórmula: VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
'''

def calcular_volume_caixa_retangular(comprimento, largura, altura):
	return comprimento * largura * altura

if __name__ == "__main__":
	#testando a funcao
	print(calcular_volume_caixa_retangular(10, 2, 4))