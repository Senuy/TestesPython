n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
op = input('Qual Operação deseja fazer digite (+,-,*./):')

if op == '+':
    resultado = n1+n2
    print('Operação soma selecionado')
elif op == '-':
    resultado = n1-n2
    print('Operação subtraçãp selecionado')
elif op == '*':
    resultado = n1*n2
    print('Operação multiplicação selecionado')
elif op == '/':
    resultado = n1 / n2
    print('Operaçào Divisão selecionado')
else:
    print('Caracater inválido')
    exit()

if resultado % 2 == 0:
    print(f'O número {resultado:.2f} do resultado é par')
else:
    print(f'O número {resultado:.2f} do resultado é impar')
if resultado > 0:
    print(f'O número {resultado:.2f} do resultado é positivo')
else:
    print(f'O número {resultado:.2f} do resultado é negativo')
if resultado == int(resultado):
    print(f'O número {resultado:.2f} do resultado é inteiro')
else:
    print(f'O número {resultado:.2f} do resultado é decimal')
