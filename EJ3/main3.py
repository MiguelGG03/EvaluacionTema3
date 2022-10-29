from clasesej3 import (HalconMilenario,EstrellaDeLaMuerte)

def listador_trip(lista):
    cont=1000000
    for alg in lista:
        if(alg.tripulacion < cont):
            cont=alg.tripulacion
    
    for i in lista:
        if(i.tripulacion==cont):
            lista.remove(i)
    
    return lista

def listador_min(lista):
    cont=0
    lista_nueva=[]
    for alg in lista:
        if(alg.tripmin > cont):
            cont=alg.tripmin
    
    for i in lista:
        if(i.tripmin==cont):
            lista_nueva.append(i)
    
    return lista_nueva

def listador_at(lista):
    cont=0
    lista_nueva=[]
    for alg in lista:
        if(alg.tripmin > cont):
            cont=alg.tripmin
    
    for i in lista:
        if(i.tripmin==cont):
            lista_nueva.append(i)
    
    return lista_nueva

def main3():
    ds=EstrellaDeLaMuerte()
    hm=HalconMilenario()
    lista=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
    print('================================')
    print('HACLON MILENARIO CARACTERISTICAS')
    print('================================\n')
    hm.__str__()
    print('================================')
    print('ESTRELLA DE LA MUERTE CARACTERIS.')
    print('================================\n')
    ds.__str__()
    print('================================')
    print('NAVES MAYOR NUMERO DE TRIPULACION')
    print('================================\n')
    lista_trip=listador_trip(lista)
    for i in lista_trip:
        print(f'Tripulacion >>> {i.tripulacion} entes')
    print('\n================================')
    print('NAVES MAYOR NUMERO DE TRIPULACION min')
    print('================================\n')
    lista_trip=listador_min(lista)
    for i in lista_trip:
        print(f'Tripulacion minima maxima >>> {i.tripulacion} entes')
    print('\n================================')
    print('NAVES CUYO NOMBRE COMIENZA CON AT')
    print('================================\n')
    lista_at=listador_at(lista)
    for i in lista_at:
        print(f'Naves que comienzan con AT >>> {i.tripulacion} ')
    print('\n================================\n')
        



if __name__=='__main__':
    main3()