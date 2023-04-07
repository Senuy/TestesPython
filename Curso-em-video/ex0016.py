# Crie um programa que leia um número Real qualquer pelo teclado e mosta na tela a sua porção inteira
from math import trunc
n = float(input('Insira um número real com vírgula: '))
print(f'O valor inteiro de {n} é {trunc(n)}')
