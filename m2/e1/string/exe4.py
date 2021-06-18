"""
4. Um palíndromo é uma palavra ou frase que pode ser lida da
mesma forma tanto da esquerda para a direita como da direita
para a esquerda (desconsiderando os espaços em branco).
Considere que a entrada não possui sinais de pontuação ou
acentos. Escreva um programa que, dada uma String, verifique
se ela é um palíndromo.
"""

txt = input("Entre com uma palavra ou frase: ")
txt = txt.lower()
txt = txt.replace(" ", "")

i = 0
j = len(txt) - 1

palindromo = True

while i < j:
    if txt[i] != txt[j]:
        palindromo = False
        break
    else:
        i = i + 1
        j = j - 1
if palindromo:
    print("Palíndromo")
else:
    print("Não palíndromo")