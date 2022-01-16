# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

#Inicialização das variáveis principais do programa;
anoAtual = 0
anoNascimento = 0 
idade = 0

#inputs dos dados solicitados pelo exercício;
anoAtual = (int(input("Infome o ano atual: ")))
anoNascimento = (int(input("Infome o seu ano de nascimento: ")))

#calculo da idade;
idade = (anoAtual-anoNascimento)

#print da idade do usuário;
print("Idade: ",idade)

#uso da expressão condicional que é chamado de operador ternário em algumas outras linguagens, mas é um if else simples
#e pode ser substituido pela forma convencional de escrita;
print("Pode votar" if idade>=16 else "Não pode votar")
 
