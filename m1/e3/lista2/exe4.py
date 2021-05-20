"""
4. Faça um programa que leia um número inteiro positivo n e imprima n linhas com o seguinte
formato (exemplo para n = 6):
1
 2
  3
   4
    5
     6
"""
n = int(input("n: "))
for i in range(n):
    print(' ' * i, i + 1)
