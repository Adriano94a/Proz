ano_atual = 2023
nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

while (ano_nascimento < 1922) or (ano_nascimento > ano_atual):
    ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_atual - ano_nascimento
print(f"A idade atual do {nome} é {idade} anos.")

