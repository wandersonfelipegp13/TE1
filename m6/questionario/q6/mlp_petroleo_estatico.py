import matplotlib.pyplot as plt
import numpy as np

X = np.asarray([
        [-0.6508,0.1097,4.0009],
				[-1.4492,0.8896,4.4005],
				[2.0850,0.6876,12.0710],
				[0.2626,1.1476,7.7985],
				[0.6418,1.0234,7.0427],
				[0.2569,0.6730,8.3265],
				[1.1155,0.6043,7.4446],
				[0.0914,0.3399,7.0677],
				[0.0121,0.5256,4.6316],
				[-0.0429,0.4660,5.4323],
				[0.4340,0.6870,8.2287],
				[0.2735,1.0287,7.1934],
				[0.4839,0.4851,7.4850],
				[0.4089,-0.1267,5.5019],
				[1.4391,0.1614,8.5843],
				[-0.9115,-0.1973,2.1962],
				[0.3654,1.0475,7.4858],
				[0.2144,0.7515,7.1699],
				[0.2013,1.0014,6.5489],
				[0.6483,0.2183,5.8991],
				[-0.1147,0.2242,7.2435],
				[-0.7970,0.8795,3.8762],
				[-1.0625,0.6366,2.4707],
				[0.5307,0.1285,5.6883],
				[-1.2200,0.7777,1.7252],
				[0.3957,0.1076,5.6623],
				[-0.1013,0.5989,7.1812],
				[2.4482,0.9455,11.2095],
				[2.0149,0.6192,10.9263],
				[0.2012,0.2611,5.4631]])

d = np.asarray([-1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1])

amostra = np.asarray([[-0.3665,0.0620,5.9891],
                      [-0.7842,1.1267,5.5912],
                      [0.3012,0.5611,5.8234],
                      [0.7757,1.0648,8.0677],
                      [0.1570,0.8028,6.3040],
                      [-0.7014,1.0316,3.6005],
                      [0.3748,0.1536,6.1537],
                      [-0.6920,0.9404,4.4058],
                      [-1.3970,0.7141,4.9263],
                      [-1.8842,-0.2805,1.2548]])

# escalando

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X)
scaler.fit(amostra)

X = scaler.transform(X)
amostra = scaler.transform(amostra)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=10000, alpha=0.001)

mlp.fit(X, d)

print('Número de épocas: ', mlp.n_iter_)
print('Taxa de aprendizagem: ', mlp.alpha)

x = list(range(0, len(mlp.loss_curve_)))
y = mlp.loss_curve_
plt.xlabel('Época')
plt.ylabel('Erro')
plt.plot(x, y)
plt.show()

# accuracy

from sklearn.metrics import accuracy_score

predictions_train = mlp.predict(X)
print(accuracy_score(predictions_train, d))

from sklearn.metrics import confusion_matrix

conf_treino = confusion_matrix(predictions_train, d)
print(conf_treino)

from sklearn.metrics import classification_report

print(classification_report(predictions_train, d))

print("Amostras:", mlp.predict(amostra))
