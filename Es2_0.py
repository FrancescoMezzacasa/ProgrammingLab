def sum_csv(name_file):
    file = open(name_file, "r")
    lista = []
    somma = 0
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            lista.append(float(elements[1]))
    
    if(len(lista) == 0):
        return None
    somma = sum(lista)

    file.close()
    return(somma)


    
