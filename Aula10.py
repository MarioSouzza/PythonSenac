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