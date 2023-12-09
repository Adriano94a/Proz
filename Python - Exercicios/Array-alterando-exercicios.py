lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

print(lista_produtos.index('batons'))
print(lista_produtos.index('loções'))
lista_produtos.pop()
lista_produtos[1], lista_produtos[4] = 'Rimel','cremes hidratantes'
print(lista_produtos)
