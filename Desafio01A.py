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
    conta ['saldo'] = float(input("Informe o saldo inicial: "))
    print("Conta bancária criada com sucesso")
criar_conta_bancaria()