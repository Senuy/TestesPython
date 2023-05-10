c = input('Qual combustível deseja abastecer (A-alcool / G-gasolina):').upper()
if c == 'A':
    litros = float(input('Insira quantos Litros de Álcool deseja abastecer:'))
    a = 1.90
    if litros <= 20:
        valor = (a*(0.97*litros))
        print(
            f'Valor a pagar R${a*litros:.2f}, valor com desconto R${valor:.2f}')
    else:
        valor = (a*(0.95*litros))
        print(
            f'Valor a pagar R${a*litros:.2f}, valor com desconto R${valor:.2f}')
elif c == 'G':
    litros = float(
        input('Insira quantos Litros de Gasolina deseja abastecer:'))
    a = 1.90
    if litros <= 20:
        valor = (a*(0.96*litros))
        print(
            f'Valor a pagar R${a*litros:.2f}, valor com desconto R${valor:.2f}')
    else:
        valor = (a*(0.94*litros))
        print(
            f'Valor a pagar R${a*litros:.2f}, valor com desconto R${valor:.2f}')
else:
    print('Caracter inválido')
