femininoMaior170 = 0
mascStatus = 0
masc = 0

for i in range(2):
    matricula = input(f'Digite a matricula do {i+1}º aluno: ')
    sexo = input(f'Digie o sexo(M/F) do {i+1}aluno: ').upper()
    altura = float(input(f'Digie a altura cm do {i+1}º aluno: '))
    status = int(input(f'Digie o status fisico  1 bom , 2 regular 3, ruim: '))

    if sexo == 'F' and altura > 170:
        femininoMaior170 += 1
    if sexo == 'M':
        masc += 1
        if status == 1:
            mascStatus += 1
percentualBom = (mascStatus/masc)*100

print(f'Quantidade de sexo Feminino maior que 1.70m: {femininoMaior170}')
print(f'Percentual de alunos masculinos com bom status: {percentualBom}%')
