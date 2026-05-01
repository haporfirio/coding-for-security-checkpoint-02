while True:
    try:
        entrada1 = input("Número 1: ")
        if entrada1.lower() == "sair":
            print("Encerrando calculadora.")
            break
        num1 = float(entrada1)

        num2 = float(input("Número 2: "))
        operacao = input("Operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError(f"Operação '{operacao}' não suportada. Use +, -, * ou /")

    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
    except ValueError as e:
        # Diferencia entre erro de conversão e operação inválida
        if "could not convert" in str(e) or "invalid literal" in str(e):
            print("Erro: Digite apenas números!")
        else:
            print(f"Erro: {e}")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Operação processada.")