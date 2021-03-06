import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("files/Tabela_Dados_Treinamento_M4_3.6_RNA.csv")
df2 = pd.read_csv("files/Tabela-Amostras-para-validar_RNA_M4_3.6.csv")
X = np.asarray(df)
amostras = np.asarray(df2) 
linha = len(X)
coluna = len(X[0])

Y = list()

for i in range(linha):
    for j in range(coluna):
        if j == 3:
            Y.append(X[i][j])  # pego o 'd'

X = np.delete(X, 3, 1)  # removo o 'd'

# print(np.unique(Y))

# scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X)
scaler.fit(amostras)

X = scaler.transform(X)
amostras = scaler.transform(amostras)

from sklearn.neural_network import MLPClassifier

# era 1000, aumentar para 10000, alpha=0.0001
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=10000, alpha=0.001)

# let's fit the training data to our model

mlp.fit(X, Y)

print('Número de épocas: ', mlp.n_iter_)
print('Taxa de aprendizagem: ', mlp.alpha)

# mlp.loss curve

# print(len(mlp.loss_curve_))
x = list(range(0, len(mlp.loss_curve_)))
y = mlp.loss_curve_
plt.xlabel('Época')
plt.ylabel('Erro')
plt.plot(x, y)
plt.show()

# accuracy

from sklearn.metrics import accuracy_score

predictions_train = mlp.predict(X)
print(accuracy_score(predictions_train, Y))

from sklearn.metrics import confusion_matrix

conf_treino = confusion_matrix(predictions_train, Y)
print(conf_treino)

from sklearn.metrics import classification_report

print(classification_report(predictions_train, Y))

print("Amostras:", mlp.predict(amostras))
