
def contaFrase(parole, parola):#conta quante volte una frase inizia con quella parola
    conto = 0
    punti = ['.', '!', '?']
    parole_consentite = [parola, parola + '.', parola + '!', parola + '?']
    if(parole[0] in parole_consentite):
        conto += 1
    for i in range(1, len(parole)):
        parola_precedente = parole[i-1]
        if(parole[i] in parole_consentite and parola_precedente[-1] in punti):
            conto += 1
    return conto

def conteggio(file):
    file = open(file, 'r')
    text = file.read()
    parole = text.split(' ')
    diz = {}
    punti = ['.', '!', '?']
    for parola in parole:
        if(parola[-1] in punti):
            p = parola[:-1]
        else:
            p = parola
        diz[p] = contaFrase(parole, p)
    return diz


print(conteggio('Prova.txt'))