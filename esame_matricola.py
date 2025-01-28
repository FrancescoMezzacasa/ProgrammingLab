class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        try:
            file = open(self.name, 'r')
        except Exception:
            raise ExamException('Non è stato possibile aprire il file')
        else:
            ris = []
            for line in file:
                elements = line.split(',')
                if(elements[0] != 'date'):
                    if(elements[1].strip() != ''):
                        #contorllo se non è solo '\n'
                        i = elements[1].strip()
                        if(i.isdigit() and int(i) > 0):
                            elements[1] = int(i)
                        else:
                            print('{} non è un numero intero'.format(i))
                    else:#se non ho la misurazione di quel mese lo tolgo dalla lista che metterò in ris
                        elements.pop()
                    ris.append(elements)

            #punto 2 parte opzionale, controllo se sono in ordine cronologico
            for j in range(len(ris) - 1):
                curr = ris[j][0].split('-')#se siamo in '2024-01' curr sarà ['2024', '01']
                pross = ris[j + 1][0].split('-')#come curr ma per il prossimo, così confronto se sono in ordine
                #print(curr)
                #print(pross)
                if(curr[0] > pross[0] or (curr[1] >= pross[1] and pross[1] != '01')):
                    #se l'anno di curr è maggiore di quello di pross o se il mese di curr è >= di quello di pross
                    #escludo il caso in cui pross è gennaio perche altrimenti è ovvio che 12 > 1
                    raise ExamException('I timestamp non sono in ordine')
            file.close()
            return ris
        
def compute_variations(time_series, first_year, last_year):
    #fare qua i controlli
    if(first_year == None or last_year == None):
        raise ExamException('Devi fornire gli input richiesti')
    #punto 1 parte opzionale, controllo se i tipi sono stringhe e controllo se sono fuori dal range che c'è nel file
    if(type(first_year) != str or type(last_year) != str):
        raise ExamException('Gli anni devono essere passati come stringhe')
    if(int(first_year) < 1949 or int(first_year) > 1960):
        raise ExamException("L'anno da cui partire non è presente nei dati")
    if(int(last_year) < 1949 or int(last_year) > 1960):
        raise ExamException("L'anno a cui arrivare non è presente nei dati")
    if(int(last_year) < int(first_year)):
        raise ExamException("L'anno di partenza deve essere prima di quello di fine")
    anni = {}#qua ci metto i numeri di passeggeri per ogni anno
    for i in range(int(first_year), int(last_year) + 1):
        l = []
        for j in time_series:
            if(j[0].startswith(str(i)) and len(j) > 1):#se sono nell'anno giusto e c'è la misurazione di quel mese
                l.append(j[1])
        anni[str(i)] = l
    #fatto il dizionario
    #print(anni)
    media = {}
    for i in anni.keys():
        #print(type(i))
        if(len(anni[i]) > 0):#calcolo la media solo se ho le misurazioni per quell'anno
            media[i] = round(sum(anni[i])/len(anni[i]), 1)
    #fatto il dizionario con le medie di ogni anno
    #print(media)
    diff = {}
    chiavi = list(media.keys())
    #print(chiavi)
    for i in range(len(chiavi) - 1):
        diff[str(chiavi[i]) + '-' + str(chiavi[i + 1])] = round(media[chiavi[i + 1]] - media[chiavi[i]], 1)
    return diff
        
time_series_file = CSVTimeSeriesFile('dati/data.csv')
time_series = time_series_file.get_data()
#print(time_series)
print(compute_variations(time_series, '1949', '1960'))

                    
                    
