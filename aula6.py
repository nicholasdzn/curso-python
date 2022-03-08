"""
Entrada de dados
"""
nome = input("Qual o seu nome? ")
#conversao de str para int
idade = int(input("Qual a sua idade? "))
ano_nascimento = 2021-idade
print(f'O usuario digitou {nome} e o tipo da variavel é {type(nome)} ')
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}.')