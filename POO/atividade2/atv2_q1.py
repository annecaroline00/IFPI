from tkinter import HORIZONTAL


class Relogio:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.ligado = False 
    
    def ajustarHoras(self, hora):
        if hora < 0:
            self.hora = 0
        elif hora > 23:
            while hora > 23:
                hora -= 23
            self.hora = hora 
        else:
            self.hora = hora
        


    def ajustarMinutos(self, minuto):
        if minuto < 0:
            self.minuto = 0 
        elif minuto > 59:
            while minuto > 59:
                minuto -= 59
            self.minuto = minuto
        else:
            self.minuto = minuto

    def turnOn_turnOff(self):
        self.ligar = False
        self.desligar = False
    
    def whatTimeIs(self):
        if self.ligado == True:
            print (f'Hora atual: {self.hora}:{self.minuto}')
        else:
            print("Ligar relógio")

            
    def updateHour(self):
        self.segundos += 1
		if self.segundos > 59:
			self.minutos += 1
			self.segundos = 0
		if self. minutos > 59:
			self.minutos = 0
			self.horas += 1
		if self.horas > 23:
			self.horas = 0

    
r1 = Relogio()
r1.whatTimeIs()
