salario = float(input('Insira o Salário R$'))
if salario <= 280.00:
    print(f'''
            Salário atual R${salario:.2f}\n
            Percentual de Aumento 20%
            Valor do aumento R${salario*0.2:.2f}
            Salário atualizado R${salario*1.2:.2f}
    
    ''')
elif 280 < salario <= 700:
    print(f'''
            Salário atual R${salario:.2f}\n
            Percentual de Aumento 15%
            Valor do aumento R${salario*0.15:.2f}
            Salário atualizado R${salario*1.15:.2f}
    
    ''')
elif 700 < salario <= 1500:
    print(f'''
            Salário atual R${salario:.2f}\n
            Percentual de Aumento 10%
            Valor do aumento R${salario*0.1:.2f}
            Salário atualizado R${salario*1.1:.2f}
    
    ''')
else:
    print(f'''
            Salário atual R${salario:.2f}\n
            Percentual de Aumento 5%
            Valor do aumento R${salario*0.05:.2f}
            Salário atualizado R${salario*1.05:.2f}
    
    ''')
