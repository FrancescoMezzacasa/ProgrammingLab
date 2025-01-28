
try:
    def sum_csv(name_file):
        file = open(name_file, "r")
        lista = []
        somma = 0
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                try:
                    lista.append(float(elements[1]))
                except ValueError as e:
                    print('Errore: {}'.format(e))
                    print('Non posso convertire stringhe a numeri per sommarli')
        
        if(len(lista) == 0):
            return None
        somma = sum(lista)

        file.close()
        return(somma)

except ValueError as e:
    print('Errore: {}'.format(e))
    print('Non posso convertire stringhe a numeri per sommarli')

