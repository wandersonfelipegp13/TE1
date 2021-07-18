# Utilize a biblioteca Mathplotlib do Python para gerar um gráfico de linhas
# dos valores armazenados em uma lista
# e = [20, 10, 6.5, 6, 5, 4, 3.75, 3.5, 3.25, 3, 2.9, 2.8, 2.7].

import matplotlib.pyplot as plt

e = [20, 10, 6.5, 6, 5, 4, 3.75, 3.5, 3.25, 3, 2.9, 2.8, 2.7]
fig, ax = plt.subplots()
plt.plot(range(1, 14), e, marker='o')
ax.set(xlabel='Época', ylabel='Erro médio')
plt.show()
