salario = float(input('Insira o valor do salário R$'))
vendas = float(input('Insira o valor das vendas R$'))
comissao = vendas*0.04
print(f'''
    Salário BrutoR${salario:.2f}
    Comissão R${comissao:.2f}
    Salario + Comissão R${salario+comissao:.2f}
''')
