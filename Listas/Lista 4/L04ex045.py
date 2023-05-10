import datetime
nascimento = int(input('Insira o ano de nascimento XXXX:'))
ano = datetime.datetime.now().year
print(f'''
    A quantidade em anos: {ano-nascimento}
    A quantidade em meses: {(ano-nascimento)*12}
    A quantidade em dias: {(ano-nascimento)*365}
    A quantidade em semanas: {(ano-nascimento)*52}
''')
