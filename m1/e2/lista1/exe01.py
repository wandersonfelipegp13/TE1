"""
1. Faça um programa que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor
corresponde à temperatura em Fahrenheit ou Celsius. Em seguida, o programa deve ler o
valor da temperatura e então imprimir o valor correspondente à temperatura na outra
unidade de medida. Observação: (C = 5/9 × (F − 32)).
"""

option = input("Conversor de temperaturas\n F - Fahrenheit\n C - Celsius\n$ ")
temper = float(input("Temperatura: "))
if option == 'F':
    print(f"{temper} F = " + format(5 / 9 * (temper - 32), ".2f"), "C")
else:
    print(f"{temper} C = " + format((temper * 9/5) + 32, ".2f"), "F")
