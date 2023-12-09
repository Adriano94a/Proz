def calculadora(num1, num2):

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    escolha = int(input("[1] para somar, [2] para subtração, [3] para multiplicação, [4] para divisão: "))

    if escolha == 1:
        escolha = soma
    elif escolha ==2:
        escolha = subtracao
    elif escolha == 3:
        escolha = multiplicacao
    elif escolha == 4:
        escolha = divisao
    else:
        escolha = 0

    print(escolha)

num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))
resultado = calculadora(num1, num2)



