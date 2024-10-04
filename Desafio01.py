# Crie um progarama que perimita ao usuário realizar as seguintes operações bancárias:
# 1 - Criar conta
# 2 - Verificar Saldo
# 3 - Depositar dinheiro
# 4 - Sacar Dinheiro
# 5 - Encerrar o atendimento

# O programa deve armezenar as informações da conta bancária do usuário em um dicionário.
# O programa deve exibir um menu para o usuário escolher a operação que deseja realizar e, em seguida, executar a operação escolhida.
# Ao depositar dinheiro, o programa deve atualizar o saldo da conta bancária adicionando o valor depositado ao saldo atual.
# Ao sacar dinheiro, o programa deve verificar se o valor a ser sacado é menor ou igual ao saldo atual da conta bancáriae, em caso afirmativo, atualizar o saldo da conta bancária subtraindo o valor sacado do saldo atual.
# Se o valor a ser sacado for maior que o saldo atual da conta bancária, o programa deve exibir uma mensagem infromado que não há saldo sificiente na conta bancária para realizar a operação.

# def criar_conta_bancaria():
#     conta = {}
# # Solicita as informações do usuário
#     conta ['nome'] = input("Informe o nome do correntista: ")
#     conta ['agencia'] = input("Informe a sua agência: ")
#     conta ['conta_corrente'] = input("Informe a sua conta corrente: ")
#     conta ['saldo'] = float(input("Informe o saldo inicial: "))
#     print("Conta bancária criada com sucesso")
# # correntista = {nome:, agencia:,conta_corrente: }
#     return conta

def menu():
    print("\nEscolha uma operação:")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

def main():
    conta_bancaria = {
        "titular": "João da Silva",
        "saldo": 1000.0  # Saldo inicial
    }

    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '1':
            print(f"Saldo atual: R$ {conta_bancaria['saldo']:.2f}")
        
        elif escolha == '2':
            try:
                valor_deposito = float(input("Digite o valor a depositar: R$ "))
                if valor_deposito <= 0:
                    print("Erro: O valor do depósito deve ser positivo.")
                else:
                    conta_bancaria['saldo'] += valor_deposito
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
            except ValueError:
                print("Erro: Por favor, digite um valor válido.")

        elif escolha == '3':
            try:
                valor_saque = float(input("Digite o valor a sacar: R$ "))
                if valor_saque <= 0:
                    print("Erro: O valor do saque deve ser positivo.")
                elif valor_saque > conta_bancaria['saldo']:
                    print("Erro: Saldo insuficiente na conta bancária para realizar a operação.")
                else:
                    conta_bancaria['saldo'] -= valor_saque
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            except ValueError:
                print("Erro: Por favor, digite um valor válido.")

        elif escolha == '4':
            print("Saindo do programa.")
            break

        else:
            print("Erro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()