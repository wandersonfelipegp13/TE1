import numpy as np
# Define o número de épocas da simulação e o número de atributos
numEpocas = 1
numAmostras = 4
# Atributos
x1 = np.array([0.1, 0.3, 0.6, 0.5])
x2 = np.array([0.4, 0.7, 0.9, 0.7])
x3 = np.array([0.7, 0.2, 0.8, 0.1])
# bias
bias = 1
# Entrada do Perceptron.
X = np.vstack((x1, x2, x3))  # Ou X = np.asarray([peso, pH])
# print(X)

Y = np.array([1, -1, -1, 1])
# Taxa de aprendizado.
eta = 0.01
# Array para amazernar os erros.
e = np.zeros(6)
# Define a matriz de pesos.
W = np.ones([1, 4])  # Duas entradas e o bias !
# print(W)
for j in range(numEpocas):
    for k in range(numAmostras):
        # Insere o bias no vetor de entrada.
        Xb = np.hstack((bias, X[:, k]))
        # Calcula o vetor campo induzido.
        V = np.dot(W, Xb)
        # Calcula a saída do perceptron.
        Yr = np.sign(V)
        # Calcula o erro: e = (Y - Yr)
        e[k] = Y[k] - Yr
        # Treinando a rede.
        W = W + eta * e[k] * Xb
print(V)
# print(W)
# print("Vetor de errors (e) = " + str(e))

