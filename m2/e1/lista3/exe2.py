"""2. Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos."""

l1 = ["A", "B", "B", "D"]
l2 = ["2", "A", "x", "C", "B"]
l3 = []

for i in l1:
    if i not in l3:
        l3.append(i)
for i in l2:
    if i not in l3:
        l3.append(i)

print(l3)
