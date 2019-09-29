# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Elaborar um programa que calcule e apresente o volume de uma caixa retangular.
Use a fórmula: VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
'''

def calcular_volume_caixa_retangular(comprimento, largura, altura):
  return comprimento * largura * altura;

if __name__ == "__main__":
  
  # Valores 10, 4 e 4 usados apenas para testar a função.
  volume = calcular_volume_caixa_retangular(10, 4, 4)
  print(volume)
