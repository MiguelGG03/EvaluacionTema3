from EJ3.clasesej3 import (HalconMilenario,EstrellaDeLaMuerte)

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
    lista_nueva=[]
    for alg in lista:
        if(((alg.nombre[0] == 'A') or (alg.nombre[0] == 'a')) and ((alg.nombre[1] == 'T') or (alg.nombre[1] == 't'))):
           lista_nueva.append(alg)
    
    return lista_nueva

def listador_min_six(lista):
    lista_nueva=[]
    for alg in lista:
        if(alg.pasajeros >= 6):
            lista_nueva.append(alg)
    
    return lista_nueva

def listador_max_min(lista):
    lista_nueva=[]
    
    contmin=1000000
    for alg in lista:
        if(alg.tripulacion < contmin):
            contmin=alg.tripulacion
    contmax=0
    for alg in lista:
        if(alg.tripulacion > contmax):
            contmax=alg.tripulacion
    

    for i in lista:
        if(i.tripulacion==contmax or i.tripulacion==contmin):
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
    lista=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
    print('\n================================')
    print('NAVES MAYOR NUMERO DE TRIPULACION min')
    print('================================\n')
    lista_trip=listador_min(lista)
    for i in lista_trip:
        print(f'Tripulacion minima maxima >>> {i.tripulacion} entes')
    
    print('\n================================')
    print('NAVES CUYO NOMBRE EMPIEZA CON AT')
    print('================================\n')
    lista=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
    lista_at=listador_at(lista)
    for i in lista_at:
        print(f'Nave que empieza con AT >>> {i.nombre}')
    print('\n================================')
    print('NAVES MINIMO SEIS PASAJEROS')
    print('================================\n')
    lista=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
    lista_six=listador_min_six(lista)
    for i in lista_six:
        print(f'Nombre >>> {i.nombre} ; Pasajeros >>> {i.pasajeros}')
    print()
    print('\n================================')
    print('NAVES MAS GRANDE Y MAS PEQUEÑA \n   medidas por tripulacion')
    print('================================\n')
    lista=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
    lista_max_y_min=listador_max_min(lista)
    for i in lista_max_y_min:
        print(f'Nombre >>> {i.nombre}\nPasajeros >>> {i.pasajeros}\nVelocidad >>> {i.velocidad}\nTripulacion >>> {i.tripulacion}\nCarga de Transporte >>> {i.transporte}\nTripulacion Minima >>> {i.tripmin}\n')
    print()
   

        



if __name__=='__main__':
    main3()