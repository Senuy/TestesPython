l1 = float(input('Insira um dos lados do triangulo": '))
l2 = float(input('Insira um dos lados do triangulo": '))
l3 = float(input('Insira um dos lados do triangulo": '))

if l1 + l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    if l1 == l2 and l2 == l3:
        print('o triangulo é equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('o trangulo é isoceles')
    else:
        print('o triangulo é escaleno')
else:
    print('os lados não formam triangulo')
