import numpy as np
# 1) Criar uma matriz X com 10 linhas e 2 colunas contendo números reais aleatórios
print("Matriz X:")
X = np.random.rand(10, 2)
print(X)

# 2) Criar um vetor W de tamanho 2 contendo números reais aleatórios.
print("Vetor W:")
W = np.random.rand(2)
print(W)

# 3) Apresente o resultado da produto escalar de cada linha da matriz X pelo vetor W
for i in range(10):
    print(f"({X[i][0]} * {W[0]}) + ({X[i][1]} * {W[1]}) = ", np.dot(X[i], W))
