"""
Variaveis
"""

nome = 'Nicholas'
idade = 18
altura = 1.82
peso = 80
e_maior = idade >= 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?:', e_maior)

print('Meu nome é', nome, 'e meu peso é', peso,'kg, e meu imc é de', peso/(altura ** 2))
print(f'meu nome é {nome} e meu peso é {peso} kg, e meu imc é de {peso/(altura**2):.2f}')

