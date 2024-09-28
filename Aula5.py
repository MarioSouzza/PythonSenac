# declarando dicionários
dic = {}
print(type(dic))
dic_pernambuco = {'Sport': 41, 'Santa Cruz': 29, 'Nautico': 21}
print(dic_pernambuco)

# adicionando um elemento no dicionário (chave : valor)
# onde a chave é 'Salgeiro' e o valor é 1
#  note que a chave é passada dentro de colchetes, após o nome do dicionário.
dic_pernambuco['Salgueiro'] = 1
print(dic_pernambuco)

# Buscando valor com base  na chave
qnt_titulos = dic_pernambuco.get('Sport')
print(qnt_titulos)
print('O Sport tem', qnt_titulos, 'titulos')

# Remover um elemnto com base na chave
del dic_pernambuco['Salgueiro']
print(dic_pernambuco)

# Remover a chave e retorna seu valor
valor = dic_pernambuco.pop('Nautico')
print('O valor retornado de chave é: ', valor)
print(dic_pernambuco)

# Verificar se uma chave existe no dicionário
print('Santa Cruz' in dic_pernambuco)

# Pegar todas as chaves do dicionário
print(dic_pernambuco.keys())

# Pegar todos os valores do dicionário
teste = dic_pernambuco.values()
print(teste)

dic_pernambuco = {'Sport': 41, 'Santa Cruz': 29, 'Nautico': 21}
converter = list(dic_pernambuco)
print(converter[0])

dic_paulista = {"Corinthias": 29, 'Santos': 22, "Palmeiras": 22}

#  Revovendo e Retornando último elemento
print(dic_paulista.popitem())
print(dic_paulista)

# Mesclar dois dicionários
dic_paulista.update(dic_paulista)
print(dic_pernambuco)

# Convertendo um dicionário em uma lista
print(list(dic_pernambuco))
print(list(dic_pernambuco.values()))

# Exercicio
aluno = {'Nome': 'Mário', 'Idade': 44, 'Nota': 7.0}
aluno['Curso'] = 'Ciência da Computação'
print(aluno)
nome = aluno.get('Nome')
print(nome)
del aluno['Nota']
print(aluno)

print("Idade" in aluno)