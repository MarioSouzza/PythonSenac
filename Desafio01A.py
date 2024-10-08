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

def criar_conta_bancaria():
    conta = {}
    conta ['nome'] = input('Informe o nome do correntista: ').strip()
    conta ['agencia'] = float(input('Informe a agencia: '))
    conta ['conta'] = float(input('Informe a conta: '))
    print("Conta bancária criada com sucesso")
# Valida o saldo inicial
    while True:
        try:
            saldo = float(input("Informe o saldo inicial: "))
            if saldo < 0:
                print("O saldo inicial não pode ser negativo. Tente novamente.")
            else:
                conta['saldo'] = saldo
                break
        except ValueError:
            print("Por favor, informe um número válido para o saldo.")

    print("Conta bancária criada com sucesso!")
    
    return conta

def verificar_saldo(conta):
    print(f"O saldo atual da conta é R$ {conta['saldo']:.2f}")

def depositar(conta):
    while True:
        try:
            valor = float(input("Informe o valor a ser depositado: "))
            if valor <= 0:
                print("O valor do depósito deve ser positivo. Tente novamente.")
            else:
                conta['saldo'] += valor
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                break
        except ValueError:
            print("Por favor, informe um número válido para o valor do depósito.")

def sacar(conta):
    while True:
        try:
            valor = float(input("Informe o valor a ser sacado: "))
            if valor <= 0:
                print("O valor do saque deve ser positivo. Tente novamente.")
            elif valor > conta['saldo']:
                print("Saldo insuficiente para realizar o saque.")
            else:
                conta['saldo'] -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                break
        except ValueError:
            print("Por favor, informe um número válido para o valor do saque.")

def main():
    conta = None  # Inicializa a variável da conta como None

    while True:
        print("\n--- Menu ---")
        print("1. Criar Conta")
        print("2. Verificar Saldo")
        print("3. Depositar Dinheiro")
        print("4. Sacar Dinheiro")
        print("5. Encerrar Atendimento")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            conta = criar_conta_bancaria()
        elif opcao == '2':
            if conta:
                verificar_saldo(conta)
            else:
                print("Você precisa criar uma conta primeiro.")
        elif opcao == '3':
            if conta:
                depositar(conta)
            else:
                print("Você precisa criar uma conta primeiro.")
        elif opcao == '4':
            if conta:
                sacar(conta)
            else:
                print("Você precisa criar uma conta primeiro.")
        elif opcao == '5':
            print("Atendimento encerrado. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()