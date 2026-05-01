especiais = "!@#$%&*"

while True:
    senha = input("Digite uma senha: ")
    erros = []

    if len(senha) < 8:
        erros.append("- Mínimo 8 caracteres")
    if not any(c.isupper() for c in senha):
        erros.append("- Falta pelo menos 1 letra maiúscula")
    if not any(c.islower() for c in senha):
        erros.append("- Falta pelo menos 1 letra minúscula")
    if not any(c.isdigit() for c in senha):
        erros.append("- Falta pelo menos 1 número")
    if not any(c in especiais for c in senha):
        erros.append("- Falta pelo menos 1 caractere especial (!@#$%&*)")

    if not erros:
        print("Senha válida!")
        break

    print("Senha inválida! Problemas encontrados:")
    for erro in erros:
        print(erro)