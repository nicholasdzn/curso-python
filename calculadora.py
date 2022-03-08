from time import sleep

print('Operadores suportados: +, -, *, /')
while True:
    num1=input("Digite um numero: ")
    num2=input("Digite outro numero: ")
    operador=input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Não é um valor válido')
        continue

    num1=int(num1)
    num2=int(num2)

    if operador == '+':
        print(num1+num2)
    elif operador == '-':
        print(num1-num2)
    elif operador == '/':
        print(num1/num2)
    elif operador == '*':
        print(num1*num2)

    print('-'*10)

    stop = input('Deseja sair?\n[s] para sim\n[n] para não\n')
    if stop == 's':
        break
    elif stop == 'n':
        continue
    else:
        print('Comando não reconhecido!')
        print('Recomeçando....')
        sleep(2)
        continue

print('Finalizado!')
