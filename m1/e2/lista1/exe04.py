"""
1. Faça um programa que leia dois números e em seguida um caracter que representa um
operador aritmético (‘+’, ‘−’, ‘*’ ou ‘/’). Seu programa então deve imprimir o resultado
do operador aplicado aos dois números dados.
"""

n1 = float(input("n1: "))
n2 = float(input("n2: "))
ch = input("operador (‘+’, ‘−’, ‘*’ ou ‘/’): ")

if ch == '+':
    print(n1 + n2)
elif ch == '-':
    print(n1 - n2)
elif ch == '*':
    print(n1 * n2)
else:
    print(n1 / n2)
