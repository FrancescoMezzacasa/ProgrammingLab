def contaLettera(par, lett):
    conto = 0
    for i in par:
        if(i == lett):
            conto = conto + 1
    
    return conto

par = 'cicciogamer'
lett = 'c'
print(contaLettera(par, lett))