frango = int(input('Digite a quantidade de frangos: '))
valor = (frango*4)+(frango*3.5)

print(f'''
    Valor do anel rastreador R$4,00
    Valor dos aneis de alimentação R$3,50
    Valor total referente a quantidade inserida R${valor:.2f}

''')
