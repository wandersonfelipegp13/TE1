"""
2. Faça um programa que leia um número n. Após isso, o seu programa deve ler uma sequência de n
números e imprimir uma mensagem indicando se a sequência lida está ordenada de forma crescente
ou não.
"""

n = int(input("n: "))
l = []
for i in range(n):
    l.append(int(input(f"n{i+1}: ")))
p = l[0]
for iten in l:
    if iten >= p:
        p = iten
    else:
        print("Não ordenada de forma crescente!")
        break
else:
    print("Ordenada de forma crescente!")