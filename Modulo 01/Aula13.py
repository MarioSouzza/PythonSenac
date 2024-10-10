# API

"""" Métodos HTTP Comuns"""
# GET: Obtém dados de um servidor.
# POST: Envia dados para um servidor.
# PUT: Atualiza dados no servidor.
# DELETE: Remove dados no servidor.
# request: Para fazer requisições HTTP e consumir dados de APIs
# opnpyxl: Para manipular arquivos em excel (planilhas) com python.
# pip: gerenciador de pacotes no python.

# No terminal: pip install requests openpyxl

import openpyxl
import requests

# URL da API
url = "https://jsonplaceholder.typicode.com/users"

# Fzendo a requisição GET para a API
response = requests.get(url)

# Verificando o status da requisição

if response.status_code == 200:
    users = response.json()  # Convertendo a resposta em formato JSON
    print('-'*50)
    for user in users:
        # if user['name'] =="Leanne Graham":
        print(
            f"Nome: {user['name']}, E-mail: {user['email']}, Telefone: {user['phone']}")
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")
print('-'*50)


# URL da API
url = "https://jsonplaceholder.typicode.com/users"

# Fazendo a requisição GET para a API
response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    # Criando um novo arquivo em Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Adicionando os cabeçalhos
    sheet.append(["ID", "Nome", "Email", "Empresa"])

    # Adicionando dados da API ao Excel
    for user in users:
        sheet.append([user['id'], user['name'],
                     user['email'], user['company']['name']])

    # Salvando o arquivo
    workbook.save('usarios_api.xlsx')
    print("Dados salvos no arquivo 'usuarios_api.xlsx'.")
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")
print('-'*50)

# URL da API
url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

# Fazendo a requisição GET para a API
response = requests.get(url)
if response.status_code == 200:
    loterias = response.json()
    print(loterias)
    # Criando um novo arquivo em Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Adicionando os cabeçalhos
    sheet.append(["Concurso", "local", "Estados Premiados"])

    # Adicionando dados da API ao Excel
    for loteria in loterias:
        sheet.append(
            f"{loteria['concurso']}, {loteria['local']}, {loteria['estadosPremiados']}")

    # Salvando o arquivo
    workbook.save('loteria_api.xlsx')
    print("Dados salvos no arquivo 'usuarios_api.xlsx'.")
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")
print('-'*50)
