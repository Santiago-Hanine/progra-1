def comporobar_disponibilidad(artista, opcion_sector):
    """"Comprueba si un sector tiene cupos para la cantidad requerida"""""
    if opcion_sector == 1:
        if eventos[artista - 1][2][1] == 0:
            return False
        else:
            return True
    elif opcion_sector == 2:
        if eventos[artista - 1][3][1] == 0:
            return False
        else:
            return True
    elif opcion_sector == 3:
        if eventos[artista - 1][4][1] == 0:
            return False
        else:
            return True

def seleccionar_artistas(eventos):
    """"Mestra las opciones del menu artirta y le pide al usuario que ingrese su opcion"""""
    print("seleccione su artista")
    opcion_elegida = 0
    for evento in eventos:
        print("%d. %s" % (eventos.index(evento) + 1, evento[0]))
    opcion_elegida = input("Ingrese el numero del evento o -1 para salir: ")
    return opcion_elegida


def ver_fechas_del_artista(artista):
    """"Mestra las fechas del artista elegido"""""
    print(eventos[artista - 1])
    fechas = []
    for evento in eventos[artista - 1][1]:
        fechas.append(evento)
    return fechas


def seleccionar_sector(artista):
    """"Mestra las opciones del menu sector y le pide al usuario que ingrese su opcion"""""
    print ("Seleccione el sector:")
    print("Sectores: ")
    print ("1. Campo")
    print("2. Platea Alta")
    print("3. Platea Baja")
    opcion_sector = int(input("Ingrese el sector: "))
    disponibilidad = comporobar_disponibilidad(artista, opcion_sector)
    if (disponibilidad):
        print("El sector tiene disponibilidad")
        print("Precio: ", eventos[artista - 1][opcion_sector][1])



# def calcular_precio(opcion_sector):
#     """"Devuelve el precio unitario según el sector"""""
#     if opcion_sector == "1":
#         return precios["campo"]
#     elif opcion_sector == "2":
#         return precios["platea_alta"]
#     elif opcion_sector == "3":
#         return precios["platea_baja"]

eventos = [
    # Artista, Fechas donde toca     , Disponibilidad y precio de entradas (Campo )
	['Tini', ['22/04/25', '23/04/25'], [2000, 1000], [3000, 200], [3500, 100]],
	['Duki', ['25/04/25', '26/04/25'], [1300, 400], [2500, 400], [1500, 800]],
	['Airbag', ['28/04/25', '29/04/25'], [2000, 200], [4000, 450], [1500, 200]]
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
        print("---------------------------")
        print("[0] Salir del programa")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "1":
                artista = int(seleccionar_artistas(eventos))
                print("---------------------------")
                print("Que desea hacer?")
                print("---------------------------")
                print("[1] Proceder con la compra")
                print("[2] Ver fechas disponibles")
                print("[3] Ver entradas disponibles")
                opcion_elegida = int(input('Seleccione una opcion: '))
                
                if(opcion_elegida == 1):
                        print(seleccionar_sector(artista))
                elif(opcion_elegida == 2):
                    fechas = ver_fechas_del_artista(artista)
                    print('Fechas disponibles: ')
                    for fecha in fechas: 
                        print(fecha)
                elif opcion_elegida == 3:
                    pass
                
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






