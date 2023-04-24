# Faç um progrma que leia o nome completo de uma pessoa, mostrando em seguida o primeio e o último nome sepradamente.

nome = input(f'Digite o seu nome completo: ').title().split()
print(f'O primeio nome é {nome[0]}')
print(f'O último nome é {nome[-1]}')
