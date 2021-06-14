"""
3. Escreva um programa que, dada uma String texto e uma String
palavra, ache todas as posições de ocorrência da palavra no
texto. O seu programa deve desconsiderar se as letras são
maiúsculas ou minúsculas.
"""

texto = input("Entre com um texto: ")
palavra = input("Entre com uma palavra: ")
texto = texto.lower()
palavra = palavra.lower()

removido = 0
while palavra in texto:
    posicao = texto.find(palavra)
    print(removido + posicao)
    texto = texto[posicao + 1:]
    removido = removido + (posicao + 1)
