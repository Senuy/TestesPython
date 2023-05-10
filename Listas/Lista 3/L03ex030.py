peso = float(input('Insira a quantidadem em Kg de peixes pescados: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f''' 
            Quantidade Pescada em Kg{peso:.2f}
            Quantidade ultrapassando o regulamento: Kg{excesso:.2f}
            Valor da multa a pagar R${multa:.2f}
    ''')
else:
    print(
        f'Quantidade pescada não ultrapassou o limite de  50Kg,\nQuantidade Pescada Kg{peso:.2f}')
