num = float(input('Insira um número: '))
soma = 0
digitados = 0
while num != -999:
    soma += num
    digitados += 1
    print(
        f'A soma dos valores ficou: {soma},\n A quantidade digitada: {digitados}\n Digite-999 para sair')
    num = float(input('Insira um número: \n'))
