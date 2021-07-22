import numpy as np

w = [2.87558617, 1.41430368, 2.38864992, -0.67117034]
bias = 1

# x = [-0.3665, 0.0620, 5.9891]
x = [-0.7842, 1.1267, 5.5912]

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
