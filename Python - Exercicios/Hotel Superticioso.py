print("Estrutura FOR")
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(f'Andar:{i}')
print()
print("Estrutura While")
andar = 1
while andar <= 20:
    if andar != 13:
        print(f"Andar:{andar}")
    andar += 1

print()
print("Hotel Descrescente FOR")
for i in range(20,0,-1):
    if i == 13:
        continue
    else:
        print(f"Andar reverso:{i}")

print()
print("Hotel Descrescente While")
andar_reverso = 20
while andar_reverso >=1:
    if andar_reverso != 13:
        print(andar_reverso)
    andar_reverso -=1




