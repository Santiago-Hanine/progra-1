def comporobar_disponibilidad(opcion_sector):
    """"Comprueba si un sector tiene cupos para la cantidad requerida"""""
    if opcion_sector == 1:
        if capacidades[0] == 0:
            print("AGOTADO")
            return "AGOTADO"
        else:
            return "DISPONIBLE"
    elif opcion_sector == 2:
        if capacidades[1] == 0:
            print("AGOTADO")
            return "AGOTADO"
        else:
            return "DISPONIBLE"
    elif opcion_sector == 3:
        if capacidades[2] == 0:
            print("AGOTADO")
            return "AGOTADO"
        else:
            return "DISPONIBLE"

def seleccionar_artistas(eventos):
    """"Mestra las opciones del menu artirta y le pide al usuario que ingrese su opcion"""""
    print("seleccione su artista")
    opcion_elegida = 0
    for evento in eventos:
        print("%d. %s" % (eventos.index(evento) + 1, evento[0]))
    opcion_elegida = input("Ingrese el numero del evento o -1 para salir: ")
    return opcion_elegida


def seleccionar_fecha():
    """"Mestra las opciones del menu fecha y le pide al usuario que ingrese su opcion"""""

    print("seleccione la fecha")
    print("1. 22/04/25", end="")
    print("2. 25/04/25", end="")
    print("3. 28/04/25", end="")


def seleccionar_sector():
    """"Mestra las opciones del menu sector y le pide al usuario que ingrese su opcion"""""
    print ("Seleccione el sector:")
    print ("1. Campo")
    print("2. Platea Alta")
    print("3. Platea Baja")
    opcion_sector = int(input("Ingrese el sector: "))
    disponibilidad = comporobar_disponibilidad(opcion_sector)
    return disponibilidad



def calcular_precio(opcion_sector):
    """"Devuelve el precio unitario según el sector"""""
    if opcion_sector == "1":
        return precios["campo"]
    elif opcion_sector == "2":
        return precios["platea_alta"]
    elif opcion_sector == "3":
        return precios["platea_baja"]


capacidades = [
    ["campo", 1000],
	["platea_alta", 500],
	["platea_baja", 300],
]

precios = [
    ["campo", 2000],
    ["platea_alta", 3000],
	["platea_baja", 4000]
]

eventos = [
	['Tini', '22/04/25'],
	['Duki', '25/04/25'],
	['Airbag', '28/04/25']
]


#PROGRAMA PRINCIPAL

def main():
    opciones = 4
    opcion = ""
    while opcion != "0":
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
            if opcion == "1":
                print(seleccionar_artistas(eventos))
        	# Opción 1

            elif opcion == "2":   # Opción 2
                print(seleccionar_sector())

            elif opcion == "3":   # Opción 3
                opcion_fecha = int(input("Ingrese la fecha: "))
                seleccionar_fecha()
        else:
            input("Opción inválida.")
    print()

    if opcion == "0": # Opción salir del programa
        print("Saliendo del programa...") # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    print("\n\n")


# Punto de entrada al programa



main()
print("BIENVENIDO AL ESTADIO ....")






