#esercizio ppt parte 5 (pagina 201 GoodNotes)
class CSVFile():
    def __init__(self, name):
        
        self.name = name
    
    def get_data(self):
        try:
            file = open(self.name, 'r')
        except FileNotFoundError as e:
            print('Errore: il file con il nome {} non esiste'.format(self.name))
        else:
            dati = []
            for line in file:
                elements = line.split(',')
                if(elements[0] != 'Date'):
                    dati.append(elements)
            file.close()
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
'''
ogg = NumericalCSVFile('dati/shampoo_sales.csv')
padre = CSVFile('dati/shampoo_sales.csv')
print(padre.get_data())
print(ogg.get_data())
'''