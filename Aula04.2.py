# lista1 = [1, '2', 3]
# lista2 = ["C", 4.65, True, "True","Vamos aprender", ["outra", "lista", "interna"]]

# texto = "Sera que vai funcionar? "
# print(texto.split(" "))

# # contar o nº de elementos dentro da lista
# tupla = (1, 2, 3, 2, 3, 3,)
# print(tupla.count(2))
# print(tupla.count(4))


frutas = ['maçã', 'banana', 'laranja']
print(frutas)

frutas.append('uva')
print(frutas)

frutas.remove('banana')
print(frutas)

print(frutas[1])

frutas.reverse()
print(frutas)

cores = ('vermelho', 'verde', 'azul')
print(cores[0],cores[-1])

# cores[1] = 'amarelo' #TypeError:O objeto 'tuple' não suporta atribuição de itens

outrascores = ('amarelo', 'roxo')
print(cores + outrascores)

cor1 = cores[0]
cor2 = cores[1]
cor3 = cores[2]
print(cor1)
print(cor2)
print(cor3)