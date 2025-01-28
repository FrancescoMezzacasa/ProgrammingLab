def isTriangle(a, b, c):
    #possono formare un triangolo se e solo se ognuno è minore della somma degli altri due
    if((a > b + c) or (b > a + c) or (c > b + a)):
        return('Con questi tre lati non si può costruire un triangolo')
    elif((a == b and b != c) or (b == c and c != a) or (c == a and a != b)):
        return('Il triangolo formato da questi lati è isoscele')
    elif(a == b and b == c):
        return('Il triangolo formato da questi lati è equilatero')
    else:
        return('Il triangolo formato da questi lati è scaleno')
    
a = int(input('Inserisci la lunghezza del primo lato: '))
b = int(input('Inserisci la lunghezza del secondo lato: '))
c = int(input('Inserisci la lunghezza del terzo lato: '))

print(isTriangle(a, b, c))