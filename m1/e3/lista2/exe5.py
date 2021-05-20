"""
5. Faça um programa que leia um número n e imprima n linhas com o seguinte formato (exemplo
para n = 6):
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
"""

n = int(input("n: "))

for i in range(n):
    for j in range(i+1):
        print(f"{j+1} ", end="")
    print()
