def somma_cifre(n):
    if(n < 0):
        n = -n
    if(n < 10):
        return n
    return(n%10 + somma_cifre(n//10))

def controllaInput(inizio, fine, cifre):
    if(type(inizio) != int or type(fine) != int or type(cifre) != int) :
        raise TypeError('Inizio, Fine e il valore della somma delle cifre devono essere tutti numeri interi!')
    if(inizio > fine):
        raise ValueError("L'inizio deve essere un numero minore della fine")
    if(cifre <= 0):
        raise ValueError('La somma delle cifre deve essere un numero strettamente positivo')
    return

inizio = int(input('Inserisci il numero da cui iniziare: '))
fine = int(input('Inserisci il numero a cui arrivare: '))
cifre = int(input('A quale numero deve essere uguale la somma delle cifre? '))
controllaInput(inizio, fine, cifre)

l = []
for i in range(inizio, fine + 1):
    l.append(i)

for i in l:
    #print(somma_cifre(i))
    if(somma_cifre(i) == cifre):
        print(i)