def scambia(lista, i, j):
    tmp = lista[i]
    lista[i] = lista[j]
    lista[j] = tmp
    return lista

lista = [1, 2, 3, 4, 5]
i = int(input('Inserisci il primo indice: '))
j = int(input('Inserisci il secondo indice: '))

print(scambia(lista, i, j))