"""
contagem de caracteres usando len
"""
usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('Voce foi cadastrado no sistema')

string1= input('Digite algo: ')
string2= input('Digite mais alguma coisa: ')

print(f'Foram digitados {len(string1) + len(string2)} caracteres')
