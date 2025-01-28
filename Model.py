
class Model():
    def __init__(self, window = 2):
        self.window = window
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')
    def evaluate(self, data):
        errori = []
        self.lungh = int(len(data)*70/100)
        storici = data[:self.lungh]
        test_data = data[self.lungh:]
        #devo controllare se esiste fit perche se istanzio un TrendModel non esiste fit
        #se istanzion un FitTrendModel invece sì
        try:
            self.fit(storici)
        except Exception as e:
            if isinstance(e, NotImplementedError):
                pass
        for i in range(len(test_data) - self.window):
            valore_predetto = self.predict(test_data[i:self.window + i])
            errori.append(abs(valore_predetto - test_data[self.window + i]))
        mae_error = sum(errori)/len(errori)
        return mae_error

class TrendModel(Model):
    def Media(self, data):
        return sum(data)/len(data)
    
    def compute_avg_variation(self, data):
        differenze = []
        for i in range(len(data) - 1):
            differenze.append(data[i + 1] - data[i])
        media = self.Media(differenze)
        return media
    
    def ControlloInput(self, data):
        if(type(data) != list):
            raise TypeError('I dati forniti non sono una lista')
        for i in data:
            if(type(i) != int and type(i) != float):
                raise TypeError('I valori nella lista non sono numeri')
        if(len(data) == 1):
            raise Exception('La predizione si deve basare su almeno due mesi')
    
    def predict(self, data):
        self.ControlloInput(data)

        ultimo = data[len(data) - 1]
        predizione = ultimo + self.compute_avg_variation(data)
        return predizione

class FitTrendModel(TrendModel):
    def fit(self, storici):
        self.historical_avg_variation = self.compute_avg_variation(storici)
        
    def predict(self, test_data):
        try:
            self.historical_avg_variation
        except AttributeError:
            print('Il modelllo non può essere fittato')
        self.ControlloInput(test_data)
        ultimo = test_data[len(test_data) - 1]
        predizione = ultimo + ((self.compute_avg_variation(test_data) + self.historical_avg_variation)/2)
        return predizione

valori = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10.5, 11.5, 11.2]
modelloFittato = FitTrendModel()
modello = TrendModel()
print(modello.evaluate(valori))
print(modelloFittato.evaluate(valori))





