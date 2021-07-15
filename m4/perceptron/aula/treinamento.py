import numpy as np
# Define o número de épocas da simulação e o número de atributos
numEpocas = 100000
numAmostras = 6
# Atributos
peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])
# bias
bias = 1
# Entrada do Perceptron.
X = np.vstack((peso, pH))  # Ou X = np.asarray([peso, pH])
Y = np.array([-1, 1, -1, -1, 1, 1])
# Taxa de aprendizado.
eta = 0.01
# Array para amazernar os erros.
e = np.zeros(6)
# Define a matriz de pesos.
W = np.ones([1, 3])  # Duas entradas e o bias !
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

print(W)
print("Vetor de errors (e) = " + str(e))
