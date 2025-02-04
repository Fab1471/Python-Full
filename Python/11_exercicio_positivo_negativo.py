# Receba um número e exibe se ele é positivo ou negativo.

n = float(input('Digite um número: '))

if n > 0:
    print(f'{n} é um número positivo.')
elif n == 0:
    print(f'{n} é um número neutro.')
else:
    print(f'{n} é um número negativo.')
