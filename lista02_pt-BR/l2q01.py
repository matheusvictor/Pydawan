# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
'''
def máxima (valor_1= int(input("insira o primeiro valor:")),valor_2= int(input("insira o segundo valor:")),
            valor_3= int(input("insira o terceiro valor:"))):#função que recebe a entrada do usuário como parâmetro

	if (valor_1 > valor_2) and (valor_1 > valor_3)and (valor_2!=valor_3): #condição para verificar se o valor 1 é maior
		maior = valor_1
		print (maior) #imprimir o maior valor	
	
	elif (valor_2 > valor_1) and (valor_2 > valor_3) and(valor_1!=valor_3): #condição para verificar se o valor 3 é maior
		maior = valor_2
		print (maior) #imprimir o maior valor
	
	elif (valor_3 > valor_1) and (valor_3 > valor_2) and (valor_1!=valor_2) : #condição para verificar se o valor 3 é maior
		maior = valor_3
		print (maior) #imprimir o maior valor
  	
	else: 
		print ("Os números inseridos devem ser exclusivos (todos os números devem ser diferentes.) Tente novamente")
		return máxima(valor_1= int(input("insira o primeiro valor:")),valor_2= int(input("insira o segundo valor:")),valor_3=int(input("insira o primeiro valor:")))
		
máxima()
