# coding: UTF-8


# Revisão - Estrutura condicional IF

acesso_name = input('User: ')
acesso_pass = int(input('Password: '))

#acesso_pass = int(acesso_pass)

print("Analisando...")

if acesso_name == 'Ronald' and acesso_pass == 123:
    print("Acesso liberado!")
elif acesso_name == 'Emanuella' or acesso_name == "emanuella" or acesso_name == "EMANUELLA":
    print("Ola, " + acesso_name + ". Nao encontramos seu perfil, por favor, cadastre-se.")
else:
    print("ACESSO NÃO AUTORIZADO!!!")

print("The End!")
