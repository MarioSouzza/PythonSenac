# # declarando uma lista vazia em Python.

# lista1 = []

# lista1 = [1, "2", 3]  # CRIANDO UMA LISTA
# print(type(lista1), lista1)

# # declaração explícita de uma lista
lista2 = list((1, "2", 3))
# print(type(lista2), lista2)

# # declaração implícita
lista3 = ["C", 4.65, True, "True", "Vamos aprender",["outra", "lista", "interna"], lista2]
print(lista3)

# lista4 = ["primeiro", "segundo", "terceiro"]
print(lista4)

# acessando um elemento dentro da lista
print(lista3)
print(lista3[6][1])  # acessando a lsita dentro da lista

# Fatiando listas
# nomeDalista[start:stop:step]
# start - indice
# stop - elemento
# step - passo

# execute um print por vez!!

print(lista3)
print(lista3[2:6:2])
print(lista3[2:7])
print(lista3[:3])
print(lista3[::-1])
print(len(lista3))
