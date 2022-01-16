# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

def converter_fahrenheit_para_celsius(F):
	return ((F - 32) * 5) / 9

if __name__ == "__main__":
	fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
	print("Grau(s) em Celsius: " + str(converter_fahrenheit_para_celsius(fahrenheit)))
	