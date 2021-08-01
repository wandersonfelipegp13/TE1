import numpy as np
import pandas as pd

w = [5.11233131, 2.8340889, 4.93277417, -1.27227181]
bias = 1

df = pd.read_csv("files/Tabela-Amostras-para-validar_RNA_M4_3.6.csv")
x = np.asarray(df)

for i in range(len(x)):
    xb = np.hstack((bias, x[i]))
    u = 0

    yr = 0
    for j in range(len(w)):
        u = u + w[j] * xb[j]

    yr = np.sign(u)

    if yr == -1.0:
        print("P1")
    else:
        print("P2")
