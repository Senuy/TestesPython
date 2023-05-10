dia = int(input('Digite o dia: '))
mes = int(input('Digite o número do mês: '))
diasPorMes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
diasCorridos = sum(diasPorMes[m] for m in range(1, mes))+dia

print(f'Total de dias corridos:{diasCorridos}')
