qt = input('Digite a quantidade de convidadeos\n')
qt = int(qt)
ps =[]
i = 0
j = 0

while i < qt:
    ps.append(input('Digite o nome do convidados:\n'))
    i += 1

while j < i :
    print('Covidado:',ps[-i])
    i -= 1