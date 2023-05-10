m001 = int(input('Insira a quantidade de moedas de 1 Centavo: '))*0.01
m005 = int(input('Insira a quantidade de moedas de 5 Centavos: '))*0.05
m010 = int(input('Insira a quantidade de moedas de 10 Centavos: '))*0.1
m025 = int(input('Insira a quantidade de moedas de 25 Centavos: '))*0.25
m050 = int(input('Insira a quantidade de moedas de 50 Centavos: '))*0.5
m1 = int(input('Insira a quantidade de moedas de 1 Real: '))*0.05
print(f'O valor total economizado é de R${m001+m005+m010+m025+m050+m1}')
