# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler dois valores e imprimir uma das três mensagens a seguir:

- ‘Números iguais’, caso os números sejam iguais;
- ‘Primeiro é maior’, caso o primeiro seja maior que o segundo; ‘Segundo maior’, caso o segundo seja maior que o primeiro.

'''

#inicialização de variaveis
num_1 = 0
num_2 = 0

#input dos dados inseridos pelo usuário
num_1 = (float(input("Informe o primeiro valor: ")))
num_2 = (float(input("Informe o segundo valor: ")))

#condicional if else para verificar se os valores sao iguais, ou qual o maior entre eles
if num_1==num_2:
    print("Números iguais")
elif num_1>num_2:
    print("Primeiro é maior")
else:
    print("Segundo maior")