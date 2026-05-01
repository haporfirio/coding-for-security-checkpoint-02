alunos = [
    ("Carlos", 8.5),
    ("Ana", 9.2),
    ("Bruno", 6.0),
    ("Diana", 7.8),
    ("Eduardo", 4.5),
]

maior_nome, maior_nota = alunos[0]
menor_nome, menor_nota = alunos[0]
soma = 0

for nome, nota in alunos:
    if nota > maior_nota:
        maior_nome, maior_nota = nome, nota
    if nota < menor_nota:
        menor_nome, menor_nota = nome, nota
    soma += nota

media = round(soma / len(alunos), 1)

print("=== Relatório de Notas ===")
print(f"Maior nota: {maior_nome} - {maior_nota}")
print(f"Menor nota: {menor_nome} - {menor_nota}")
print(f"Média da turma: {media}")
print("\nAlunos acima da média:")
for nome, nota in alunos:
    if nota > media:
        print(f"- {nome}: {nota}")