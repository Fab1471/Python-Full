# Receba uma temperatura em Farenheit e exiba em graus Celsius

farenheit = float(input('Digite uma temperatura em Farenheit: '))

celsius = (farenheit - 32) * 5 / 9

print(f'{farenheit} Farenheit equivale a {celsius} graus Celsius')
