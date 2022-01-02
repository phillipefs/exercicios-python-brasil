"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""

def imprimir_sequencia(n):
    contagem_linhas = 1    
    for numero in range(1,n+1):
        if contagem_linhas>10:
            break                    
        print((str(numero)+" ")*numero)
        contagem_linhas+=1

imprimir_sequencia(11)