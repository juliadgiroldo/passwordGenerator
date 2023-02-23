import random

caracteres_senha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number_of_password = int(input("Digite a quantidade de senhas que você deseja: "))

for i in range(1, number_of_password+1):
    password_lenght = int(input(f'Digite o número de caracteres da senha {i}: '))
    password = ''
    for j in range(password_lenght):
        password += random.choice(caracteres_senha)
    print(password)
