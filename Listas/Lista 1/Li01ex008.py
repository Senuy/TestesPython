valor = float(input('Insira o valor do Combustível: '))
quantidade = float(input('Insira a quantidade inserida: '))
consumo = float(input('Insira o consumo médio em Litros: '))
print(f''' 
        Valor total gasto R${valor*quantidade}
        Distancia máxima percorrida sem abastecer novamente: {consumo*quantidade}Km

''')
