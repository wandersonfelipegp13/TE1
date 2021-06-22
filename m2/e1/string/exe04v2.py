txt = input("Entre com uma palavra ou frase: ")
txt = txt.lower()
txt = txt.replace(" ", "")

if txt == txt[::-1]:
    print("́Palindromo")
else:
    print("̃Nao ́palindromo")
