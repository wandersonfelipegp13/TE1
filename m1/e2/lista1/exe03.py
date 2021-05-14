"""
3. Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das
situações abaixo:

1. • É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de
contribuição.
2. • É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de
contribuição.
3. • É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de
contribuição.
4. • É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de
contribuição.

Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o sexo de um
indivíduo, e dois inteiros, que representam a idade e o tempo de contribuição. O programa
deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações acima. Caso
contrário, o programa deverá imprimir “Não Aposentável”.
"""

sex = input("Sexo (M ou F): ")
age = int(input("Idade: "))
con = int(input("Tempo de contribuição: "))

if sex == 'M':
    if age >= 65 and con >= 10 or age >= 63 and con >= 15:
        print("Aposentável")
    else:
        print("Não Aposentável")
else:
    if age >= 63 and con >= 10 or age >= 61 and con >= 15:
        print("Aposentável")
    else:
        print("Não Aposentável")