# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = input('Digite um número de 0 a 9999: ')
print(f'milhar: {n[:1]}')
print(f'centena: {n[1:2]}')
print(f'dezena: {n[2:3]}')
print(f'unidade: {n[3:]}')
