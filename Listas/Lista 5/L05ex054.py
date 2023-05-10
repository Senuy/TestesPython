num = int(input('Insira um número: '))
soma = 0
cinquenta = 0
while num != 0:
    soma += num
    if num == 50:
        cinquenta += 1
    print(
        f'A soma dos valores ficou: {soma},\n A quantidade de "50" digitada: {cinquenta}\n Digite 0 para sair')
    num = int(input('Insira um número: \n'))
