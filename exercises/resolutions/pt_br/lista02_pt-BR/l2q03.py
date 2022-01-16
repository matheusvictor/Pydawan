# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

nota1 = input('Informe a nota da 1ª avaliação: ')
nota2 = input('Informe a nota da 2ª avaliação: ')

media = (float(nota1)+float(nota2)) / 2

if media >= 6:
    print("Parabéns, você foi aprovado! Sua média nas duas avaliações foi de", media)
else:
    print("Você está reprovado. Sua média nas duas avaliações foi de", media)

