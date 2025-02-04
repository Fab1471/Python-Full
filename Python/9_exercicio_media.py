# Receba 4 notas de um aluno e exiba:

# Se ele foi aprovado (nota maior ou igual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) 
# Se ele foi reprovado (nota menor do que 4)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print(f'Aluno Aprovado com a média {media}')
elif media >= 4:
    print(f'Aluno de Recuperacão com a média {media}')
else:
    print(f'Aluno Reprovado com a  média {media}')
