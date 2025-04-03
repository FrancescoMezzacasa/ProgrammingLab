class ExamException(Exception):
    pass

class CSVTextFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        try:
            file = open(self.name, 'r')
        except:
            raise ExamException('Impossibile aprire il file.')
        
        ris = []
        for line in file:
            elements = line.strip().split(',', 1)#elements = [1, '...']
            if(elements[1] != 'sentence'):
                riga = []
                try:
                    riga.append(int(elements[0]))
                except:
                    print('Il numero delle frasi deve essere intero')
                else:
                    if(len(elements[1]) > 0):
                        riga.append(elements[1])
                        ris.append(riga)
        return ris

def contaParole(frase):
    parole = frase.split(' ')
    paroleVere = []
    conto_apostrofi = 0
    for i in parole:
        if(not(len(i) == 1 and not i.isalpha())):#parole vere sono quelle non tipo '-'
            paroleVere.append(i)
            if("'" in i):
                conto_apostrofi += 1
    return len(paroleVere) + conto_apostrofi

def contaLettere(frase):
    conto = 0
    for i in frase:
        if i.isalnum():
            conto += 1
    return conto

def contaPunteggiaturaComplessa(frase):
    punteggiaturaComplessa = [';', ':', '-', '...']
    conto = 0
    for i in frase:
        if(i in punteggiaturaComplessa):
            conto += 1
    return conto

def calcolaComplessità(frase):
    tuttisimboli = True
    complessità = 0
    for i in frase:
        if(i.isalnum()):
            tuttisimboli = False
    if(not tuttisimboli):
        complessità = contaParole(frase) + (0.5 * (contaLettere(frase)/contaParole(frase))) + (2 * contaPunteggiaturaComplessa(frase))
    return complessità

def compute_sentence_complexity(lista_frasi):
    diz = {}
    #controllo che siano in ordine
    for j in range(len(lista_frasi) - 1):
        if(lista_frasi[j][0] >= lista_frasi[j+1][0]):
            raise ExamException('I numeri non sono in ordine')
        
    for i in lista_frasi:
        diz[i[0]] = round(calcolaComplessità(i[1]), 2)
    return diz

if(__name__ == "__main__"):
    fileFrasi = CSVTextFile('/mnt/c/Users/frame/OneDrive/Desktop/Francesco scuola/Uni/Programmazione/Nenzi/git/dati/sentences_dataset.csv')
    lista_frasi = fileFrasi.get_data()
    print(compute_sentence_complexity(lista_frasi))
    
    
    