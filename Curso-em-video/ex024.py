# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
city = input('Insira o nome da cidade: ')
city = city.capitalize()
city = city.split()
c = city[0].find('Santo')
if c == 0:
    print('A cidade começa com santo')
else:
    print('A cidade não começa com santo')
