import os, sys

def salir():
    controls=True
    os.system("cls")
    while controls==True:
        print(" ")
        print(" ")
        conf_salida = input("--------->   Está seguro que quiere salir?   <---------   ( 1 = si / 2 = no ):")
        if conf_salida.isdigit():
            conf_salida=int(conf_salida)
            if conf_salida == 1:
                os.system("cls")
                print(" ")
                print("----------------> Gracias por haber usado este software <----------------")
                print(" ")
                print(" ")
                sys.exit()
            elif conf_salida == 2:
                os.system("cls")
                break
            else:
                print("La opción ingresada no es válida, elige entre 1 ó 2")
        else:
            print("La opción ingresada no es válida, elige entre 1 ó 2")

