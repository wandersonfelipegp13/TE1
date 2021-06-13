# Exemplo de como receber uma matriz de dimensões l × c como entrada

l = int(input("Entre com o número de linhas: "))
c = int(input("Entre com o número de colunas: "))
matriz = []

for i in range(l):
    linha = []
    for j in range(c):
        linha.append(int(input())) # recebendo os dados
    matriz.append(linha)

print(matriz)

# Forma alternativa/compacta de inicializar uma matriz
matriz = [[13 for i in range(c)] for j in range(l)]
# matriz = [13 for i in range(c)]

print(matriz)
