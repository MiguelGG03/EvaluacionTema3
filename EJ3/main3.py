from clasesej3 import (HalconMilenario,EstrellaDeLaMuerte)

def listador(lista):
    cont=1000000
    for alg in lista:
        if(alg.tripulacion < cont):
            cont=alg.tripulacion
    
    for i in lista:
        if(i.tripulacion==cont):
            lista.remove(i)
    
    return lista



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
    lista_trip=listador(lista)
    for i in lista_trip:
        print(f'Tripulacion >>> {i.tripulacion} entes')
    print('\n================================')
    print('NAVES MAYOR NUMERO DE TRIPULACION')
    print('================================\n')
    lista_trip=listador(lista)
    for i in lista_trip:
        print(f'Tripulacion >>> {i.tripulacion} entes')
    print('\n================================\n')
        



if __name__=='__main__':
    main3()