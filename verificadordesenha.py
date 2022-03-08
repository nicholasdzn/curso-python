usuario = input('Digite um nome de usuário: ')
senha = int(input('Digite uma senha: '))

print('Cadastro concluído, vamos fazer o login')

login = input('LOGIN\n')
senha_login = int(input('SENHA\n'))

if usuario == login and senha == senha_login:
    print('Login efetuado com sucesso')
else:
    print('Usuario ou senha incorretos, tente novamente')
