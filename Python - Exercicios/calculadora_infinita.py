def calculadora():
    while True:
        print("Selecione o que deseja:")
        print("1: soma")
        print("2: subtração")
        print("3: Multiplicação")
        print("4: Divisão")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 0:
            print("Finalizando a calculadora")
            break
        elif escolha in [1, 2,3,4]:
            num1 = int(input("Digite o primeiro valor:"))
            num2 = int(input("Digite o segundo valor:"))

            if escolha == 1:
                res = num1 + num2
                print(res)
            elif escolha == 2:
                res = num1 - num2
                print(res)
            elif escolha == 3:
                res = num1 * num2
                print(res)
            elif escolha == 4:
                if num2 != 0:
                    res = num1 / num2
                    print(res)
                else:
                    print("Não é possível dividir por zero.")
        else:
            print("Opção invalida, tente novamente.")

calculadora()