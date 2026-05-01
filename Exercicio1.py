frase = input("Digite uma frase: ").lower()

vogais = 0
consoantes = 0

for caractere in frase:
    if caractere in "aeiou":
        vogais += 1
    elif caractere.isalpha():
        consoantes += 1

print(f"Frase: \"{frase}\"")
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")

