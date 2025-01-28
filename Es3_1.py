
class CSVFile():
    def __init__(self, name):
        
        self.name = name
    
    def get_data(self):
        file = open(self.name, 'r')
        dati = []
        for line in file:
            elements = line.split(',')
            if(elements[0] != 'Date'):
                e = elements[1].strip()
                elements[1] = e
                dati.append(elements)
        return dati


dati = CSVFile('dati/shampoo_sales.csv')

print(dati.get_data())



