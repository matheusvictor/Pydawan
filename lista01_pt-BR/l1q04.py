# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Desenvolva um algoritmo capaz de ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

def converter_celsius_para_fahrenheit(C):
	return (9 * C + 160) / 5

if __name__ == "__main__":
	celsius = float(input("Digite a temperatura em graus celsius: "))
	print("Grau em Fahrenheit: " + str(converter_celsius_para_fahrenheit(celsius)))