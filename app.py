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
    fechas = []
    for evento in eventos[artista - 1][1]:
        fechas.append(evento)
    return fechas

def ver_entradas_disponibles(opcion_fecha):
    """"Muestra las entradas disponibles para la fecha elegida"""""
    print("Entradas disponibles para la fecha: ", opcion_fecha)
    for evento in eventos:
        if opcion_fecha in evento[1]:
            print("Campo: ", evento[2][0])
            print("Platea Alta: ", evento[3][0])
            print("Platea Baja: ", evento[4][0])
            return True
    return False


def seleccionar_sector(artista):
    """"Mestra las opciones del menu sector y le pide al usuario que ingrese su opcion"""""
    print ("Seleccione el sector:")
    print("Sectores: ")
    print("1. Campo:")
    print("2. Platea Alta:")
    print("3. Platea Baja:")
    opcion_sector = int(input("Ingrese el sector: "))
    disponibilidad = comporobar_disponibilidad(artista, opcion_sector)
    if (disponibilidad):
        print("El sector tiene disponibilidad")
        if (opcion_sector == 1):
            print("Precio Campo: ", eventos[artista - 1][2][0])
            return 2
        elif (opcion_sector == 2):
            print("Precio Platea Alta: ", eventos[artista - 1][3][0])
            return 3
        elif (opcion_sector == 3):
            print("Precio Platea Baja: ", eventos[artista - 1][4][0])
            return 4
    else:
        print("El sector no tiene disponibilidad")
        return "No hay disponibilidad"

def modificar_precio():
    """"Modifica el precio de un sector"""""
    print("Modificar precios")
    print("---------------------------")
    artista = int(seleccionar_artistas(eventos))
    if artista == -1:
        return
    sector = seleccionar_sector(artista)
    nuevo_precio = int(input("Ingrese el nuevo precio: "))
    if sector == 2:
        eventos[artista - 1][2][1] = nuevo_precio
        print("Precio Campo actualizado a: ", nuevo_precio)
    elif sector == 3:
        eventos[artista - 1][3][1] = nuevo_precio
        print("Precio Platea Alta actualizado a: ", nuevo_precio)
    elif sector == 4:
        eventos[artista - 1][4][1] = nuevo_precio
        print("Precio Platea Baja actualizado a: ", nuevo_precio)

def agregar_artistas(nombre, fechas,disponibilidad_campo, precio_campo, disponibilidad_platea_alta ,precio_platea_alta, disponibilidad_platea_baja, precio_platea_baja):
    """"Agrega un artista al sistema"""""
    nuevo_artista = [nombre, fechas,[disponibilidad_campo ,precio_campo], [disponibilidad_platea_alta ,precio_platea_alta], [disponibilidad_platea_baja,precio_platea_baja]]
    eventos.append(nuevo_artista)
    print("Artista agregado: ")
    print("Nombre: ", nuevo_artista[0])
    print("Fechas: ")
    for fecha in nuevo_artista[1]:
        print("-", fecha)
    print("Precio Campo: ", nuevo_artista[2][0])
    print("Disponibilidad Campo: ", nuevo_artista[2][1])
    print("Precio Platea Alta: ", nuevo_artista[3][0])
    print("Disponibilidad Platea Alta: ", nuevo_artista[3][1])
    print("Precio Platea Baja: ", nuevo_artista[4][0])
    print("Disponibilidad Platea Baja: ", nuevo_artista[4][1])


eventos = [
    # Artista, Fechas donde toca     , Precio y disponibilidad de entradas (Campo, platea alta, platea baja )
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
        print("[2] Ingresar Administrador")
        print("---------------------------")
        print("[0] Salir del programa")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "1":
                artista = int(seleccionar_artistas(eventos))
                if artista == -1:
                    break
                print("Artista elegido: ", eventos[artista - 1][0])
                print("---------------------------")
                print("Que desea hacer?")
                print("---------------------------")
                print("[1] Proceder con la compra")
                print("[2] Ver fechas disponibles")
                print("[3] Ver entradas disponibles")
                opcion_elegida = int(input('Seleccione una opcion: '))
                
                if(opcion_elegida == 1):
                    sector = seleccionar_sector(artista)
                    if sector == 2:
                        print("Campo elegido: ", )
                    elif sector == 3:
                        print("Platea Alta elegida: ", )
                    elif sector == 4:
                        print("Platea Baja elegida: ", )
                elif(opcion_elegida == 2):
                    fechas = ver_fechas_del_artista(artista)
                    print('Fechas disponibles: ')
                    for fecha in fechas: 
                        print('-', fecha)
                            
                elif opcion_elegida == 3:
                    print("Ver entradas disponibles")
                    print("---------------------------")
                    print("Fechas Disponibles")
                    fechas_disponibles = ver_fechas_del_artista(artista)
                    for fecha in fechas_disponibles:
                        print(fecha)
                    opcion_fecha = input("Ingrese la fecha: ")
                    while opcion_fecha not in fechas_disponibles:
                        print("Fecha no valida")
                        opcion_fecha = input("Ingrese la fecha: ")
                    ver_entradas_disponibles(opcion_fecha)
                
            elif opcion == "2":   # Opción 2
                print()
                print("Ingreso de administrador")
                print("---------------------------")
                print("Ingrese su usuario: ")
                usuario = input()
                print("Ingrese su contraseña: ")
                contrasena = input()
                if usuario == "admin" and contrasena == "admin":
                    print()
                    print("Bienvenido Administrador")
                    print("---------------------------")
                    print("1. Modificar precios")
                    print("2. Modificar disponibilidad")
                    print("3. Agregar artistas")
                    print("---------------------------")
                    opcion_administrador = int(input('Seleccione una opcion: '))
                    if opcion_administrador == 1:
                        print("Modificar precios")
                        modificar_precio()
                    elif opcion_administrador == 2:
                        print("Modificar disponibilidad")
                        # Lógica para modificar disponibilidad
                    elif opcion_administrador == 3:
                        nombre = input("Ingrese el nombre del artista: ")
                        fechas = input("Ingrese las fechas del artista (separadas por comas): ").split(",")
                        precio_campo = int(input("Ingrese el precio del campo: "))
                        disponibilidad_campo = int(input("Ingrese la disponibilidad del campo: "))
                        precio_platea_alta = int(input("Ingrese el precio de la platea alta: "))
                        disponibilidad_platea_alta = int(input("Ingrese la disponibilidad de la platea alta: "))
                        precio_platea_baja = int(input("Ingrese el precio de la platea baja: "))
                        disponibilidad_platea_baja = int(input("Ingrese la disponibilidad de la platea baja: "))
                        agregar_artistas(nombre, fechas,disponibilidad_campo, precio_campo, disponibilidad_platea_alta ,precio_platea_alta, disponibilidad_platea_baja, precio_platea_baja)
                        print("Listado actualizado con exito.")
                        for evento in eventos:
                            print(evento[0], evento[1], evento[2], evento[3], evento[4], sep=" - ")
                else:
                    print("Usuario o contraseña incorrectos.")

        else:
            input("Opción inválida.")
    print()

    if opcion == "0": # Opción salir del programa
        print("Saliendo del programa...") # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    print("\n\n")


# Punto de entrada al programa



main()
print("BIENVENIDO AL ESTADIO ....")






