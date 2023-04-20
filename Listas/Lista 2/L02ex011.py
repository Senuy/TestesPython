nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
if idade <= 2:
    print('A pessoa é um bebê')
elif 2 < idade <= 11:
    print('A pessoa é um criaça')
elif 11 < idade <= 21:
    print('A pessoa é um jovem')
elif 21 < idade <= 64:
    print('A pesoa é um adulto')
elif 64 < idade <= 100:
    print('A pessoa é um idoso')
else:
    print('A pessoa é muito velhinha')
