from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
iris = load_iris()

# mostra detalhes do dataset

# print(iris, iris.data, iris.target_names, iris.DESCR)
# print(iris.feature_names)

# usar colunas de comprimento e largura da pétala

iris.data = iris.data[:, [2, 3]]

y = iris.target

# print("Class labels: ", np.unique(y))

# splitting into train and test datasets

from sklearn.model_selection import train_test_split
# datasets = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1, stratify=y)
datasets = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1, stratify=y)

train_data, test_data, train_labels, test_labels = datasets

# scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# we fit the train data
scaler.fit(train_data)

# scaling the train data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

# print(train_data)

# Training the Model
from sklearn.neural_network import MLPClassifier
# creating an classifier from the model:

# era 1000, aumentar para 10000, alpha=0.0001
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=10000, learning_rate_init=0.01)

# let's fit the training data to our model
mlp.fit(train_data, train_labels)

print('Número de épocas: ', mlp.n_iter_)
print('Taxa de aprendizagem: ', mlp.alpha)

# mlp.loss curve

print(len(mlp.loss_curve_))
x = list(range(0, len(mlp.loss_curve_)))
y = mlp.loss_curve_
plt.xlabel('Época')
plt.ylabel('Erro')
plt.plot(x, y)
plt.show()

# accuracy

from sklearn.metrics import accuracy_score

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

from sklearn.metrics import confusion_matrix

conf_treino = confusion_matrix(predictions_train, train_labels)
print(conf_treino)

conf_test = confusion_matrix(predictions_test, test_labels)
print(conf_test)

from sklearn.metrics import classification_report

print(classification_report(predictions_test, test_labels))

# do livro do Sebastian Raschka
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    # markers = ('o', 'o', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    color=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx]

        # if LooseVersion(matplotlib.__version__) < LooseVersion('0.3.4'):
        if False:
            plt.scatter(X_test[:, 0],
                        X_test[:, 1],
                        c='',
                        edgecolor='black',
                        alpha=1.0,
                        linewidth=1,
                        marker='o',
                        s=100,
                        label='test set')
        else:
            plt.scatter(X_test[:, 0],
                        X_test[:, 1],
                        c='none',
                        edgecolor='black',
                        alpha=1.0,
                        linewidth=1,
                        marker='o',
                        s=100,
                        label='test set')


X_combined_std = np.vstack((train_data, test_data))
y_combined = np.hstack((train_labels, test_labels))

plot_decision_regions(X=X_combined_std, y=y_combined, classifier=mlp, test_idx=range(105, 150), resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
# plt.savefig('03_01.png', dpi=300)
plt.show()

# plotar iris  dataset
import numpy as np, matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
dados = iris.data[:, [2, 3]]
if True:
    # scaling the data
    scaler = StandardScaler()
    # we fit the train data
    scaler.fit(dados)
    # scaling the train data
    dados = scaler.transform(dados)

classes = iris.target  # rótulos de cada amostra
especies = np.unique(iris.target_names)  # obtém os nomes das espécies
cores = ['red', 'blue', 'green']  # cores para cada espécie
for i in np.unique(classes):
    # descompacta as 2 colunas (eixo 1) em x e y, para cada espécie
    x, y = np.split(dados[np.where(classes == i)], 2, 1)
    # monta a dispersão para cada espécie com sua respectiva cor e rótulo
    plt.scatter(x, y, color=cores[i], alpha=0.5, label=especies[i])
plt.xlabel('Comprimento da sépala (cm)')
plt.ylabel('Largura da pétala (cm)')
plt.title('Iris dataset: comprimentos pétala vs. largura pétala')
plt.legend(loc='lower right') #determina a posição da legenda
# plt.savefig('irisDataset.png', dpi=300)
plt.show()

