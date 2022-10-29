class Nave:
    def __init__(self,velocidad,tripulacion,transporte):
        self.velocidad=velocidad
        self.tripulacion=tripulacion
        self.transporte = transporte

class HalconMilenario(Nave):
    def __init__(self):
        self.velocidad=1050
        self.tripulacion=4
        self.transporte=1000
    
    def __str__(self):
        print('El Halcon Milenario consta de las siguientes caracteristicas:\n'
              f'Velocidad maxima >>> {self.velocidad} km/h\n'
              f'Tripulacion >>> {self.tripulacion} entes\n'
              f'Capacidad de transporte >>> {self.transporte} kg\n')
        
class EstrellaDeLaMuerte:
    def __init__(self):
        self.nave1=Nave(1000,3,600)
        self.nave2=Nave(600,6,5000)
        self.nave3=Nave(750,40,1050)
        self.nave4=Nave(1100,2,500)
        self.nave5=Nave(100,10,1000)
        self.listadonaves=[self.nave1,self.nave2,self.nave3,self.nave4,self.nave5]

    def __str__(self):
        print('La Estrella de la Muerte consta de 4 naves')
        for i in self.listadonaves:
            print(f'La nave {i} consta de los siguiente:\n'
                  f'Velocidad maxima >>> {i.velocidad} km/h\n'
                  f'Tripulacion >>> {i.tripulacion} entes\n'
                  f'Capacidad de transporte >>> {i.transporte} kg\n')       
    
    def printa_nave(self,nav):
        print('El Halcon Milenario consta de las siguientes caracteristicas:\n'
              f'Velocidad maxima >>> {nav.velocidad} km/h\n'
              f'Tripulacion >>> {nav.tripulacion} entes\n'
              f'Capacidad de transporte >>> {nav.transporte} kg\n')