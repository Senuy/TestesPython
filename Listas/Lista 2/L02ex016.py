n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n2 < n1 > n3:
    print(f'O número maior é {n1}')
elif n1 < n2 > n3:
    print(f'O número maior é {n2}')
else:
    print(f'O número maior é {n3}')

if n2 > n1 < n3:
    print(f'O número menor é {n1}')
elif n1 > n2 < n3:
    print(f'O número menor é {n2}')
else:
    print(f'O número menor é {n3}')
