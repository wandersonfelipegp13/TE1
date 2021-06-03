"""
2 Elaborar um outro programa em Python, que lê os dados do arquivo gerado no item anterior.
Assim sendo:
a) Imprima uma listagem contendo os nomes de clientes (contribuintes e dependentes) que possuem
idades acima de 60 anos.
b) Imprima uma listagem contendo os nomes de clientes (contribuintes e dependentes) em que a
substring "da Silva" é parte do nome.
c) A partir de 1o. de julho os planos de saúde terão um reajuste. Aplique um aumento de 11% no
valor do plano de cada contribuinte e salve em um novo arquivo os dados atualizados.
d) Identifique os planos com a maior e a menor média de idades entre seus integrantes (contribuinte
e dependentes). Em seguida, gere um relatório em arquivo com todos os dados destes dois planos.
"""

dados = []


def leArq():
    arq = open("files/arquivo1.txt", "r")
    for linha in arq:
        txt = linha.replace("\n", "")
        dados.append(txt.split(", "))


def maior60():
    nomes = []
    for i in range(len(dados)):
        obj = dados[i]
        if int(obj[1]) > 60:
            nomes.append(obj[0])
        if int(obj[2]) > 0:
            for c in range(3, len(obj) - 1, 2):
                nomed = obj[c]
                if int(obj[c + 1]) > 60:
                    nomes.append(nomed)
    return nomes


def daSilva():
    nomes = []
    for i in range(len(dados)):
        obj = dados[i]
        if "da Silva" in obj[0]:
            nomes.append(obj[0])
        if int(obj[2]) > 0:
            for c in range(3, len(obj) - 1, 2):
                nomed = obj[c]
                if "da Silva" in nomed:
                    nomes.append(nomed)
    return nomes


def mais11():
    reaj = dados.copy()
    for e in reaj:
        e[len(e) - 1] = format(float(e[len(e) - 1]) * 1.11, ".2f")
    with open("files/arquivo2.txt", "w") as a:
        for c in reaj:
            txt = ", ".join(c)
            a.write(txt + "\n")
    return reaj


# Um plano é uma linha no arquivo1.txt
# A media se baseia na idades das pessoas do plano


def medias():
    maior = dados[0]
    ma = cal(dados[0])
    menor = dados[0]
    me = cal(dados[0])

    for i in range(1, len(dados)):

        obj = dados[i]
        med = cal(obj)

        if med > ma:
            maior = obj
            ma = med
        if med < me:
            menor = obj
            me = med
    return maior, format(ma, ".2f"), menor, format(me, ".2f")


def cal(obj):

    med = 0
    n = 0

    # idades dos contribuintes
    med = med + int(obj[1])
    n = n + 1
    # idades dos dependentes
    if int(obj[2]) > 0:
        for c in range(4, len(obj) - 1, 2):
            med = med + int(obj[c])
            n = n + 1
    # a media
    med = med / n
    return med


def printPlan(plan):
    txt = ""
    for i in range(len(plan)):
        txt += " Nome do contribuinte: " + plan[0] + "\n"
        txt += " Idade do contribuinte: " + plan[1] + "\n"
        txt += " Quantidade de dependentes: " + plan[2] + "\n"
        if int(plan[2]) > 0:
            for c in range(3, len(plan) - 1, 2):
                txt += " Nome dependente: " + plan[c] + "\n"
                txt += " Idade dependente: " + plan[c + 1] + "\n"
        txt += " Valor do plano: " + plan[len(plan) - 1]
        return txt


def report(maior, menor):
    with open("files/arquivo3.txt", "w") as a:
        txt = ", ".join(maior)
        a.write(txt + "\n")
        txt = ", ".join(menor)
        a.write(txt + "\n")


leArq()
print("Maiores de 60: ", maior60(), "\n")
print("da Silva: ", daSilva(), "\n")
print("Reajuste: ", mais11(), "\n")
report(medias()[0], medias()[2])
print(f"Maior media = {medias()[1]} do plano:\n{printPlan(medias()[0])}")
print(f"Menor media = {medias()[3]} do plano:\n{printPlan(medias()[2])}")
