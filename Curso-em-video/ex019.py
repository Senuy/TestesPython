# Umprofessor quer sotear um dos seus quatro alunos para apagar o quadro. Facça um programa que ajude ele, lendo o nome dels e escrevendoo nome do escolhido.
from random import choice
prim = input('Digite o nome do primeiro aluno: ')
segu = input('Digete o nome do segundo aluno: ')
terc = input('Digite o nome do terceiro aluno: ')
quar = input('Digite o nome do quarto aluno: ')
nomes = [prim, segu, terc, quar]
print(f'O aluno escolhido foi {choice(nomes)}')
