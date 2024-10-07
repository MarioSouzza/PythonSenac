# Exemplo
from datetime import date



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Maria", 30)
print(pessoa1.nome) # Saída: Maria
print(pessoa1.idade) # Saída: 30

pessoa2 = Pessoa("Chico", 40)
print(pessoa2.nome) # Saída: Chico
print(pessoa2.idade) # Saída: 40

pessoa3 = Pessoa("Carlos", 30)
print(pessoa3.nome) # Saída: Carlos
print(pessoa3.idade) # Saída: 30
print("***********************************")
# Exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar (self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
pessoa1 = Pessoa('Maria', 30)
print(pessoa1.nome) # Saída: Maria
print(pessoa1.idade) # Saída: 30
pessoa1.apresentar()
print("***********************************")




# Exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.data_atual = date.today()
        self.data_atual = self.data_atual.year
    def apresentar (self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade}')
    def exibir (self):
        nascimento = self.data_atual - self.idade
        print(f'{self.nome} nasceu em { nascimento}')
pessoa1 = Pessoa('Maria', 30)
# print(pessoa1.nome) # Saída: Maria
# print(pessoa1.idade) # Saída: 30
# print(pessoa1.nascimento) # Saída: 1994
pessoa1.apresentar()
pessoa1.exibir()
print("***********************************")
