"""
5. Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda
"""

l1 = ["A", "B", "B", "D"]
l2 = ["2", "A", "x", "C", "B", "x"]
ax = []

print("Valores comuns as duas listas: ", end="")
for i in l1 and l2:
    if i in l1 and l2:
        ax.append(i)
print(ax)
ax.clear()

print("Valores que só existem na primeira: ", end="")
for i in l2 and l1:
    if i in l1 and i not in l2 and i not in ax:
        ax.append(i)
print(ax)
ax.clear()

print("Valores que só existem na segunda: ", end="")
for i in l1 and l2:
    if i in l2 and i not in l1 and i not in ax:
        ax.append(i)
print(ax)
ax.clear()

print("Lista com os elementos não repetidos das duas listas (interpretacao 1): ", end="")
for i in l1 + l2:
    if i not in ax:
        ax.append(i)
print(ax)
ax.clear()

print("Lista com os elementos não repetidos das duas listas (interpretacao 2): ", end="")
for i in l1:
    if l1.count(i) == 1 and i not in ax:
        ax.append(i)
for i in l2:
    if l2.count(i) == 1 and i not in ax:
        ax.append(i)
print(ax)
ax.clear()

print("Lista com os elementos não repetidos das duas listas (interpretacao 3): ", end="")
for i in l1:
    if l1.count(i) == 1:
        ax.append(i)
for i in l2:
    if l2.count(i) == 1:
        ax.append(i)
print(ax)
ax.clear()

l2.append("A")
print("A primeira lista sem os elementos repetidos na segunda: ", end="")
ax2 = []
for i in l2:
    if l2.count(i) > 1:
        ax2.append(i)
for i in l1:
    if i not in ax2:
        ax.append(i)
print(ax)
ax.clear()
