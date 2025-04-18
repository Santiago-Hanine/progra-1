def seleccionar_artistas():
    """"Mestra las opciones del menu artirta y le pide al usuario que ingrese su opcion"""""
    print("seleccione su artista")
    print("1. Tini ", end="")
    print("2. Duki", end="")
    print("3. Airbag",end="")


def seleccionar_fecha():
    """"Mestra las opciones del menu fecha y le pide al usuario que ingrese su opcion"""""

    print("seleccione la fecha")
    print("1. 22/04/25", end="")
    print("2. 25/04/25", end="")
    print("3. 28/04/25", end="")


def seleccionar_sector():
    """"Mestra las opciones del menu sector y le pide al usuario que ingrese su opcion"""""
    print ("seleccione el sector")
    print ("1. Campo", end="",)
    print("2. Platea Alta", end="")
    print("3. Platea Baja", end="")

    """"Comprueba si un sector tiene cupos para la cantidad requerida"""""
    if opcion_sector == "1":
        if capacidades["campo"] == 0:
            print("AGOTADO")
            return False
        else:
            return True
    elif opcion_sector == "2":
        if capacidades["platea_alta"] == 0:
            print("AGOTADO")
            return False
        else:
            return True
    elif opcion_sector == "3":
        if capacidades["platea_baja"] == 0:
            print("AGOTADO")
            return False
        else:
            return True



def calcular_precio(opcion_sector):
    """"Devuelve el precio unitario según el sector"""""
    if opcion_sector == "1":
        return precios["campo"]
    elif opcion_sector == "2":
        return precios["platea_alta"]
    elif opcion_sector == "3":
        return precios["platea_baja"]


capacidades = {

    "campo": 20000,
    "platea_alta": 30000,
    "platea_baja": 30000
}

precios = {
    "campo": 60000,
    "platea_alta": 50000,
    "platea_baja": 90000
}

eventos = {
    "tini": {
        "22/4/2025",

    },
    "duki": {
        "25/4/2025",


    },
    "airbag":{

        "28/4/2025",

    }
}


#PROGRAMA PRINCIPAL

while True:
    opciones = 4
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Ver artistas")
        print("[2] Disponibilidad de entradas")
        print("[3] Gestionar compra de entradas ")
        print("---------------------------")
        print("[0] Salir del programa")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción salir del programa
        exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":
        opcion_artista=int(input("Ingrese el show del artista: "))
        seleccionar_artistas(eventos)
        # Opción 1

    elif opcion == "2":   # Opción 2
        opcion_sector=int(input("Ingrese el sector: "))
        seleccionar_sector()

    elif opcion == "3":   # Opción 3
        opcion_fecha=int(input("Ingrese la fecha: "))
        seleccionar_fecha()

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")


# Punto de entrada al programa



main()
print("BIENVENIDO AL ESTADIO ....")






