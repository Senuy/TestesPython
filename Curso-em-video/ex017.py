
# Facça um progrma que leia o comprineo do cateto oposto e do cateto adjacente de um triângula retângulo, calule e mostr o comprime da hipotenusa.
from math import hypot
ca = float(input('Insira o Cateto  Adjacente: '))
co = float(input('Insira o Cateto Oposto: '))
hyp = hypot(co, ca)
print(f'A hipotenusa deses triangulo é: {hyp:.2f}')
