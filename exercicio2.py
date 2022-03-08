horario = float(input('Digite o horário atual: '))

if horario >= 0 and horario <= 11:
    print('Bom dia')
elif horario >= 12 and horario <= 17:
    print('Boa tarde')
elif horario >= 18 and horario <= 23:
    print('Boa noite')

