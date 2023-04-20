roupas = float(input('Insira o valor pago nas roupas R$'))
if roupas < 50:
    print(f'''
            O valor de Revenda da peça será de R${roupas*1.45:.2f}
    ''')
else:
    print(f'''
            O valor de Revenda da peça será de R${roupas*1.30:.2f}
    ''')
