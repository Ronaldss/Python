# Revisao: Strings -  métodos mais usado em geral

print('Concatenando strings')
string1 = 'Estou estudando '
string2 = 'a linguagem de programacao Python'


print('Concatenacao: ' + string1 + string2)

print('\n')
print('Contar quantos caracteres existem no texto em questao: ')
texto = 'My name is Ronald.'
tamanho = len(texto)
print('Quantidade de caracteres: ' + str(tamanho))

print('\n')
print('Navengando entre a posicao dos caracteres de uma frase: ')
frase1 = 'Minha terra tem palmeiras onde canta o sabiar'
frase2 = 'As aves que aqui gorgeinha gorjeiam, nao gorjeiam como la...'
print('\n')
print('FRASES COMPLETAS: ')
print('')
print(frase1)
print(frase2)
print('')
print('Selecionando um caracter na frase 1: ' + str(frase1[0]))
print('Selecionando um caracter na frase 2: ' + str(frase2[9]))

print('\n')
print('IMPRIMIR PARTE DE UMA FRASE 1:')
print(frase1[5:11])


