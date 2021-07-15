import numpy as np

w = [-240.28, 11.64, -250.172]
bias = 1

# x = [113, 6.8]
x = [122, 4.7]

x = np.hstack((bias, x))
print(x)

u = 0

yr = 0
for j in range(len(w)):
    u = u + w[j] * x[j]

yr = np.sign(u)

if yr == -1.0:
    print("P1")
else:
    print("P2")
