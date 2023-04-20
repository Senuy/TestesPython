horas = float(input('Insira a quantidade de horas trabalhadas:'))
valor = float(input('Insira o valor da sua hora de trabalho R$'))
salario = horas*valor
inss = salario*0.1
fgts = salario * 0.11
if salario <= 900:
    ir = 0
    print(f'''
    Salário Bruto R${salario:.2f}
    (-)IR 0
    INSS 10%      R${inss:.2f}
    FGTS 11%      R${fgts:.2f}
    Total de descontos R${ir+inss+fgts}
    Salário liquido R${salario-ir-inss-fgts}
    ''')
elif 900 < salario <= 1500:
    ir = 0.05
    print(f'''
    Salário Bruto R${salario:.2f}
    (-)IR 5%      R${salario*ir}
    INSS 10%      R${inss:.2f}
    FGTS 11%      R${fgts:.2f}
    Total de descontos R${(ir*salario)+inss+fgts}
    Salário liquido R${salario-ir-inss-fgts}
    ''')
elif 1500 < salario <= 2500:
    ir = 0.10
    print(f'''
    Salário Bruto R${salario:.2f}
    (-)IR 10%     R${salario*ir}
    INSS 10%      R${inss:.2f}
    FGTS 11%      R${fgts:.2f}
    Total de descontos R${(ir*salario)+inss+fgts}
    Salário liquido R${salario-ir-inss-fgts}
    ''')
else:
    ir = 0.2
    print(f'''
    Salário Bruto R${salario:.2f}
    (-)IR 20%     R${salario*ir}
    INSS 10%      R${inss:.2f}
    FGTS 11%      R${fgts:.2f}
    Total de descontos R${(ir*salario)+inss+fgts}
    Salário liquido R${salario-ir-inss-fgts}
''')
