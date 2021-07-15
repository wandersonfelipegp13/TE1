def funcaosinal(v):
    if v <= 0:
        return -1
    return 1


# w = [-369.99999999998755, 95.0000000000127, -1998.2200000004568]
w = [-2420.4, 116.6, -2502.09999999]
entrada = [1, 110, 6.5]
entrada2 = [1, 122, 4.7]  # laranja

u = 0

for i in range(len(w)):
    u = u + w[i] * entrada[i]
    # u = u + w[i] * entrada2[i]  # testar laranja

yr = funcaosinal(u)

if yr == -1.0:
    print("maçã")
else:
    print("laranja")
