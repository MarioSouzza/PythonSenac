# Exemplo 01
def saudacao():
    print("Olá, seja bem vindo")
saudacao()
print()
# Exemplo 02
def saudacao(nome): # 'nome' é um parâmetro
    print(f"Olá, {nome}!")
saudacao("Carlos") # 'Carlos' é um argumento

print()
# Exemplo 03
def somar ( a, b ): # mais de um parâmetro
    return a + b
resultado = somar (10,20) # mais de um argumento
print(resultado) 

print()
# Exemplo de multiplos Retornos
def checar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"


print (checar_numero(10))
print()
# Escopo de variáveis:
# Escopo Local: Variáveis definidas dentro de uma função só existem dentro dela.
# Escopo global: Variáveis definidas em qualquer função podem ser acessadas em qualquer parte do código.
global_var = 100
def exemplo_escopo():
    local_var = "Estou dentro da função"
    print(local_var)
    print(global_var)
exemplo_escopo()
"""print(local_var) # Ficou fora da função, logo irá crashar o programa."""
print()
# Argumentos Posicionais:
# Os argumentos são passados para função na mesma ordem dos parâmetros.
def exibir_nome_idade(nome, idade):
    print(f'nome: {nome}, idade: {idade}')
exibir_nome_idade("Carlos", 30) 
print()

def txt (frase):
 tamanho = len(frase)
 print("*"*40)
 print("*"*int((39-tamanho)*0.5),frase,"*"*int((39-tamanho)*0.5))
 print("*"*40)
frase = (input("Digite uma frase: "))
txt(frase)
