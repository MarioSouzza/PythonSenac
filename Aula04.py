# metodos de listas
# append - acrescenta elementos a lista
lista1 = []

lista1.append('python')
lista1.append('java')
lista1.append('php')
lista1.append('C#')
lista1.append('1,2,3')

print(lista1)

# localiza a posição de um elemento 
print(lista1.index('php'))

# insert - insere elementos em uma posição específica
lista1.insert(2, "C++")
print(lista1)

# substitui o elemento
lista1[2] = '50000'
print(lista1)

# remove - remove um elemento pelo seu valor
lista1.remove('50000')
print(lista1)

# remover um elemento pelo seu indice
del (lista1[0])
print(lista1)

# invertendo uma lista
lista1.reverse()
print("lista invertida -", lista1)


lista2 = ['c', 'a', 'e', 'x', 't']
# ordenando uma lista
lista2.sort()
print("lista ordenada - ", lista2)
