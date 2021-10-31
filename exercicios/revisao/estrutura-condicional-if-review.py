# coding: UTF-8


# Revisão - Estrutura condicional IF

acesso_name = input('User: ')
acesso_pass = int(input('Password: '))

#acesso_pass = int(acesso_pass)

print("Analisando...")

if acesso_name == 'Ronald' and acesso_pass == 123:
    print("Acesso liberado!")
else:
    print("ACESSO NÃO AUTIRIZADO!!!")
