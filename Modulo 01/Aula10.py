# Execeções
"""try:
    # Código que pode causar uma exceção
except TipodaExceção:
    # Código que será execultado se ocorrer a exceção
else:
    # Código que será execultado se nehuma exceção ocorrer"""

# Exemplo
print("--------------------------------")
try:
   resultado = 10/0
   print(resultado)
except ZeroDivisionError:
   print("Erro: Divisão por zero não é permitida.")
print("--------------------------------")
# Exemplo
try:
   resultado = 10/2
except ZeroDivisionError:
   print("Erro: Divisão por zero não é permitida. ")
else:
   print(f'O resultado é {resultado}')
print("--------------------------------")
"""Exemplo
try:
    # Código que pode causar uma exceção
except TipoDaExceção:
    # Código que será execultado se ocorrer a execeção
finally:
    # Código será independente do erro"""
try:
   arquivo = open('dados.txt','r')
   conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não econtrado.")
finally:
   print('Operação finalizada.')
print("--------------------------------")
try:
   num = int(input("Digite um número: "))
   resultado = 100 / num
except ValueError:
   print("Erro: Você deve digitar um número inteiro.")
except ZeroDivisionError:
   print("Erro: divisão por  zero não é permitida.")
else:
   print(f'o resultado é {resultado}')
finally:
   print("obrigado por usar o programa.")
print("--------------------------------")

def verifica_idade(idade):
   if idade < 18:
      raise ValueError ("Idade deve ser maior ou igual a 18.")
   else:
      print("Entrada permitida.")
try:
   verifica_idade(18)
except ValueError as e:
   print(e)
print("--------------------------------")

# Exemplo
class SaldoInsufucienteError(Exception):
   """Exceção levantada quando o saldo é insufuceinte para realizar uma transação."""
   pass
def sacar (valor, saldo):
   if valor > saldo:
      raise SaldoInsufucienteError("Saldo insuficiente para sacar o valor solicitado.")
   saldo -= valor
   return saldo
try:
   saldo_atual = sacar (1500, 1000)
except SaldoInsufucienteError as e:
    print(e)

