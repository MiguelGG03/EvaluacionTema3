from clasesej3 import (HalconMilenario,EstrellaDeLaMuerte)

def listador(algo):
    lista=[]
    hm=HalconMilenario()
    ds=EstrellaDeLaMuerte()
    lista.append(ds.nave1)
    lista.append(ds.nave2)
    lista.append(ds.nave3)
    lista.append(ds.nave4)
    lista.append(ds.nave5)
    cont=0
    for i in range(5):
        if(lista[i].tripulacion<cont):
            cont=lista[i].tripulacion

        

def main3():
    ds=EstrellaDeLaMuerte()
    hm=HalconMilenario()
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





if __name__=='__main__':
    main3()