import random
import numpy as np
import pandas as pd

df = pd.read_csv("files/Tabela_Dados_Treinamento_M4_3.6_RNA.csv")
X = np.asarray(df)
linha = len(X)
coluna = len(X[0])

Y = list()

for i in range(linha):
    for j in range(coluna):
        if j == 3:
            Y.append(X[i].__getitem__(j))  # pego o 'd'

X = np.delete(X, 3, 1)  # removo o 'd'

print(X)
print(Y)

numEpocas = 0
numAmostras = len(X)
bias = 1
eta = 0.01
e = np.zeros(linha)
W = list()
for c in range(coluna):
    W.append(random.random())
print("w(s) gerados aleatoriamente: ", end="")
print(W)
erro = True
while erro or numEpocas > 10000:
    erro = False
    for k in range(numAmostras):
        # Insere o bias no vetor de entrada.
        Xb = np.hstack((bias, X[k]))
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
