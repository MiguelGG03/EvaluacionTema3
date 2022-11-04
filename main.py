from EJ1.main1 import main1
from EJ2.main2 import main2
from EJ3.main3 import main3
from EJ5.main5 import main5
from EJ4.main4 import main4
import sys


def main():

    pr1=input('Que ejercicio deseas ver (1,2,3,4,5): ')

    if pr1=='1':
        main1()
    elif pr1=='2':
        main2()
    elif pr1=='3':
        main3()
    elif pr1=='4':
        main4()
    elif pr1=='5':
        main5()
    else:
        print('Respuesta incorrecta')



if __name__=='__main__':
    main()