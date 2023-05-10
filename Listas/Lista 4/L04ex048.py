valor = float(input('Insira o valor da compra: '))
pagamento = int(input('''
1- À vista em dinheiro ou pix recebe 10 de desconto
2- À vista no cartão de crédito, recebe 5 de desconto
3- Em duas vezes, preço normal de etiqueta sem juros
4- Em três vezes, preço normal de etiqueta mais juros de 10
'''))
if pagamento == 1:
    print(
        f'Para pagamento a vista ou pix o valor com desconto fica {valor*0.9:.2f}')
elif pagamento == 2:
    print(
        f'Para pagamento a vista no crédito o valor com desconto fica {valor*0.95:.2f}')
elif pagamento == 3:
    print(f'Para pagamento em 2x o valor fica{valor:.2f}')
elif pagamento == 4:
    print(
        f'Para pagamento dem 3x fica com um juros de 10% o valor fica{valor*1.1:.2f}')
