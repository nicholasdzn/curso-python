"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')
string2 = ' '.join(lista_1)
print(lista_1)
print(lista_2)
print(string2)

for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase.')