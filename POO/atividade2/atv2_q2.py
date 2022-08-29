class Bike:
    def __init__(self, cor, marca, aro, altura_max_cela, calibragem_max):
        self.veloc_inicial = 0
        self.calibragem = 0
        self.cor = 0
        self.cor = cor
        self.marca = marca
        self.veloc_max = 90
        self.aro = aro
        self.altura_max_cela = altura_max_cela
        self.calibragem_max = calibragem_max

    def pedalar (self):
        if (veloc_inicial > 0 and veloc_max <= 90):
            print("pedalando")    

    def frear(self):

        if self.veloc_inicial < self.velc_atual < self.veloc_max:
            print("Parou")

    def parar (self):
        self.veloc_inicial = 0
    
    def ajustar_cela (self):
        if self.ajustar_cela >= self.altura_max_cela:
            print("Cela vai sair")
        elif (self.veloc_inicial == 0 and self.ajustar_cela <= self.altura_max_cela):
            print("Cela ajustada")
        

    def calibrarPneu (self, calibragemAtual):      

        if self.calibragemAtual == self.calibragem:
            print("Calibrar")
        elif self.calibragemAtual <= self.calibragem_max:
            print("NÃO PRECISA CALIBRAR")


        pass


b1 = Bike("amarela", "caloi", 26, 5, 28)
b1.pedalar ()

#mostrar a velocidade atual da bicicleta