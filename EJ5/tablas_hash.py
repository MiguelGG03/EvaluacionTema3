import hashlib

class hashNodo(object):

    info , sig = None , None


class Hash(object):

    def __init__(self):
        self.tabla=[]
        self.tamanio=0

    def bernstein(self,cadena):
        '''Solo Funciona para cadenas de caracteres'''
        h=0
        for caracter in cadena:
            h = h *33 + ord(caracter)
        return h

    def encriptador(self,dato):
        '''Encripta el texto'''
        resultado=int(hashlib.sha256(dato.encode('utf-8')).hexdigest(), 16) % 10**8
        return resultado
    

    def crear_tabla(self,tamanio):
        self.tabla=[None]*tamanio
        self.tamanio=tamanio
        return self.tabla

    def __str__(self):
        return print(self.tabla)
    
    def cantidad_elementos(self):
        return self.tamanio-self.tabla.count(None)

    def agregar(self,tabla,dato,posicion):
        '''Agrega un elemento a la tabla'''
        
        if(tabla[posicion] is None):
            tabla[posicion]=dato
            print(f'{dato} instertado con exito a la tabla en la posicion {posicion}')
            self.tabla=tabla
        else:
            aux2=tabla[posicion]
            while(aux2.sig!=None):
                aux2=aux2.sig            
            aux2.sig=aux
            print(f'Se ha adherido ({aux2.info}) a la cola con exito, su puntero apunta a ({aux2.sig.info}),\nel cual apunta a (None)')
            print(f'Ahora el nodo ({aux2.info}) apunta hacia ({aux2.sig.info})')
            self.tabla=tabla