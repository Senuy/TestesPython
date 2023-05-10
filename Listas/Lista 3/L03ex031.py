turno = input(
    'Qual turno você estuda, M-matutino ou V-Vespertino ou Noturno:').upper()
if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa Tarde')
elif turno == 'N':
    print('Boa Noite')
else:
    print('Valor inválido')
