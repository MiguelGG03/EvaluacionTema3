from tablas_hash import Hash

def main5():
    mensaje=input('Mensaje a encriptar\n>>>')
    encript=Hash()
    tabla=encript.crear_tabla(len(mensaje))
    encript.__str__()
    print(encript.encriptador(mensaje))
    cont=0
    for i in mensaje:
        h=encript.encriptador(i)
        encript.agregar(tabla,h,cont)
        cont+=1
    '''A partir de aqui tengo una tabla en la que 
    cada casilla representa un caracter encriptado'''
    print('Datos encriptados en lista >>> ',tabla)



if __name__=='__main__':
    main5()