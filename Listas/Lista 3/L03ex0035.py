carne = input(
    'Insira qual carne deseja comprar(F-File Duplo/ A- Alcatra/ P- picanha)').upper()
quantidade = float(input('Insira a quantidade em KG que deseja comprar: '))

if carne == 'F':
    if quantidade <= 5:
        preco = 34.90
        total = preco*quantidade
        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95}
        ''')
    else:
        preco = 35.80
        total = preco*quantidade
        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95:.2f}
        ''')
elif carne == 'A':
    if quantidade <= 5:
        preco = 44.90
        total = preco*quantidade
        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95:.2f}
        ''')
    else:
        preco = 46.80
        total = preco*quantidade

        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95:.2f}
        ''')

elif carne == 'P':
    if quantidade <= 5:
        preco = 66.90
        total = preco*quantidade

        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95:.2f}
        ''')
    else:
        preco = 67.80
        total = preco*quantidade
        print(f'''
        Preço por KG R${preco:.2f}
        Preço Total a pagarR${total:.2f}
        Preço total a pagar usando cartão Tabajara dando um desconto de 5% R${total*0.95:.2f}
        ''')
else:
    print('Caracter inválido')
