# Revisão - Operadores relacionais

# == != < > <= >=


a = 1
b = 3
c = 4
d = 6
e = 4

print('Valor de A: ' + str(a))
print('Valor de B: ' + str(b))
print('Valor de C: ' + str(c))
print('Valor de D: ' + str(d))
print('Valor de E: ' + str(e))

if a == b:
	print("A eh maio que B")
if a != b:
	print("A eh diferente de B")
if c < a:
	print("C eh menor que A")
if d > b:
	print('D eh maior que B')
if c >= e:
	print('C eh maior ou igual a E')
if e <= a:
	print('E eh menor ou igual a A') 
else:
	print("Estamos no bloco do else")
