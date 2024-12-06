import pickle, os


def ticket(ruta):
    os.system("cls")
    with open(ruta, "rb") as f:
            t_d3=pickle.load(f)
            f.close()
    print("====================================================================================")
    print("                    Generado exitosamente el siguiente Ticket")
    print("====================================================================================")
    print(" ")
    print(f'Su nombre es:{t_d3["nombre"].upper()}')
    print(f'Su sector es:{t_d3["sector"].upper()}')
    print(f'Su asunto es:{t_d3["asunto"].upper()}')
    print(f'Su mensaje es:{t_d3["mensaje"].upper()}')
    print(" ")
    print("====================================================================================")
    print(f'                         Su número de ticket es:{t_d3["numeroticket"]}')
    print("              Favor de recordar este número para posibles consultas")
    print("====================================================================================")
    print(" ")
    print(" ")
    from genticket import genticket
    while True:
        consultaseguir= input("--------->   Querés crear otro ticket?   <---------   ( 1 = si / 2 = no ):")
        if consultaseguir.isdigit():
            consultaseguir=int(consultaseguir)
            if consultaseguir == 1:
                genticket()
            elif consultaseguir == 2:
                os.system("cls")
                break
            else:
                print("La opción ingresada no es válida, elegí entre 1 ó 2")
        else:
            print("La opción ingresada no es válida, elegí entre 1 ó 2")
