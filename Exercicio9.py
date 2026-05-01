logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

contagem_niveis = {"INFO": 0, "WARNING": 0, "ERROR": 0}
erros_por_ip = {}
malformados = 0

for log in logs:
    try:
        # O log tem 2 colchetes: [data] [nível]. Pegamos o segundo par.
        partes = log.split("[")
        # partes = ["", "data] ", "nivel] mensagem - IP: ip"]
        if len(partes) < 3:
            raise ValueError("formato inválido")

        nivel = partes[2].split("]")[0]
        ip = log.split("IP: ")[1].strip()

        if nivel not in contagem_niveis:
            raise ValueError("nível desconhecido")

        contagem_niveis[nivel] += 1

        if nivel == "ERROR":
            erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1

    except (IndexError, ValueError):
        malformados += 1

print("=== Relatório de Logs ===")
print(f"INFO:    {contagem_niveis['INFO']} eventos")
print(f"WARNING: {contagem_niveis['WARNING']} eventos")
print(f"ERROR:   {contagem_niveis['ERROR']} eventos")
print(f"Logs malformados: {malformados}")

if erros_por_ip:
    ip_mais_erros = max(erros_por_ip, key=erros_por_ip.get)
    print(f"\nIP com mais erros: {ip_mais_erros} ({erros_por_ip[ip_mais_erros]} erros)")

    print("\nDetalhamento de erros:")
    erros_ordenados = sorted(erros_por_ip.items(), key=lambda x: x[1], reverse=True)
    for ip, qtd in erros_ordenados:
        unidade = "erro" if qtd == 1 else "erros"
        print(f"  {ip} → {qtd} {unidade}")