variavel = ["Luiz", "Joao", "Maria"]

comeca_com_j = False

for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print("Existe uma palavra que começa com J")
else:
    print("Nao existe uma palavra que começa com J")