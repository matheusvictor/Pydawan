# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

def calculaSalarioLiqProfessor(sal_bruto: float, pct_impostos) -> None:
    '''
    Função que retorna o salário líquido em R$ de um professor dado salário bruto em R$ e 
    porcentagem de impostos (em porcentagem ou fracionário)
    '''

    str_salario = "Salário líquido após descontos: R$ "
    str_imposto_100 = "Imposto igual ou superior a 100%"

    if type(sal_bruto) != float:
        print("Entre com sal_bruto do tipo float.")
    elif type(pct_impostos) == float:
        if (pct_impostos >= 1.0):
            print(str_imposto_100)
        else:
            # caso seja float (e.g. => 0.02 que equivale a 2%)
            print(str_salario + str(sal_bruto * (1 - pct_impostos)))
    elif type(pct_impostos) == int:
        if (pct_impostos >= 100):
            print(str_imposto_100)
        else:
            # caso seja int (e.g. => 20 que equivale a 20%)
            print(str_salario + str(sal_bruto * (1 - pct_impostos/100)))
    else:
        print("Entre com pct_impostos do tipo float ou int")


calculaSalarioLiqProfessor(1000.0, 0.02) # deve printar R$ 980.0 (2% de imposto)
calculaSalarioLiqProfessor(1000.0, 20) # deve printar R$ 800.0 (20% de imposto)
