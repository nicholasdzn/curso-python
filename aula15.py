"""
Iterações de strings
"""
frase = 'o rato roeu a roupa do rei de roma'
contador = 0
nova_string = ''

while contador < len(frase):
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1

print(nova_string)