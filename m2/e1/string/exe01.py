"""
1. Escreva um programa que, dada uma sequência de números
inteiros (todos fornecidos na mesma linha, separados por
espaços), imprima a média desses números.
"""

txt = input("Entre com uma sequência de números: ")
num = txt.split()
som = 0

for n in num:
    som = som + int(n)
med = som / len(num)

print("A média é: ", format(med, ".2f"))