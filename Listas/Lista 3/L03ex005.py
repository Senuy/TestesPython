nome = input('Insira o nome do Aluno: ')
materia = input('Qual disciplina: ')
n1 = float(input('Insira a nota da primeira prova: '))
n2 = float(input('Insira a nota da Segunda prova: '))
n3 = float(input('Insira a nota da terceira prova: '))
print(f''' 
        Nome do aluno: {nome}
        1º Prova:{n1}
        2º Prova:{n2}
        3º Prova:{n3}
        Média final:{(n1+n2+n3)/3:.2f}
''')
