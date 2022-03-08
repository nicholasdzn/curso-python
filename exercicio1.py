num = input('Digite um numero inteiro: ')

if num.isdigit():
    num = int(num)
    num = num % 2
    if num == 0:
        print('O numero é par')
    else:
        print('O numero é impar')
else:
    print('Error (nao é um numero inteiro)')

