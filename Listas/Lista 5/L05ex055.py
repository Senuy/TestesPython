num = []
menor = 999999
for i in range(20):
    valor = int(input('Insira um número: '))
    num.append(valor)
    if valor < menor:
        menor = valor
print(f'o menor foi {menor}')
