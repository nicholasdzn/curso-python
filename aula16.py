"""
For in em python
iterando strings com for 
função range(start=0, stop, step=1)
"""
#começa no 1 e termina no 9 pulando de 1 em 1
for n in range(1,10,1):
    print(n)

print('#########')

for n in range(100):
    if n % 8 == 0:
        print(n)

print('###########')

texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)