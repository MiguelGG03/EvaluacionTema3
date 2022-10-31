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
    
'''Implementaciones para el polinomio'''

def agregar_termino(polinomio,termino,valor):
    '''Agregaun termino y su valor al polinomio'''
    aux=Nodo()
    dato=datoPolinomio()
    aux.info=dato
    if(termino > polinomio.grado):
        aux.sig= polinomio.termino_mayor
        polinomio.termino_mator=aux
        polinomio.grado= termino
    else:
        actual= polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual=actual.sig
        aux.sig=actual.sig
        actual.sig=aux

def modificar_termino(polinomio,termino,valor):
    '''Modifica el termino de un polinomio'''
    aux=polinomio.termino_mayor
    while(aux is not None and aux.info.termino!=termino):
        aux=aux.sig
    aux.info.valor=valor

def obtener_valor( polinomio,termino):
    '''Devuelve el valor de un termino del polinomio'''
    aux=polinomio.termino_mayor
    while(aux is not None and aux.info.termino > termino):
        aux=aux.sig
    if(aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0