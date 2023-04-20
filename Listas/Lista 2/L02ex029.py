s = input('Insira o seu sexo (M ou F): ').upper()
h = float(input('Insira a sua altura: '))

if s == 'M':
    print(f'{(72.7*h)-58:.2f}Kg Peso ideal para um homem da altura {h}')
else:
    print(f'{(62.1*h)-44.7:.2f}Kg Peso ideal para uma mulher da altura {h}')
