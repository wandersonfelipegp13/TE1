"""
1. Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas
primeiras.
"""
# Criando primeira lista
t1 = int(input("Tamanho da primeira lista: "))
l1 = list()
# Lendo primeira lista
for i in range(t1):
    l1.append(input(f"Valor {(i+1)}: "))

# Criando segunda lista
t2 = int(input("Tamanho da segunda lista: "))
l2 = list()
# Lendo segunda lista
for i in range(t2):
    l2.append(input(f"Valor {(i+1)}: "))

# Criando terceira lista
l3 = l1.copy() + l2.copy()
# Imprimindo terceira lista
print(l3)