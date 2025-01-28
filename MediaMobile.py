class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        self.window = window
        if(self.window == None):
            raise ExamException('La finestra non può essere None')
        if(type(self.window) != int):
            raise ExamException('La dimensione della finestra deve essere un intero')
        if(self.window <= 0):
            raise ExamException('La lunghezza della finestra deve essere positiva')
    def checkDati(self, dati):
        if(dati == None):
            raise ExamException('Il tipo di dato in input non può essere None')
        if(type(dati) != list):
            raise ExamException('I dati forniti devono essere una lista')
        if(len(dati) == 0):
            raise ExamException('Deve esserci almeno un dato')
        if(self.window > len(dati)):
            raise ExamException('La lunghezza della finestra deve essere minore di quella dei dati')
        for i in dati:
            if(type(i) != int and type(i) != float):
                raise ExamException('I dati forniti non sono numerici')
    def compute(self, dati):
        self.checkDati(dati)
        result = []
        for i in range(len(dati) - (self.window - 1)):
            sparz = 0
            for j in range(self.window):
                sparz += dati[i + j]
            result.append(sparz/self.window)
        return result


            