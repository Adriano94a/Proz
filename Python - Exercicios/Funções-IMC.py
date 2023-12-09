def imc_aluno(peso,altura):
    imc = (peso) / altura ** 2
#   print(round(imc, 2)) #função round auxilia na formatação de casas decimais
    if (imc <= 18.5):return "Magreza"
    elif(imc > 18.5) and (imc <= 24.9):return "Saudavel"
    elif(imc >= 25) and (imc <= 29.9):return "Sobrepeso"
    elif(imc >30) and (imc <= 34.9):return "Obesidade grau 1"
    elif(imc > 35) and (imc <=39.9):return "Obesidade severa grau 2"
    else:return "Obesidade morbida grau 3"


peso = int(input("Qual o seu peso:"))
altura = float(input("Qual a sua altura:"))
resultado_imc = imc_aluno(peso, altura)
print(resultado_imc)