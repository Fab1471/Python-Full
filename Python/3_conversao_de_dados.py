idade_str = '21'
idade_inteiro = 21
number_float = 21.2
n_i_to_f = 21

tipo_de_dado = type(idade_str)

print(type(idade_str)) # printando tipo direto da variável
print(tipo_de_dado) # printando o tipo da variável dentro de uma variável

idade_str = int(idade_str)
print(idade_str)
print(type(idade_str))

idade_inteiro = str(idade_inteiro)
print(idade_inteiro)
print(type(idade_inteiro))

number_float = int(number_float) # conversão de float para int - removida a parte decimal. .
print(number_float)
print(type(number_float))

n_i_to_f = float(n_i_to_f)
print(n_i_to_f)
print(type(n_i_to_f))
