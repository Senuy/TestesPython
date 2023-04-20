conta = int(input('Insira o número da conta: '))
saldo = float(input('Insira o saldo da conta: '))
debito = float(input('Insira o valor do débito: '))
credito = float(input('Insira o valor do crédito: '))

saldoAtual = saldo - debito + credito

if saldoAtual >= 0:
    print(f'Saldo Positivo no valor de R${saldoAtual:.2f}')
else:
    print(f'Saldo Negativo no valor de R${saldoAtual:.2f}')
