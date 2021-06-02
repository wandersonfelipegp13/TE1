"""
1 Elaborar um programa em Python para:
• Ler dados de uma Agência de Planos de Saúde;
• Gerar um arquivo contendo os dados lidos no seguinte formato:

Nome do contribuinte, idade do contribuinte, quantidade de dependentes,
nomes dos dependentes e respectivas idades dos dependentes, valor do plano

Não se sabe quantos contribuintes existem mas, o programa deve terminar quando for digitado:
'xxx' ou 'XXX'.
"""

# O programa para a qualquer momento que o usuario digitar 'xxx' ou 'XXX'

dados = []


def continua(s):
    if s != "xxx" and s != "XXX":
        contr.append(s)
        return s
    grava()
    exit()


def grava():
    arq = open("files/arquivo1.txt", "a")
    for c in dados:
        txt = ",".join(c)
        arq.write(txt + "\n")
    arq.close()


while True:

    contr = []
    continua(input("Nome do contribuinte: "))
    continua(input("Idade do contribuinte: "))
    qntdeDep = int(continua(input("Quantidade de dependentes: ")))
    for i in range(qntdeDep):
        continua(input(f"Nome do dependente {i + 1}: "))
        continua(input(f"Idade do dependente {i + 1}: "))
    continua(input("Valor do plano: "))

    dados.append(contr.copy())
