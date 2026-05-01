ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

while True:
    print("\n[1] Adicionar IP")
    print("[2] Remover IP")
    print("[3] Listar todos")
    print("[4] Buscar IP")
    print("[5] Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        ip = input("Digite o IP: ")
        if ip in ips:
            print("IP já existe na lista!")
        else:
            ips.append(ip)
            print("IP adicionado!")

    elif opcao == "2":
        ip = input("Digite o IP a remover: ")
        if ip in ips:
            ips.remove(ip)
            print("IP removido!")
        else:
            print("IP não encontrado!")

    elif opcao == "3":
        if not ips:
            print("Lista vazia.")
        else:
            for i, ip in enumerate(ips, start=1):
                print(f"{i}. {ip}")

    elif opcao == "4":
        ip = input("Digite o IP a buscar: ")
        if ip in ips:
            posicao = ips.index(ip) + 1
            print(f"IP encontrado na posição {posicao}")
        else:
            print("IP não encontrado")

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")