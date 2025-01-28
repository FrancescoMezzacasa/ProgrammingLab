def occorrenze(parole, parola):
    count = 0
    for j in parole:
        if(j == parola):
            count += 1
    return count

def contaParole(file):
    diz = {}
    file = open(file, 'r')
    text = file.read()
    parole = text.split(' ')
    print(parole)
    for i in parole:
        diz[i] = occorrenze(parole, i)
    file.close()
    return diz

print(contaParole('Prova.txt'))