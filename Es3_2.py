class Veicolo():
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
    
    def __str__(self):
        return 'marca: {}, modello :{}, anno: {}, velocità: {}'.format(self.marca, self.modello, self.anno, self.speed)
    
    def accelerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
    
    def getspeed(self):
        return(self.speed)
    
class Macchina(Veicolo):
    def __init__(self, anno , modello, marca, numero_porte):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
        self.numero_porte = numero_porte
    
    def __str__(self):
        return 'marca: {}, modello :{}, anno: {}, velocità: {}, numero di porte: {}'.format(self.marca, self.modello, self.anno, self.speed, self.numero_porte)

class Moto(Veicolo):
    def __init__(self, anno, modello, marca, tipo):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
        self.tipo = tipo
    
    def __str__(self):
        return 'marca: {}, modello: {}, anno: {}, velocità: {}, tipo: {}'.format(self.marca, self.modello, self.anno, self.speed, self.tipo)

    
ferrari = Macchina('2023', 'Purosangue', 'Ferrari', '3')
print(ferrari.getspeed())
ferrari.accelerare()
ferrari.accelerare()
print(ferrari.getspeed())
ferrari.frenare()
print(ferrari.getspeed())
print(ferrari)

harley = Moto('1995', 'Harley Davidson', 'HD', 'Touring')
print(harley)