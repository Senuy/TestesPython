num = float(input('Insira um número: '))
soma = 0
impar = 0
while num != -999:
    soma += num
    if num % 2 != 0:
        impar += 1
    print(
        f'A soma dos valores ficou: {soma},\n A impar quantidade digitada: {impar}\n Digite-999 para sair')
    num = float(input('Insira um número: \n'))
