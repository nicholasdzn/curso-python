"""
Formatando valores com modificadores - aula 5
:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.f(numero)f - quantidade de casas decimais (float)
:.(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
"""
num_1=1
#será colocado 9 zeros para completar 10 casas decimais
print(f'{num_1:0>10}')

num_2=1150
print(f'{num_2:0^10}')

nome = 'Nicholas'
#funciona com strings também
print(f'{nome:#^50}')

print(nome.ljust(15, '@'))
print(nome.lower())
print(nome.upper())
print(nome.title())
