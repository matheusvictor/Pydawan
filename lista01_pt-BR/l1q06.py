# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Desenvolva um algoritmo capaz de calcular e apresentar o valor do volume de uma lata de óleo, cujo tamanho deverá ser definido pelo usuário.
Utilize a fórmula: Volume ← π * Raio^2 * Altura
'''

#Declaração das variáveis principais do exercício.
pi = 3.14;
raio = 0;
altura= 0;
volume = 0;

#espaço reservado ao input de dados do usuário

raio = float(input("Informe o raio da lata: "))
altura = float(input("Informe a altura da lata: "))

#calculo do volume a partir da fórmula apresentada no exercício
volume = pi * (raio*raio) * altura;

#print do resultado para o usuário
print("Volume da lata = ",volume,"l");
