import random

senhas = {
    "gmail": "MinhaS3nha!",
    "github": "Dev@2024Seguro",
    "banco_dados": "db123",
}

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
ESPECIAIS = "!@#$%&*"


def avaliar_forca(senha):
    if len(senha) < 8:
        return "Fraca"

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for c in senha:
        if c.isupper():
            tem_maiuscula = True
        elif c.islower():
            tem_minuscula = True
        elif c.isdigit():
            tem_numero = True
        elif c in ESPECIAIS:
            tem_especial = True

    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return "Forte"
    if tem_minuscula and tem_numero:
        return "Média"
    return "Fraca"


def gerar_senha(tamanho):
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha


while True:
    print("\n[1] Cadastrar senha")
    print("[2] Listar serviços")
    print("[3] Buscar senha por serviço")
    print("[4] Gerar senha aleatória")
    print("[5] Avaliar força de todas as senhas")
    print("[6] Exportar relatório")
    print("[7] Sair")
    opcao = input("Escolha: ")

    try:
        if opcao == "1":
            servico = input("Serviço: ").lower()
            if servico in senhas:
                raise ValueError("Serviço já cadastrado!")
            senha = input("Senha: ")
            senhas[servico] = senha
            forca = avaliar_forca(senha)
            print(f"Cadastrado! Força: {forca}")

        elif opcao == "2":
            if not senhas:
                print("Nenhum serviço cadastrado.")
            for servico in senhas:
                print(f"- {servico}")

        elif opcao == "3":
            servico = input("Serviço: ").lower()
            if servico not in senhas:
                raise KeyError("Serviço não encontrado!")
            print(f"{servico}: {senhas[servico]}")

        elif opcao == "4":
            tamanho = int(input("Tamanho: "))
            if tamanho < 1:
                raise ValueError("Tamanho deve ser positivo!")
            print(f"Senha gerada: {gerar_senha(tamanho)}")

        elif opcao == "5":
            print("=== Avaliação de Senhas ===")
            for servico, senha in senhas.items():
                forca = avaliar_forca(senha)
                print(f"{servico}: \"{senha}\" → {forca}")

        elif opcao == "6":
            try:
                with open("senhas_relatorio.txt", "w", encoding="utf-8") as f:
                    f.write("=== Relatório de Senhas ===\n\n")
                    for servico, senha in senhas.items():
                        forca = avaliar_forca(senha)
                        f.write(f"{servico}: {senha} → {forca}\n")
                print("Relatório exportado com sucesso!")
            except IOError as e:
                print(f"Erro ao exportar: {e}")

        elif opcao == "7":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    except ValueError as e:
        print(f"Erro: {e}")
    except KeyError as e:
        print(f"Erro: {e}")