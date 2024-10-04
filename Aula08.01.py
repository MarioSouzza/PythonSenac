# Funções
# Sintaxe Básica
def nome_da_funcao (parametros):
    # bloco de codigo
    return resultado

# Exemplo:

def saudacao():
    print("Olá, bem vindo(a) à aula de funções em Python!")

# Para "chamar" a função e execultar seu código:
saudacao()

# Exemplo:
def saudacao(nome):
    print(f"Olá,{nome}!")
saudacao('Carlos')
saudacao('Mário')

# Exemplo
def somar (a,b,c): # mais de um parâmetro
    return a + b + c

resultado = somar(10,20,5)
print(resultado) #Saída: 35

# Exemplo
def saudacao (nome = "aluno"):
    print(f"Olá, {nome}!")
saudacao()
saudacao("Carlos")

# Exemplo de múltiplos retornos:

def checar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
print(checar_numero(5))

def teste():
    valor = int(input("digite um número: "))
    if valor > 0:
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Zero"
print(teste())

# global_var = 100
# def exemplo_escopo():
#     local_var = "Estou dentro da função"
#     print(local_var)
#     print(global_var)
# exemplo_escopo()
# print(local_var)

# Argumentos posicionais:
# Os argumentos são passados para função na mesma ordem do parâmetros.

def exibir_nome_idade(nome, idade):
    print(f'Nome: {nome}, Idade: {idade}')
exibir_nome_idade("Carlos", 30)

def exibir_nome_idade(nome, idade):
    print(f'Nome: {nome}, Idade: {idade}')
exibir_nome_idade(idade = 25, nome = "Karla")

# Argumentos Arbitrários (*args e **kwargs):
# *args: Recebe múltiplos argumentos como uma tupla.
def somar_todos(*args):
    return sum(args)
print(somar_todos(1,2,3,4,5)) #Saída: 15

#**kwargs: Recebe mútiplos argumentos nomeados como im dicionário.
def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
exibir_detalhes(nome = "Carlos", Idade = 30, cidade = "São Paulo", telefone = 99999.9999)

# Função para Encontrar a soma dos números pares usando while:
def soma_pares(numeros):
    soma = 0
    i = 0
    while i < len (numeros):
        if numeros [i] % 2 == 0:
            soma += numeros [i]
        i += 1
    return soma
print(soma_pares([1,2,3,4,5,6])) #Saída: 12