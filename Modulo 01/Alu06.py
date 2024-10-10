# A sintaxe básica de um for

# Exemplo:
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

#  A função range() gera uma sequência de números, que é frequentemente utilizada para laços for.:


# Gera uma sequência de 0 a 4
for i in range(5):
    print(i)

#  Exemplo
soma = 0
for i in range(1, 11):  # Gera uma sequência de 1 a 10
    soma += i
print('A Soma de 1 a 10 é:', soma)

# Neste exemplo, o laço for é usado para somar os números de 1 a 10..
soma = 0
for i in range(1, 11):
    soma = i + soma
    print(soma, 'Carlos')

for i in range(1, 11):
    soma = i + soma
    a = 0
    b = 10
    print(soma)
    print(a)
