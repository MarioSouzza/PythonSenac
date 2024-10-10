# Avaliar a possibilidade de empretimo.

salario = (float(input('Informe o seu salário: ')))
emprestimo = (float(input('Informe o valor do emprestimo: ')))

if (emprestimo <= salario*0.5):
    print(f'Sua solicitação de emprestimo foi aprovado no valor de R$ {emprestimo:.2f}')
elif (emprestimo <= salario*0.75):
    print(f'Sua solicitação de emprestimo no valor de R$ {emprestimo:.2f} está em analise')
else:
    print(f'Sua solicitação de emprestimo no valor de R$ {emprestimo:.2f} foi negada')
