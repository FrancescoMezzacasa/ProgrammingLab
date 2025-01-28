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
            return dati
    

#padre = CSVFile('dati/shampoo_sales.csv')
#print(padre.get_data())
