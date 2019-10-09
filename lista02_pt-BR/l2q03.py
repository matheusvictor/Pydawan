# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler as notas da 1ª e 2ª avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado. Considere que nota igual ou maior que 6 o aluno é aprovado.
Escreva também a média calculada.
'''

nota1 = input('Informe a nota da 1ª avaliação: ')
nota2 = input('Informe a nota da 2ª avaliação: ')

media = (float(nota1)+float(nota2)) / 2

if media >= 6:
    print("Parabéns, você foi aprovado! Sua média nas duas avaliações foi de", media)
else:
    print("Você está reprovado. Sua média nas duas avaliações foi de", media)

