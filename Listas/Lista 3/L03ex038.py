prato = float(
    input('Coloque seu prato por cima da balança para que seja calculado o valor: '))
valorPrato = (prato/1000)*59.00
print(f'''
O peso em Gramas ficou {prato/1000:.3f}kg no valor de R$59.00/Kg
fica num total de R${valorPrato:.2f}
''')
