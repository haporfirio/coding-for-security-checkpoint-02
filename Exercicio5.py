texto = input("Digite um texto: ").lower()
palavras = texto.split()

contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

# Ordena por frequência (decrescente)
ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

print("=== Contagem de Palavras ===")
for palavra, qtd in ordenado:
    vezes = "vez" if qtd == 1 else "vezes"
    print(f'"{palavra}" → {qtd} {vezes}')

mais_frequente = ordenado[0]
print(f'\nPalavra mais frequente: "{mais_frequente[0]}" ({mais_frequente[1]} vezes)')
print(f"Total de palavras únicas: {len(contagem)}")