# Operadores Logicos
# and or not

a = 100
b = 200
c = 300
d = 10


print('A: ' + str(a))
print('B: ' + str(b))
print('C: ' + str(c))
print('D: ' + str(d))



if a < b and a > d:
    print('A eh menor que B e maior que D.')
if b > a or d >= c:
    print('B eh maior que A ou D eh maior ou igual a C')
if not(a > b):
    print('a > b: condicao modificada pelo NOT')
else:
    print('Condicao inexistente.')




