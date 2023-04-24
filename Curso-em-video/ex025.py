# Crie um program que leia o noem de uma pessoa e diga se ela tem silva no nome
nome = input('Digite o seu nome: ').strip().title()
print(f'O seu nome tem Silva {"Silva" in nome} ')
