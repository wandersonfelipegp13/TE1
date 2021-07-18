import random
import numpy as np
# Define o número de épocas da simulação e o número de atributos
numEpocas = 0
numAmostras = 30
# bias
bias = 1
# Entrada do Perceptron.

x1 = np.array([-0.6508, -1.4492, 2.0850, 0.2626, 0.6418, 0.2569, 1.1155, 0.0914, 0.0121, -0.0429,
               0.4340, 0.2735, 0.4839, 0.4089, 1.4391, -0.9115, 0.3654, 0.2144, 0.2013, 0.6483,
               -0.1147, -0.7970, -1.0625, 0.5307, -1.2200, 0.3957, -0.1013, 2.4482, 2.0149, 0.2012])
x2 = np.array([0.1097, 0.8896, 0.6876, 1.1476, 1.0234, 0.6730, 0.6043, 0.3399, 0.5256, 0.4660,
               0.6870, 1.0287, 0.4851, -0.1267, 0.1614, -0.1973, 1.0475, 0.7515, 1.0014, 0.2183,
               0.2242, 0.8795, 0.6366, 0.1285, 0.7777, 0.1076, 0.5989, 0.9455, 0.6192, 0.2611])
x3 = np.array([4.0009, 4.4005, 12.0710, 7.7985, 7.0427, 8.3265, 7.4446, 7.0677, 4.6316, 5.4323,
               8.2287, 7.1934, 7.4850, 5.5019, 8.5843, 2.1962, 7.4858, 7.1699, 6.5489, 5.8991,
               7.2435, 3.8762, 2.4707, 5.6883, 1.7252, 5.6623, 7.1812, 11.2095, 10.9263, 5.4631])

X = np.vstack((x1, x2, x3))
# print(X)

Y = np.array([-1.0000, -1.0000, -1.0000, 1.0000, 1.0000, -1.0000, 1.0000, -1.0000, 1.0000, 1.0000,
              -1.0000, 1.0000, -1.0000, -1.0000, -1.0000, -1.0000, 1.0000, 1.0000, 1.0000, 1.0000,
              -1.0000, 1.0000, 1.0000, 1.0000, 1.0000, -1.0000, -1.0000, 1.0000, -1.0000, 1.0000])
# Taxa de aprendizado.
eta = 0.01
# Array para amazernar os erros.
e = np.zeros(30)
# Define a matriz de pesos.
W = list()
for c in range((len(X) + 1)):
    W.append(random.random())
print("w(s) gerados aleatoriamente: ", end="")
print(W)

erro = True
# for j in range(numEpocas):
while erro or numEpocas > 10000:
    erro = False
    for k in range(numAmostras):
        # Insere o bias no vetor de entrada.
        Xb = np.hstack((bias, X[:, k]))
        # Calcula o vetor campo induzido.
        V = np.dot(W, Xb)
        # Calcula a saída do perceptron.
        Yr = np.sign(V)
        # Calcula o erro: e = (Y - Yr)
        e[k] = Y[k] - Yr
        if Y[k] != Yr:
            erro = True
            # Treinando a rede.
            W = W + eta * e[k] * Xb
            numEpocas = numEpocas + 1
            break

print("w(s) após execução: ", end="")
print(W)
print("Vetor de errors (e) = " + str(e))
print(f"Épocas: {numEpocas}")
