cardapio = {
    '100': 11.20,
    '101': 8.30,
    '102': 11.50,
    '103': 16.20,
    '201': 6.00,
    '202': 7.5,
    '203': 4.7
}
sanduiche = input('''
Insira o código do Sanduíche
Cachorro Quente - 100 - R$ 11,20
OvoSimples------- 101 - R$ 8,30
Baurucom Ovo----- 102 - R$ 11,50
Hambúrguer--------103 - R$ 16,20
''')
bebida = input('''
Insira o código da bebida
Refrigerante----- 201 - R$ 6.00
Suco------------- 202 - R$ 7,50
Água Mineral----- 203 - R$ 4,70
''')
if sanduiche in cardapio and bebida in cardapio:
    valorSanduiche = cardapio[sanduiche]
    valorBebida = cardapio[bebida]
    total = valorSanduiche+valorBebida
    print(f'Valor a pagar R$ {total:.2f}')
else:
    print('Código inválido')
