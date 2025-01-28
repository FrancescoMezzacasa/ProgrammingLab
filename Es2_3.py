def longest_word(file):
    diz = {}
    text = file.read()
    text = text.lower()
    parole = text.split(' ')
    for i in parole:
        primaLettera = i[0]
        if((primaLettera not in diz) or (len(i) > len(diz[primaLettera]))):
            diz[primaLettera] = i
    return diz



file = open('Prova.txt', 'r')
print(longest_word(file))
