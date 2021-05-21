"""
1. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com
a tabela a seguir.
+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
"""

csm = int(input("Consumo (kWh): "))
typ = input(" [R] Residências\n [I] Indústrias \n [C] Comércios\nInstalação: ")
if typ == 'R':
    if csm > 500:
        csm = csm * 0.65
    else:
        csm = csm * 0.40
elif typ == 'I':
    if csm > 5000:
        csm = csm * 0.60
    else:
        csm = csm * 0.55
else:
    if csm > 1000:
        csm = csm * 0.60
    else:
        csm = csm * 0.55

print("Preço = R$ %.2f" % csm)