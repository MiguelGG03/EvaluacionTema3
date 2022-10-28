class Nave:
    def __init__(self,velocidad,tripulacion,transporte):
        self.velocidad=velocidad
        self.tripulacion=tripulacion
        self.transporte = transporte

class HalconMilenario(Nave):
    def __init__(self, velocidad, tripulacion, transporte):
        super().__init__(velocidad,tripulacion,transporte)
        self.velocidad=1050
        self.tripulacion=4
        self.transporte=1000

class EstrellaDeLaMuerte:
    def __init__(self):
        self.nave1=Nave(1000,3,600)
        self.nave2=Nave(600,6,5000)
        self.nave3=Nave(750,40,1050)
        self.nave4=Nave(1100,2,500)
