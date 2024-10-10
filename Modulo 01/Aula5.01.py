# Concatenando Strings
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

# Acessando caracteres individuais em uma string
mensagem = "Hello, world!"
primeiro_caracter = mensagem[0]
ultimo_caracter = mensagem[-1]
print(primeiro_caracter)
print(ultimo_caracter)

# Encontrado o comprimento de uma string:
mensagem = "Hello, world!"
comprimento = len(mensagem)
print(comprimento)

# Convertendo um string para letras maiúsculas ou minúsculas
mensagem = "Hello, world!"
maiuscula = mensagem.upper() # Converte todo o texto para maiúscula
minuscula = mensagem.lower() # Converte todo o texto para minúscula
print(maiuscula)
print(minuscula)

# dividindo um string em substrings com base em um delimitador.
mensagem = "Hello, world!"
palavras = mensagem.split(",")
print(palavras)

#verificando se uma substring está presente em uma string
mensagem = "Hello, world!"
if "world" in mensagem:
    print("A substring 'world' está presente na mensagem ")

# Substituindo caracteres em uma string.
mensagem = "Hello, world!"
nova_mensagem = mensagem.replace("world", "python")
print(nova_mensagem)

# mensagem = "Hello, world!"
# primeira_linha = mensagem[2:]
# H = mensagem[0]
# E = mensagem[1]
# maiusculo = E.upper()
# minusculo = H.lower()
# juncao = minusculo + maiusculo + primeira_linha
# print(juncao)

# Removendo espaços em branco de uma string.
frase = '  Hello, World!   '
print(frase)
sem_espacos = frase.strip() #Retorna "Hello, World!"
print(sem_espacos)

# Exercicio
texto = "Estrutura de dados em Python"
m = texto.upper()
print(m)
texto = "Estruturas de dados em Python"
localizar = texto.find("dados")
print(localizar)

texto = "Estrutura de dados em Python"
novo_texto = texto.replace("Python", "Java")
print(novo_texto)

texto = "Estrutura de dados em Python"
texto_dividido = texto.split(" ")
print(texto_dividido)