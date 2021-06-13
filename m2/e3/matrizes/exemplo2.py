l = int(input("Entre com o número de linhas: ")) # l = 3
c = int(input("Entre com o número de colunas: ")) # c = 4
matriz = []

for i in range(l):
    linha = []
    for j in range(c):
        linha.append(i * c + j + 1)
    matriz.append(linha)
print(matriz)
