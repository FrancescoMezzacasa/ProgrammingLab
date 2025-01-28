
data = input('Inserisci la tua data di nascita nel formato DD/MM/YYYY: ')

if(len(data) != 10):
    raise ValueError('La data inserita non è nel formato corretto')
data_split = data.split('/')
for i in range(len(data_split)):
    if(data_split[i].isdigit == False):
        raise TypeError('La data inserita non è valida')
    else:
        data_split[i] = int(data_split[i])
        

print(data_split)
if(data_split[0] > 31):
    raise ValueError('Il giorno può essere al massimo 31')
if(data_split[1] > 12):
    raise ValueError('Il mese può essere al massimo 12')
if(data_split[2] > 2024):
    raise ValueError("Non puoi non essere ancora nato")


