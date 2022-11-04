import hashlib
from EJ5.tablas_hash import Hash

def valido(caracter):
    if(ord(caracter)<32 or ord(caracter)>125):
        return False
    else:
        return True


def sl():
    print('\n')

def main5():
    mensaje=input('Mensaje a encriptar\n>>> ')
    encript=Hash()
    tabla=encript.crear_tabla(len(mensaje))
    encript.__str__()
    print(encript.encriptador(mensaje))
    cont=0
    for i in mensaje:
        if(valido(i)):
            encript.agregar(tabla,encript.encriptador(i),cont)
            cont+=1
        else:
            encript.agregar(tabla,encript.encriptador(' '),cont)
            cont+=1

        
    for i in mensaje:
        if(valido(i)==False):
            print(f'Caracter {i} no valido, sustituido con un espacio ` ´')
        else:
            print(f'Caracter {i} añadido al encriptado con exito')
            
    '''A partir de aqui tengo una tabla en la que 
    cada casilla representa un caracter encriptado'''
    sl()
    print('Datos encriptados en lista >>> ',tabla)
    sl()

    '''Ahora toca desencriptar'''
    lista_desencrptada=[]
    for i in tabla:
        for j in range(32,126):
            if(encript.encriptador(chr(j))==i):
                lista_desencrptada.append(chr(j))
    separador=''
    x=separador.join(lista_desencrptada)
    print(f'Tabla de elementos encriptados >>> {lista_desencrptada}')
    print()    
    print(f'Mensaje desencriptado >>> {x}')
    



if __name__=='__main__':
    main5()