import hashlib
from tablas_hash import Hash

def valido(caracter):
    if(ord(caracter)<32 or ord(caracter)>125):
        return False
    else:
        return True


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
        if(valido(i)):
            encript.agregar(tabla,encript.encriptador(i),cont)
            cont+=1
        
    for i in mensaje:
        if(valido(i)==False):
            print(f'Caracter {i} no valido')
        else:
            print(f'Caracter {i} añadido al encriptado con exito')
            
    '''A partir de aqui tengo una tabla en la que 
    cada casilla representa un caracter encriptado'''
    sl()
    print('Datos encriptados en lista >>> ',tabla)
    sl()

    '''Ahora toca desencriptar'''
    



if __name__=='__main__':
    main5()