# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
'''

def maximum(a, b, c): 

	if (a >= b) and (a >= c): 
		largest = a 

	elif (b >= a) and (b >= c): 
		largest = b 
	else: 
		largest = c 
		
	return largest
