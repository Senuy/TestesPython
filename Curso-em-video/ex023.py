# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = int(input('Digite um número de 0 a 9999: '))

print(f'milhar: {(n//1000)%10:.0f}')
print(f'centena: {(n//100)%10:.0f}')
print(f'dezena: {(n//10)%10:.0f}')
print(f'unidade: {(n/1)%10:.0f}')
