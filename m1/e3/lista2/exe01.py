"""
1. Considere o seguinte menu:
1 - Pizza Marguerita
2 - Pizza de Calabresa
3 - Pizza de Pepperoni
4 - Pizza de Mussarela
5 - Sair

O seu programa deve: imprimir o menu; ler um número de 1 até 5; e imprimir a opção do menu
correspondente ao número lido. Isso deve ser repetido até que o usuário selecione a opção 5.
"""

menx = ["Pizza Marguerita", "Pizza de Calabresa", "Pizza de Pepperoni", "Pizza de Mussarela"]
optn = 1

while optn != 5:
    # imprimir o menu
    print("~Menu~")
    for i in range(len(menx)):
        print(f"{i+1} - {menx[i]}")
    print(f"{i+2} - Sair")
    # ler um número de 1 até 5
    optn = int(input("> "))
    # imprimir a opção do menu
    if optn in range(len(menx) + 1):
        print(menx[optn - 1])
    if optn > len(menx) + 1 or optn < 0:
        print("Opção inválida!")
print("Volte sempre!")
