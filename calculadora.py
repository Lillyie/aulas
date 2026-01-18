#calculadora básica, +-*/
while True:
    try:
        n1 = float(input("Digite um número: ").strip())
        n2 = float(input("Digite outro número: ").strip())
        op = input("Digite um operador (+ - * /): ").strip()

        if op == "+":
            print(n1 + n2)
        elif op == "-":
            print(n1 - n2)
        elif op == "*":
            print(n1 * n2)
        elif op == "/":
            if n2 == 0:
                print("não é possivel dividir por 0")
            else:
                print(n1 / n2)
        else:
            print("operador inválido")

    except ValueError:
        print("Por favor digite apenas números validos >:(")

    sair = input("Mais alguma coisa? (S/N): ").strip().lower().startswith("n")
    if sair:
        break
    else:
        continue
print("saiu da calculadora!")