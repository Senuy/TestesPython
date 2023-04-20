hamburguer = int(input('Insira a quantidade de hamburguers deseja fazer: '))
queijo = 0.1
presunto = 0.05
carne = 0.1
print(f'''
    Para a quantidade informada de {hamburguer} hamburgueres
    Será necessário comprar:
    {queijo*hamburguer:.2f}Kg de Queijo
    {presunto*hamburguer:.2f}Kg de Presunto
    {carne*hamburguer:.2f}kg de Carne de Hamburguer

''')
