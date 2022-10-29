from clasesej3 import (HalconMilenario,EstrellaDeLaMuerte)

def listador(lista):
    cont=1000000
    print(lista)
    for alg in lista:
        if(alg.tripulacion < cont):
            cont=alg.tripulacion
    
    for i in lista:
        if(i.tripulacion==cont):
            lista.remove(i)
    
    print(lista)
    return lista
        
        

        

def main3():
    ds=EstrellaDeLaMuerte()
    hm=HalconMilenario()
    lista_trip=[ds.nave1,ds.nave2,ds.nave3,ds.nave4,ds.nave5,hm]
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
    print(listador(lista_trip))




if __name__=='__main__':
    main3()