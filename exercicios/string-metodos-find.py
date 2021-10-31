# Localizar indice/posição de determinado caracter em uma string

minha_string = "O rato roeu a roupa do rei de Roma" 

busca = minha_string.find("rei")

print(busca)

'''
Descobrindo a posição do caracter, você
pode usar outros métodos para melhorar a busca.

Por exemplo, podemos imprimir uma parte do texto com
base na parte encontrada na busca realizada.


'''

print(minha_string[busca:])




