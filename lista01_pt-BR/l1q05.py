# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Elabore um algoritmo capaz de ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius.
A fórmula de conversão é C ← ((F - 32) * 5) / 9 , sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

def converter_fahrenheit_para_celsius(F):
	return ((F - 32) * 5) / 9

if __name__ == "__main__":
	fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
	print("Grau(s) em Celsius: " + str(converter_fahrenheit_para_celsius(fahrenheit)))