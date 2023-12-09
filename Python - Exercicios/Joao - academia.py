import time
print("-"*50)
print("ACADEMIA FIT PYTHON")
print("-"*50)
exercicio = str(input("Qual seu proximo exercício: "))
print(exercicio)

for i in range (1,13):
    print(f'Repetição {i}')
    time.sleep(1)
    i += 1

descanso = 1
print("-"*50)
print("Agora descansaremos 45 segundos")
print("-"*50)
while descanso <= 45:
    print(f"Segundos:{descanso}")
    time.sleep(1)
    descanso +=1
