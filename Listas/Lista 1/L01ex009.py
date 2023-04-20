nome = input('Insira  o nome: ')
d = input('Disciplina: ')
n1 = float(input('Insira a n1": '))
n2 = float(input('Insira a n2": '))
n3 = float(input('Insira a n3": '))
m = (n1+n2+n3)/3
print(f'''
    Nome: {nome}
    Disciplina: {d}
    Média: {m:.2f}
''')
if m >= 6:
    print(' Aprovado')
else:
    print(' Reprovado')
