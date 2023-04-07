# O mesmo professor do desafi anterior quer soterar a orde de apresentação de trabalhos dos alunos. Faça umporograma que leia o nome dos quatro alunos e mostre a ordem soreteada.
from random import shuffle
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem ficou {lista} ')
