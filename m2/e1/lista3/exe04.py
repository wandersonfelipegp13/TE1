"""4. Leia uma lista de números inteiros e verifique se a lista está ordenada."""

# Lista em ordem crescente
l1 = [1, 2, 4, 4, 5, 6, 7, 9]
# Lista em ordem decrescente
l2 = l1.copy()
l2.reverse()
# Lista sem ordem
l3 = [2, 4, 9, 3, 5, 1]

def ordem(l):

    if len(l) == 0:
        return "Vazia"
    if len(l) == 1:
        return "Ordenada"

    # Variavel para condicao de ordem crescente
    oc = True
    # Variavel para condicao de ordem decrescente
    od = True

    # Se o primeiro valor for menor que o segundo...
    if l[0] < l[1]:
        # ...nao pode ser ordem decrescente.
        od = False
        # Compara-se todos os valores adjacentes...
        for c in range(1, len(l) - 1):
            # ...e se algum for maior que seu sucesssor...
            if l[c] > l[c + 1]:
                # ...tambem nao esta em ordem crescente.
                oc = False
                break
    # Porem, se o primeiro valor for maior que o segundo...
    else:
        # ...nao pode ser ordem crescente.
        oc = False
        # Compara-se todos os valores adjacentes...
        for d in range(1, len(l) - 1):
            # ...e se algum for menor que seu sucesssor...
            if l[d] < l[d + 1]:
                # ...tambem nao esta em ordem decrescente.
                od = False
                break
    if oc:
        return "Ordem Crescente"
    elif od:
        return "Ordem Decrescente"
    else:
        return "Desordenado"

print(ordem(l1))
print(ordem(l2))
print(ordem(l3))
