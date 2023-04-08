# Crie um programa que leia o nome completo de uma pessoa de mostre:
# O nome com todas as letra maiúsculas
# Quantas letras ao todo(sem considerar espaços)
# quantas letras tem o primeiro nome
nome = input('Digite o seu nome inteiro: ')
print(nome.upper())
print(nome.lower())
cont = len(nome.replace(" ", ""))
print(cont)
nome = nome.split()
print(len(nome[0]))
