# Imprima os números de 1 a 10 usando um laço for.
soma = 0
for i in range(0, 10):
    soma = i + 1
    print(soma)
print()

# Soma todos os números de 1 a 50 e imprima o resultado.
soma = 0
for i in range(1, 50):
    soma = i + soma
    print(soma)
print()

# Solicta um número e exiba uma tabuada.
numero = int(input("Digite um número para ver a tabuada: "))
print(f'Tabuada do {numero}:')
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print()

#  Use um laço para imprir todos os números pares de 1 a 20.
for i in range(0, 20+1, 2):
    print(i)
print()

# Use um for para contar quantos caracteres existem em uma frase (desconsidere espaços).
frase = ("Python é divertido!")
espaco = " "
contador = 0
for letra in frase:
    if letra not in espaco:
        contador += 1
print(f'Há {contador} caracteres na frase.')
print()

# Use um laço for para criar uma nova lista com elementos na ordem inversa.
numeros = [1, 2, 3, 4, 5]
numeros_inversos = []
for i in range(len(numeros) - 1, -1, -1):
    numeros_inversos.append(numeros[i])
print("Lista original:", numeros)
print("Lista invertida:", numeros_inversos)

# Receba um número inteiro n do usuário e imprima todos os números primos menores que n.
def encontrar_primos(n):
    primos = []
    for num in range(2,n):
        eh_primo = True
        for 