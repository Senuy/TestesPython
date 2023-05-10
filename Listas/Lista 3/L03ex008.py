distancia = float(input('Insira a distancia da viagem:'))
consumo = float(input('Insra o consumo médio do carro: '))
valor = float(input('Insira o preço atual do combustível: '))
print(f'A viagem terá um custo de R${(distancia/consumo)*valor:.2f}')
