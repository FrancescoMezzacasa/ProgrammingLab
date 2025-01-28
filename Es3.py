def isPalindrome(stringa):
    check = True
    lungh = len(stringa)
    for i in range((lungh//2)):
        if(stringa[i] != stringa[lungh - 1 - i]):
            check = False
    
    return check

def isPalindrome_bis(stringa):#più giusto e comodo su python
    return(stringa == stringa[-1::-1])#tanto questa espressione ritorna gia True o False

stringa = input('Inserire la stringa da verificare: ')
print(isPalindrome(stringa.lower()))
print(isPalindrome_bis(stringa.lower()))
