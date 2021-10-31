# Alterando a caixa

nome = "Ronald"

# imprimir em minusculo
print(nome.lower())


# impremir em maiusculo
print(nome.upper())


# a forma original da variavel é mantida
print(nome)


# Remover caracteres especiais do final da string
nome1 = "Fulano"
nome2 = "deTal"
nomeCompleto = nome1 + nome2 + "\n"
print("Removendo caracteres especiais do final da string:")
print(nomeCompleto.strip())

# Convertendo uma lista em uma lista:
sequencia = "O rato roeu a roupa do rei de Roma"

seq = sequencia.split()

print(seq)
