import random, pickle, os
from ticket import ticket

def genticket():
    os.system("cls")
    u_ticket = str(input("----->Ingresa tu nombre:"))
    u_sector = str(input("----->Ingresa tu sector:"))
    u_asunto = str(input("----->Ingresa tu asunto:"))
    u_mensaje = str(input("----->Ingresa tu mensaje:"))
    numero_random = random.randrange(1000, 9999)
    nuevos_datos = {"nombre" : u_ticket,"sector":u_sector,"asunto":u_asunto,"mensaje": u_mensaje,"numeroticket": numero_random }
    ruta = "tickets/ticket_"+str(numero_random)
    with open(ruta, "wb") as f:
        pickle.dump(nuevos_datos, f)
    os.system("cls")
    ticket(ruta)
