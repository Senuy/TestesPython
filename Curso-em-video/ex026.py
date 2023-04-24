# Faça um programa que leia uma frase pelo teclado e mostre: -> quantas vezes aparae a letra "a"
# Em que posição ela aparece pa primeira vez.
# Wnq que psoição ela aparecea a última vez.
frase = input('Digite  uma Frase: ').strip().upper()
print(f'A letra "a" aparece {frase.count("A")}')
print(f'A letra "a" aparece {frase.find("A")+1}')
print(f'A letra "a" aparece {frase.rfind("A")+1}')
