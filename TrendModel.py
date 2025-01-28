def Media(dati):
    return(sum(dati)/len(dati))

class TrendModel():
    def predict(self, data):
        if(type(data) != list):
            raise TypeError('I dati forniti non sono una lista')
        for i in data:
            if(type(i) != int and type(i) != float):
                raise TypeError('I valori nella lista non sono numeri')
        ultimo = data[len(data) - 1]
        if(len(data) == 1):
            raise Exception('La predizione si deve basare su almeno due mesi')
        differenze = []
        for i in range(len(data) - 1):
            differenze.append(data[i + 1] - data[i])
        media = Media(differenze)
        predizione = ultimo + media
        return predizione

valori = [8, 19, 31, 41, 50, 52, 60]
modello = TrendModel()
print(modello.predict(valori))