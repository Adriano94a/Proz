lista_frutas = ['Maça', 'Banana', 'Pera']
print(lista_frutas)
print()
lista_frutas[0] = 'Melancia'
print(lista_frutas)


#podemos acessar mais de um item por vez
print()
lista_frutas[1], lista_frutas[2] = 'Morango', 'Abacaxi'
print(lista_frutas)

#podemos atribuir duas vezes o mesmo item
print()
lista_frutas[1] = lista_frutas[0]
print(lista_frutas)
#função append (anexar)
print()
lista_frutas.append('Ameixa')
print(lista_frutas)

print()
#função pop (remover)
lista_frutas.pop() #Quando não inserimos nada no () o mesmo remove o ultimo item.
print(lista_frutas)