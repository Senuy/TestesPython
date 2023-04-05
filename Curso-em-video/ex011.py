l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = (l*a)
tinta = area/2
print(
    f'Sua parede tem a dimensão  de {l:.2f}m x {a:.2f}m e sua área é {area:.2f}')
print(f'Para pintar essa parede, você precisára de {tinta:.2f}l de tinta')
