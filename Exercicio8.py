ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
    {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
    {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
]

TIPOS_VALIDOS = {"servidor", "estacao", "switch", "roteador"}
STATUS_VALIDOS = {"ativo", "inativo"}


def buscar_por_ip(ip):
    for ativo in ativos:
        if ativo["ip"] == ip:
            return ativo
    return None


while True:
    print("\n[1] Cadastrar ativo")
    print("[2] Listar ativos")
    print("[3] Buscar por IP")
    print("[4] Alterar status")
    print("[5] Remover ativo")
    print("[6] Sair")
    opcao = input("Escolha: ")

    try:
        if opcao == "1":
            nome = input("Nome: ")
            tipo = input("Tipo (servidor/estacao/switch/roteador): ")
            if tipo not in TIPOS_VALIDOS:
                raise ValueError(f"Tipo '{tipo}' inválido!")
            ip = input("IP: ")
            if buscar_por_ip(ip):
                raise ValueError("IP já cadastrado!")
            ativos.append({"nome": nome, "tipo": tipo, "ip": ip, "status": "ativo"})
            print("Cadastrado!")

        elif opcao == "2":
            if not ativos:
                print("Nenhum ativo cadastrado.")
            for ativo in ativos:
                print(f"- {ativo['nome']} ({ativo['tipo']}) | IP: {ativo['ip']} | Status: {ativo['status']}")

        elif opcao == "3":
            ip = input("IP a buscar: ")
            ativo = buscar_por_ip(ip)
            if ativo is None:
                raise ValueError("Ativo não encontrado")
            print(f"Nome: {ativo['nome']} | Tipo: {ativo['tipo']} | Status: {ativo['status']}")

        elif opcao == "4":
            ip = input("IP do ativo: ")
            ativo = buscar_por_ip(ip)
            if ativo is None:
                raise ValueError("Ativo não encontrado")
            novo_status = input("Novo status (ativo/inativo): ")
            if novo_status not in STATUS_VALIDOS:
                raise ValueError(f"Status '{novo_status}' inválido!")
            ativo["status"] = novo_status
            print("Status atualizado!")

        elif opcao == "5":
            ip = input("IP do ativo a remover: ")
            ativo = buscar_por_ip(ip)
            if ativo is None:
                raise ValueError("Ativo não encontrado")
            ativos.remove(ativo)
            print("Ativo removido!")

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    except ValueError as e:
        print(f"Erro: {e}")