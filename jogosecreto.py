import os

secreto = input(str("Digite uma palavra (somente letras minúsculas): "))
dica = input(str("digite uma dica: "))
secreto = secreto.upper()

if secreto.isnumeric():
    print('Comece de novo!')
    exit()

else:
    print('Ok')
    os.system('cls')

print(f'DICA: {dica}')

digitadas = []
chances = 4

while True:
    if chances <= 0:
        print('##############')
        print('#Voce perdeu!#')
        print('##############')
        print(f'A palavra era {secreto}')
        break
    letra = input('Digite uma letra: ')
    letra = letra.upper()

    if len(letra) > 1:
        print('Não vale!, digite apenas uma letra.')
        continue

    digitadas.append(letra.upper())

    if letra in secreto:
        print(f'a letra {letra} existe na palavra secreta.')
    else:
        print(f'a letra {letra} não existe na palavra secreta')
        digitadas.pop()


    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else: 
            secreto_temporario += '_'
    
    if secreto_temporario == secreto:
        print(f'Voce ganhou! a palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    
    print(f'Voce ainda tem {chances} chances')
    print()
    