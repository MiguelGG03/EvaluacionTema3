from clasesej3 import (Nave,HalconMilenario,EstrellaDeLaMuerte)

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


if __name__=='__main__':
    main3()