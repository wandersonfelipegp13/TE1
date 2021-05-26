"""
3. A lista de temperaturas de Paris, na França, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Jeito facil
# print(f"Menor temperatura = {min(T)}\nMaior temperatura = {max(T)}\n")

menor = T[0]
for i in range(1, len(T)):
    if T[i] < menor:
        menor = T[i]

maior = T[0]
for i in range(1, len(T)):
    if T[i] > maior:
        maior = T[i]

s = 0
for t in T:
    s += t

print(f"Menor temperatura = {menor}\nMaior temperatura = {maior}")
print(f"Media = {s/len(T)}")