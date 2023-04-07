# Faça um programa que leia um ângulo qualqer e mostra na tela o valor de seno, cossen e tangente desse ângulo
from math import cos, sin, tan, radians
ang = float(input('Insira o Angulo desejado: '))
print(f'O seno de {ang:.2f} é {sin(radians(ang)):.2f},\n O cosseno de {ang:.2f} é {cos(radians(ang)):.2f},\n e o tangente de {ang:.2f} é {tan(radians(ang)):.2f}.')
