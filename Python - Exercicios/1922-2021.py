ano_atual = 2023
nome = str(input("Digite seu nome: "))

executar = True
while(executar == True):
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento: "))
        if (ano_nascimento < 1922) or (ano_nascimento > 2022):
            print("O ano precisa ser entre 1922 e 2022")
        else:
            idade = ano_atual - ano_nascimento
            print(f"A idade atual do {nome} é {idade} anos.")
            executar = False
    except:
        print("Os anos precisam ser escritos apenas com números.")

