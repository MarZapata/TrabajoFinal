import pickle, os


def ticketconsulta(ruta):
    with open(ruta, "rb") as f:
            t_d4=pickle.load(f)
            f.close()
    print("====================================================================================")
    print(f'                         Recuperado el ticket:{t_d4["numeroticket"]}')
    print("====================================================================================")
    print(" ")
    print(f'Generado por:{t_d4["nombre"].upper()}')
    print(f'Del sector:{t_d4["sector"].upper()}')
    print(f'Asunto:{t_d4["asunto"].upper()}')
    print(f'Mensaje:{t_d4["mensaje"].upper()}')
    print(" ")
    print("====================================================================================")
    print("                      Gracias por usar el sistema de consulta")
    print("====================================================================================")
    print(" ")
    print(" ")

    while True:
        consultarotro= input("--------->   Querés consultar otro ticket?   <---------   ( 1 = si / 2 = no ):")
        if consultarotro.isdigit():
            consultarotro=int(consultarotro)
            if consultarotro == 1:
                os.system("cls")
                print(" ")
                print(" ")
                num_ticket =input("----->Ingresa el número del ticket a consultar:")
                ruta = f"tickets/ticket_{num_ticket}"
                ticketconsulta(ruta)
            elif consultarotro == 2:
                os.system("cls")
                break
            else:
                print("La opción ingresada no es válida, elegí entre 1 ó 2")
        else:
            print("La opción ingresada no es válida, elegí entre 1 ó 2")



