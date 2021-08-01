import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random((5, 4)), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

# Adicionar novas colunas derivadas de outras

df['new'] = df['W'] + df['X']
print(df)

# Selecionar colunas específicas

print(df[['W', 'Z']])

# Deletar colunas

df = df.drop(['new'], axis=1)
print(df)

# Selecionar parte de um DataFrame

x = df.loc[['A', 'B'], ['X', 'Y', 'Z']]
print(x)
