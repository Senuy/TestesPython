p = int(input('Insira a quantidade de Camisetas pequenas: '))
m = int(input('Insira a quantidade de Camisetas médias: '))
g = int(input('Insira a quantidade de Camisetas Grandes: '))
peq = p * 10
med = m * 12
gra = g * 15
print(f'''
    ->{p} Camisetas pequenas no valor de R$10 fica um total de  R${peq}
    ->{m} Camisetas méidas no valor de R$12 fica um total de   R${med}
    ->{g} Camisetas grandes no valor de R$15 fica um total de  R${gra}
    Valor total das Camisetas R${peq+med+gra:.2f}

''')
