saque = int(input('Insira a quantidade que deseja sacar R$'))
if 10 <= saque <= 600:
    nota100 = nota50 = nota10 = nota5 = nota1 = 0

    while saque >= 100:
        nota100 += 1
        saque -= 100
    while saque >= 50:
        nota50 += 1
        saque -= 50
    while saque >= 10:
        nota10 += 1
        saque -= 10
    while saque >= 5:
        nota5 += 1
        saque -= 5
    while saque >= 1:
        nota1 += 1
        saque -= 1

    print(f'''
        Notas de R$100 = {nota100}
        Notas de R$50 = {nota50}
        Notas de R$10 = {nota10}
        Notas de R$5 = {nota5}
        Notas de R$1 = {nota1} 
    ''')


else:
    print('Saque indisponível para valores abaixo de R$10,00')
