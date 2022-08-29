class Relogio:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.ligado = False 
    
    def ajustarHoras(self):
        pass


    def ajustarMinutos(self):
        pass

    def turnOn_turnOff(self):
        self.ligar = False
        self.desligar = False
    
    def whatTimeIs(self):
        if self.ligado == True:
            print (f'Hora atual: {self.hora}:{self.minuto}')
        else:
            print("Ligar relógio")

            
    def updateHour(self):
        pass
    
r1 = Relogio()
r1.whatTimeIs()