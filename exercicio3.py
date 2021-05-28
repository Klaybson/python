cidades = ['salvador', 'sao bento', 'bomja', 1986]
cidades.append(input('Acresente uma nova cidade:\n'))
cidades.remove(1986)
#cidades.insert(0,'São Paulo')

print(cidades)
print('A nova cidade é:',cidades[-1])