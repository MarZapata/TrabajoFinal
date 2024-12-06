import os
from menu import menu
from salir import salir
from genticket import genticket
from ticketconsulta import ticketconsulta

def main():
    while True:
        os.system("cls")
        menu()
        seleccion_menu = input("Digite su selección:")
        os.system("cls")
        if seleccion_menu.isdigit():
            seleccion_menu=int(seleccion_menu)
            if seleccion_menu==1:
                genticket()
            elif seleccion_menu==2:
                num_ticket =input("----->Ingresa el número del ticket a consultar:")
                ruta = f"tickets/ticket_{num_ticket}"
                ticketconsulta(ruta)
            elif seleccion_menu==3:
                salir()   
            else:
                print("La opción ingresada no es válida, elige entre opción 1, 2 o 3")
        else:
            print("La opción ingresada no es válida, elige entre opción 1, 2 o 3")  
    os.system("cls")
    print(" ")
    print("----------------> Gracias por haber usado este software <----------------")

main()