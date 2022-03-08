"""
Condiçoes IF, ELIF e ELSE - Aula 7
"""
if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro")
elif True:
    print("Mais uma verdadeira")
    nome = input('Qual o seu nome?')
    if nome == 'Nicholas':
        print(f'Correto {nome}')
    else: 
        print("Incorreto")
else:
    print("Não é verdadeira")

print('----Linha ignorada----')