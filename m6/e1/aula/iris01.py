from sklearn.datasets import load_iris
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

