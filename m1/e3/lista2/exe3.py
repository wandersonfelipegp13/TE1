"""
3. Escreva um programa que leia n números inteiros e imprima quantos deles estão nos seguintes
intervalos: [0, 25], [26, 50], [51, 75] e [76, 100]. Por exemplo, para n = 10 e os seguintes números
{2, 61, −1, 0, 88, 55, 3, 121, 25, 75}, seu programa deve imprimir:

[0, 25]: 4
[26, 50]: 0
[51, 75]: 3
[76, 100]: 1
"""

n = int(input("n: "))
l = []
for i in range(n):
    l.append(int(input(f"n{i+1}: ")))
i1 = i2 = i3 = i4 = 0
for o in l:
    if o >= 0 and o <=25:
        i1 = i1 + 1
    elif o >= 26 and o <=50:
        i2 = i2 + 1
    elif o >= 51 and o <=75:
        i3 = i3 + 1
    elif o >= 76 and o <= 100:
        i4 = i4 + 1

print(f"[0, 25]: {i1}\n[26, 50]: {i2}\n[51, 75]: {i3}\n[76, 100]: {i4}")
