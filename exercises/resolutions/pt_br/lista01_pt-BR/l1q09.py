# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

def calcular_volume_caixa_retangular(comprimento, largura, altura):
	return comprimento * largura * altura

if __name__ == "__main__":
	#testando a funcao
	print(calcular_volume_caixa_retangular(10, 2, 4))
