paes = int(input('Insira a quantidade de paes vendidos: '))
broas = int(input('Insira a quantidade de broas vendidas: '))
valorPaes = paes*1
valorBroas = broas * 3.5
print(f'''
Quantidade de pães vendidos {paes} no valor de R$1,00 = R${valorPaes:.2f}
----------------------------------------------------------
Quantidade de Broas vendidas {broas} no valor de R$3,50 = R${valorBroas:.2f}
----------------------------------------------------------
Total =R${valorBroas+valorPaes:.2f}
Poupança= R${(valorBroas+valorPaes)*0.1:.2f}

''')
