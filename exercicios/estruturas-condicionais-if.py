# -*- coding: utf-8 -*-


# Estruturas condicionais
# Comando IF
# sempre obsevar a identação que no Python é muito importante

'''
if condição:
    bloco_que_sera_executado
'''


''' Exemplo#01 (SIMPLES)

x = 1
y = 100

if x > y:
    print("X é maior que Y")
if y > x:
    print("Y é maior que X")

'''



''' Exenplo#02 (ELSE)

x = 2
y = 3

if x > y:
    print("X é maior que Y")
else:
    print("Y é maior que X")  


'''


# Exemplo#03 (ELIF)

x = 21
y = 34

if x == y:
    print("numeros iguais")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")
print("Saiu do IF.")

