import math
conta = float(input('Insira o valor da conta R$'))
total = conta/3
decimal, inteiro = math.modf(total)
print(f'Thiago pagará R$ {inteiro:.2f}')
print(f'Joceyr pagará R$ {inteiro:.2f}')
print(f'Alexandre parará R${(decimal*3)+inteiro:.2f}')
