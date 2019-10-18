# -*- coding: utf-8 -*- [Define a utilização de alguns
# caracteres especiais, como ~, ^, etc.]

'''
Ler 3 valores (considere que não serão informados valores iguais)
 e escrever a soma dos 2 maiores.
'''

# Inicializando uma lista para adicionar os valores
lista_valores = [0] * 3

# Inicializando a variável soma
soma = 0

# Lendo os valores e adicionando a lista de valores
for pos in range(3):
    valor = int(input("Digite o {}° valor: ".format(pos+1)))
    lista_valores[pos] = valor

# Assumindo o primeiro valor da lista como menor
menor = lista_valores[0]

# Encontrando o menor valor para excluílo da soma
for valor in lista_valores:
    if (valor < menor):
        menor = valor

# Acessando a lista de valores e somando apenas os 2 maiores
for valor in lista_valores:
    if (valor != menor):
        soma += valor

# Printando o resultado da soma
print("A soma dos 2 maiores valores é:", soma)
