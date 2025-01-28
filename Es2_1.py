def contaParola(file, parola):
    parole = []
    count = 0
    for line in file:
        aus = line.split(' ')#lista che contiene questa riga splittata
        for i in aus:
            parole.append(i)#per ogni linea metti le parole nella lista finale
    for j in parole:
        if(j == parola):
            count += 1

    return count
    


file = open('Prova.txt', 'r')

parola = input('Inserire la parola da cercare: ')
print(contaParola(file, parola))
    