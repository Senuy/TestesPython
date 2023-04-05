dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos KM rodados: '))
total = (dias*60)+(km*0.15)
print(f'O Valor total deu R${total:.2f}')
