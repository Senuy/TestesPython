num = float(input('Insira um número: '))
soma = 0
while num != -999:
    soma += num
    print(f'A soma dos valores ficou {soma}, Digite-999 para sair')
    num = float(input('Insira um número: \n'))
