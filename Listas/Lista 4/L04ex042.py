lata = int(input('Insira a quanitdade desajada de latas:'))
g600 = int(input('Insira a a quantidade deseajada de Garrafas 600ml: '))
g2l = int(input('Insira a quantidade desejada de Garrafas 2L: '))

litros = ((lata*0.35)+(g600*0.6)+(g2l*2))

print(f'''
Foi efetuado o pedido de {lata} latas de 350ml
                         {g600} garrfas de 600ml
                         {g2l}  garrfas de 2 Litros
Total em litros comprado:{litros}L.                        

''')
