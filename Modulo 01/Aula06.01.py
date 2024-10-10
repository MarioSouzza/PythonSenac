# Exemplo

# Neste caso, a variável letra assume cada caracter da string palavra.
palavra = "Python"
for letra in palavra:
    print(letra)

palavra = "Python"
for i in palavra:
    print(f"A letra {i} tem indice {palavra.index(i)}")

# Você pode usar um laço for para percorrer a frase e verificar se cada caractere é uma vogal.
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
print(f'Há {contador} vogais na frase.')

# Você pode usar um laço for para percorrer a frase e verificar se cada caractere é uma consoante.
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in frase:
    if letra not in vogais:
        contador += 1
print(f'Há {contador} consoantes na frase.')
