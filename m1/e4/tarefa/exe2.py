"""
2. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
"""

vel = int(input("Velocidade (km/h): "))
if vel > 80:
    vel -= 80
    print("Multa = R$ %.2f" % vel)
else:
    print("Tudo ok!")