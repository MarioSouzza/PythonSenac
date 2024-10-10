# Crie um programa que exiba um menu interativo com as seguintes apções:
# 1 - Adicionar item
# 2 - Remover item
# 3 - Exibir lista
# 4 - Sair

#  O programa deve permitir que o usuário gerencie uma lista de compras (compras[]).
#  Cada opção de realizar a ação correspondente até que o usuário escolha "4" para sair.

print("*****Menu*****")
print("1 - Adicionar item")
print("2 - Remover item")
print("3 - Exibir lista")
print("4 - Sair")

# Adicionar item compras
compras = []
item = input("Digite o nome do item a ser adicionado: ").lower()
compras.append(item)
print(f"Item '{item}' adicionado à lista.")
print()
# Remover item compras
item = input("Digite o nome do item a ser removido: ").lower()
if item in compras:
    compras.remove(item)
    print(f'Item {item} foi removido da lista')
else:
    print(f"Item informado não localizado na lista.")
print()
# Exibir lista de compras
if compras:
    print("n\lista de compras: ")
    for i, item in enumerate(compras, 1):
        print(f'{i}. {item}')
else:
    print("A lista está vazia.")
# Sair do programa.
while True:
    opcao = int(input("Escolha uma opção entre (1-4): "))
    if opcao =="1"
        adicionar item 
# print()

# for i in range(1,11):
#     if i == 5:
#         continue # Pula a interação quando i é igual a 5
#     print(i)
# print()

