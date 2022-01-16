# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

A = input("A: ")
B = input("B: ")

def swap(A, B):
    aux = A
    A = B
    B = aux

    print(f"A: {A}")
    print(f"B: {B}")
    
swap(A, B)
