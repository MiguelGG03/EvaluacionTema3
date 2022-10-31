class Nodo(object):
    
        info,sig=None,None

class datoPolinomio(object):
    '''Clase dato polinomio'''

    def __init__(self,valor,termino):
        '''Crea un dato polinomio con valor y termino'''
        self.valor=valor
        self.termino=termino

class Polinomio(object):
    '''Clase Polinomio'''

    def __init__(self):
        '''Crea un polinomio del grado cero'''
        self.termino_mayor=None
        self.grado=-1
    
