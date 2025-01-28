#esercizio ppt parte 5 (pagina 201 GoodNotes)
class CSVFile():
    def __init__(self, name):
        if(type(name) != str):
            raise TypeError('Il nome che hai inserito non è una stringa ma un {}'.format(type(name)))
        self.name = name
    
    def get_data(self, start = None, end = None):
        if()
        if(start != None and end != None):
            if(start > end):
                raise Exception('Start deve essere minore di end')
        if(start != None):
            if(start < 1):
                raise Exception('Start deve essere maggiore o uguale a 1')

        if(end != None and end < 1):
            raise Exception('End deve essere maggiore o uguale a 1')
        try:
            file = open(self.name, 'r')
        except FileNotFoundError:
            print('Errore: il file con il nome {} non esiste'.format(self.name))
        else:
            dati = []
            lista_righe = file.readlines()
            if(start != None and start > len(lista_righe)):
                raise Exception('Start è maggiore del numero di righe nel file')
            if(end != None and end > len(lista_righe)):
                raise Exception('End è maggiore del numero di righe nel file')
            if(start == None):
                start = 1
            for i, line in enumerate(lista_righe, start):#start mi dice da dove parte quello che itera(i)
                if(end != None and i > end):
                    return dati
                elements = line.split(',')
                if(elements[0] != 'Date'):
                    elements[1] = elements[1].strip()
                    dati.append(elements)
            return dati
    
class NumericalCSVFile(CSVFile):
    def get_data(self):
        dati = super().get_data()
        for riga in dati:
            for j in range(1, len(riga)):
                try:
                    riga[j] = float(riga[j])
                except ValueError:
                    print('Errore: non posso convertire {} a float'.format(riga[j]))
        return dati

#ogg = NumericalCSVFile('dati/shampoo_sales.csv')
#padre = CSVFile(5)
#print(padre.get_data())
#print(ogg.get_data())
