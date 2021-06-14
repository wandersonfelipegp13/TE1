"""
Escreva um programa que, dada uma String representando um
texto, imprima o número de palavras existentes. Observação:
você deve remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!”
e “?”) antes de realizar a contagem das palavras.
"""

sin = [".", ",", ":", ";", "!", "?"]
txt = input("Texto: ")

for s in sin:
    txt = txt.replace(s, " ")

print("Número de palavras: ", len(txt.split()))
