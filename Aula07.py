# #  A estrututa básica de um laço while é:
# #  Bloco de código a ser execultado.
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
# print()
# # Neste exemplo, a variável contador é incrementada a cada intereção.
# #  Quando o valor de contador é maior que 5.
# #  A condição do while deixa de ser verdadeiro, e o laço é encerrado.

# # Exemplo
while True:
    nome = input("Digite seu nome (ou 'sair' para parar) :").upper()
    if nome == "SAIR":
        break
    print(f"Olá, {nome}!")
print()
# Exemplo
numero_secreto = 7
tentativa = None
while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
print("Parabéns! VocÊ adinvinhou o número. ")
print()
# O usuário continuará tentando adivinhar o número até que acerte.
#   Neste caso, o laço while permanece ativo enquanto tentativa for diferente de numero_secreto.

# # Exemplo
contagem = 10
while contagem > 0:
    print(contagem)
    contagem -= 1
print('Feliz Ano Novo!')
print()
# Exemplo
import random
numero_secreto = random.randint(1,20)
tentativa = 0
print("Digite um número entre 1 e 20.")
while True:
    palpite = int(input("Dê seu palpite: "))
    tentativa +=1
    if palpite < numero_secreto:
        print("Seu palpite é menor que o número secreto.")
    elif palpite > numero_secreto:
        print("Seu palpite é maior que o número secreto.")
    else:
        print("Seu palpite é igual ao número secreto.")
        break
# print()
#  Crie um programa que continue pedindo para o usuário digitar dois números e a operação desejada(+,-,*,/).
#  O laço deve parar quando o usuário digitar "sair".:

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+,-,*,/) ou 'sair' para parar: ").lower()
    if operacao == 'sair':
        break
    if operacao == "+":
        print(f'Resultado: {num1 + num2}')
    elif operacao == "-":
        print(f'Resultado: {num1 - num2}')
    elif operacao == "*":
        print(f'Resultado: {num1 * num2}')
    elif operacao == "/":
        if num2 != 0:
            print(f'Resultado: {num1 / num2}')
        else:
            print(f'Erro: Divisão por zero.')
    else:
        print("Operação invalida")
# print()
# Escreva um laço while para imprimir os números de 1 a 10.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
print()
# Escreva um progarama que peça ao usuário para digitar uma senha e continue pedindo até que ele acerte a senha correta. Que é 1234.
senha_correta = 1234
tentativas = 0
max_tentativas = 3
while True:
    senha = int(input("Digite a senha de 04 digitos: "))
    
    if senha == senha_correta:
        print(f"A senha: { senha} esta correta!!!")
        break
    else:
        print(f'A senha incorreta. Você tem {max_tentativas - tentativas} tentativas restantes.')
        tentativas += 1
        if tentativas == max_tentativas:
            print("Número máximo de tentativas atingido. Acesso negado.")

