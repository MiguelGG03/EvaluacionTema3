import hashlib
from tablas_hash import Hash

def valido(caracter):
    if(ord(caracter)<32 or ord(caracter)>125):
        return print('Caracter no valido')
    else:
        return print(f'Caracter valido >>> {caracter}')


def sl():
    print('\n')

def main5():
    h='hola'
    h1=int(hashlib.sha256(h.encode('utf-8')).hexdigest(),16)
    mensaje=input('Mensaje a encriptar\n>>>')
    encript=Hash()
    tabla=encript.crear_tabla(len(mensaje))
    encript.__str__()
    print(encript.encriptador(mensaje))
    cont=0
    for i in mensaje:
        h=encript.encriptador(i)
        sn=encript.checker(i)
        if(sn==True):
            encript.agregar(tabla,h,cont)
        else:
            return Exception(f'Caracter {i} no valido')
        cont+=1
    '''A partir de aqui tengo una tabla en la que 
    cada casilla representa un caracter encriptado'''
    sl()
    print('Datos encriptados en lista >>> ',tabla)
    sl()
    '''Ahora toca desencriptar'''
    #h2=int(hashlib.sha256(h1.encode('utf-8')).hexdigest(),16)
    #print(h2)
    for i in mensaje:
        valido(i)



if __name__=='__main__':
    main5()