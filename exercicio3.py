nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) >= 6:
    print('Seu nome é grande')
    