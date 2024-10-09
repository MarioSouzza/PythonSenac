# Exemplo
from datetime import date
print("Os modelos disponiveis são: ")


class Carro:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.data_atual = date
        self.data_atual = self.data_atual.year

    def exibir(self):
        print(
            f"O modelo é {self.modelo} do ano {self.ano} no valor R$ {self.valor:.3f}")


carro1 = Carro("Kicks", 2023, 100.000)
carro2 = Carro("Versa", 2020, 80.000)
carro1.exibir()
carro2.exibir()

print("-"*45)

# Herança - é uma classe que herda as caracteristicas da classe original.


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} diz: barulho!')


class Cachorro(Animal):
    pass


class Gato(Animal):
    pass


dog = Cachorro("Rex")
cat = Gato("Tom")

dog.emitir_som()
cat.emitir_som()
print("-"*45)


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def profissao(self):
        print(f'{self.nome} é bastante profissional.')


class Medico(Pessoa):
    pass


class Advogado(Pessoa):
    pass


doc = Medico("Maria Clara")
lower = Advogado("Stephanie")

doc.profissao()
lower.profissao()

print("-"*45)

# Polimorfismo - Permite que métodos com o mesmo nome possam ser implementados de maneiras diferentes.


class Animal:
    def fazer_som(self):
        pass  # Método abstrato


class Cachorro (Animal):
    def fazer_som(self):
        print("Au,Au...")


class Gato (Animal):
    def fazer_som(self):
        print("Miau...")


animais = [Cachorro(), Gato()]

for animal in animais:
    animal.fazer_som()

print("-"*45)


class Barulho:
    def som(self):
        pass


class Explosao (Barulho):
    def som(self):
        print("BOOOOOMMMMM")


class Silencio (Barulho):
    def som(self):
        print("SHHHHHHIIII")


sons = [Explosao(), Silencio()]
for barulho in sons:
    barulho.som()

print("-"*45)

# Encapsulamento e propriedades (getters e seltters)

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    @property #getters
    def nome (self):
        return self.__nome

    @nome.setter #seltters
    def nome (self, novo_nome):
        if isinstance (novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("Nome Inválido.")
# Uso da classe
pessoa = Pessoa("Alice")
print(pessoa.nome)
pessoa.nome = "Bob"
print(pessoa.nome)
pessoa.nome = "Mário"
print(pessoa.nome)
pessoa.nome = ""
print("-"*45)

# Atributos protegidos
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome # atributo privado
        self.__idade = idade # atributo privado
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, Idade: {self.__idade}")
pessoa = Pessoa("Alice", 30)

# Tentativa de acessar o atributo privado__nome
print(pessoa.__nome)