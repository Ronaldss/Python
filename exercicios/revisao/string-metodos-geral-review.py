# Revisao: Strings

texto_minus = "este texto foi digitado em minusculo"

texto_maius = "ESTE TEXTO FOI ESCRITO EM MAIUSCULA"

print('')
print(texto_minus.lower())
print('')
print(texto_maius.upper())
print('')
print('Lembrando que a forma original da variavel eh mantida.')
print('\n')
print('Removendo caracteres especiais do final da frase.')
especial = 'Aqui temos uma quebra de linha no final. \n'
print('Com a quebra: ' + especial)
print('Sem a quebra: ' + especial.strip())
print('Fim!')
print('\n')
print('Convertendo uma frase/string em uma lista:')
print('')
frase2 = "O rato roeu a roupa do rei de Roma."
lista = frase2.split() 
print(lista)
