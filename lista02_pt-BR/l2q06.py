# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
'''

#incializacao de variaveis
num_1 = 0
num_2 = 0

#coloquei os input como float para o caso do usuario inserir valores nao inteiros
num_1 = float(input("Informe o primeiro número: "))
num_2 = float(input("Informe o segundo número: "))

#loop que solicita ao usuario que insira um segundo valor diferente
while(num_1==num_2):
    num_2 = float(input("Informe o segundo número difente do primeiro: "))

#condicional ifelse para verificar qual o maior e mostrar a ordem crescente
if num_1>num_2:
    print("Ordem crescente: ",num_1," ; ",num_2)
else:
    print("Ordem crescente: ",num_2," ; ",num_1)
