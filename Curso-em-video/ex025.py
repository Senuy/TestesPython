# Crie um program que leia o noem de uma pessoa e diga se ela tem silva no nome
nome = input('Digite o seu nome: ')
nome = nome.title()
nome = nome.split()
c = nome[0:].find('Silva')
