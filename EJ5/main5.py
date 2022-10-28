import hashlib
from tablas_hash import Hash

def sl():
    print('\n')

def main5():
    h='hola'
    print(int(hashlib.sha256(h.encode('utf-8')).hexdigest(),16))
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



if __name__=='__main__':
    main5()