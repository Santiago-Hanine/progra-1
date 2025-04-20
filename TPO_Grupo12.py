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
    print("Seleccione su artista")
    for evento in eventos:
        print("%d. %s" % (eventos.index(evento) + 1, evento[0]))
    
    opcion_elegida = int(input("Ingrese el numero del evento: "))
    while opcion_elegida < 1 or opcion_elegida > len(eventos):
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        opcion_elegida = int(input("Ingrese el numero del evento: "))
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
            print("Campo: ", evento[2][1])
            print("Platea Alta: ", evento[3][1])
            print("Platea Baja: ", evento[4][1])
            return True
    return False


def seleccionar_sector(artista):
    """"Mestra las opciones del menu sector y le pide al usuario que ingrese su opcion"""""
    print ("Seleccione el sector:")
    print("Sectores: ")
    print("1. Campo")
    print("2. Platea Alta")
    print("3. Platea Baja")
    opcion_sector = int(input("Ingrese el sector: "))
    while opcion_sector < 1 or opcion_sector > 3:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        opcion_sector = int(input("Ingrese el sector: "))
    disponibilidad = comporobar_disponibilidad(artista, opcion_sector)
    if (disponibilidad):
        print("El sector tiene disponibilidad")
        print("Disponibilidad:", eventos[artista - 1][opcion_sector + 1][1], "entradas disponibles")
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
        return False

def modificar_precio():
    """"Modifica el precio de un sector"""""
    print("---------------------------")
    artista = int(seleccionar_artistas(eventos))
    if artista == -1:
        return
    sector = seleccionar_sector(artista)
    nuevo_precio = int(input("Ingrese el nuevo precio: "))
    while nuevo_precio <= 0:
        print("El precio no puede ser negativo ni cero.")
        nuevo_precio = int(input("Ingrese el nuevo precio: "))
    if sector == 2:
        eventos[artista - 1][2][0] = nuevo_precio
        print("Precio Campo actualizado a: ", nuevo_precio)
    elif sector == 3:
        eventos[artista - 1][3][0] = nuevo_precio
        print("Precio Platea Alta actualizado a: ", nuevo_precio)
    elif sector == 4:
        eventos[artista - 1][4][0] = nuevo_precio
        print("Precio Platea Baja actualizado a: ", nuevo_precio)

def agregar_artistas(nombre, fechas,disponibilidad_campo, precio_campo, disponibilidad_platea_alta ,precio_platea_alta, disponibilidad_platea_baja, precio_platea_baja):
    """"Agrega un artista al sistema"""""
    nuevo_artista = [nombre, fechas,[disponibilidad_campo ,precio_campo], [disponibilidad_platea_alta ,precio_platea_alta], [disponibilidad_platea_baja,precio_platea_baja]]
    eventos.append(nuevo_artista)
    print("Artista agregado con exito. ")

def modificar_disponibilidad():
    """"Modifica la disponibilidad de un sector"""""
    print("---------------------------")
    artista = int(seleccionar_artistas(eventos))
    sector =int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
    while sector != 1 and sector != 2 and sector != 3:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
    nueva_disponibilidad = int(input("Ingrese la nueva disponibilidad: "))
    while nueva_disponibilidad < 0:
        print("La disponibilidad no puede ser negativa.")
        nueva_disponibilidad = int(input("Ingrese la nueva disponibilidad: "))
    if sector == 1:
        eventos[artista - 1][2][1] = nueva_disponibilidad
        print("Disponibilidad Campo actualizado a: ", nueva_disponibilidad)
    elif sector == 2:
        eventos[artista - 1][3][1] = nueva_disponibilidad
        print("Disponibilidad Platea Alta actualizado a: ", nueva_disponibilidad)
    elif sector == 3:
        eventos[artista - 1][4][1] = nueva_disponibilidad
        print("Disponibilidad Platea Baja actualizado a: ", nueva_disponibilidad)


#PROGRAMA PRINCIPAL
def main():
    opcion = ""
    while opcion != "0":
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Ver artistas")
        print('[2] Filtar artistas por precio')
        print("[9] Ingresar Administrador")
        print("---------------------------")
        print("[0] Salir del programa")
        print()

        opcion = int(input("Seleccione una opción: "))
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 9 and opcion != 0:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            opcion = int(input("Seleccione una opción: "))
        if opcion == 0:
            print("Gracias por usar el sistema de venta de entradas.")
            print("Hasta luego!")
            return
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 9:
            if opcion == 1:
                artista = int(seleccionar_artistas(eventos))
                print("Artista elegido: ", eventos[artista - 1][0])
                print("---------------------------")
                print("Que desea hacer?")
                print("---------------------------")
                print("[1] Proceder con la compra")
                print("[2] Ver fechas disponibles")
                print("[3] Ver entradas disponibles")
                opcion_elegida = int(input('Seleccione una opcion: '))
                while opcion_elegida != 1 and opcion_elegida != 2 and opcion_elegida != 3:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    opcion_elegida = int(input('Seleccione una opcion: '))
            
                if(opcion_elegida == 1):
                    sector = seleccionar_sector(artista)
                    while sector == False:
                        print("Sector sin entradas disponibles.")
                        sector = seleccionar_sector(artista)
                    print("Sector elegido con exito.", )
                    cantidad_de_entradas = int(input("Ingrese la cantidad de entradas: "))
                    while cantidad_de_entradas > eventos[artista - 1][sector][1]:
                        print("No hay disponibilidad suficiente.")
                        cantidad_de_entradas = int(input("Ingrese la cantidad de entradas: "))
                    while cantidad_de_entradas <= 0:
                        print("La cantidad de entradas no puede ser negativa ni cero.")
                        cantidad_de_entradas = int(input("Ingrese la cantidad de entradas: "))
                    print("Cantidad de entradas elegida: ", cantidad_de_entradas)
                    print()
                    print("Total a pagar: ", cantidad_de_entradas * eventos[artista - 1][sector][0])
                    print("Entradas compradas con exito.")
                    print("Gracias por su compra!")
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

            elif opcion == 2:  # Opción 2
                print("Filtrar artistas por precio")
                print("---------------------------")
                opcion_de_filtro = input("Desea filtrar por mayor o menor precio? mayor/menor: ")
                while opcion_de_filtro != "mayor" and opcion_de_filtro != "menor":
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    opcion_de_filtro = input("Desea filtrar por mayor o menor precio? mayor/menor ")
                precio = int(input("Ingrese el precio: "))
                while precio <= 0:
                    print("El precio no puede ser negativo ni cero.")
                    precio = int(input("Ingrese el precio: "))
                tipo_de_sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
                while tipo_de_sector != 1 and tipo_de_sector != 2 and tipo_de_sector != 3:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    tipo_de_sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
                if opcion_de_filtro == "mayor":
                    print("Artistas con precios mayores a ", precio)
                    artistas_filtrados = list(filter(lambda x: x[tipo_de_sector + 1][0] > precio, eventos))
                    if len(artistas_filtrados) == 0:
                        print("No hay artistas con precios menores a ", precio)
                    else:
                        print("------------------------")
                        for artista in artistas_filtrados:
                            print("Artista: ", artista[0])
                            print("Precio: ", artista[tipo_de_sector + 1][0])
                            print("------------------------")
                elif opcion_de_filtro == "menor":
                    artistas_filtrados = list(filter(lambda x: x[tipo_de_sector + 1][0] < precio, eventos))
                    if len(artistas_filtrados) == 0:
                        print("No hay artistas con precios menores a ", precio)
                    else:
                        print("------------------------")
                        for artista in artistas_filtrados:
                            print("Artista: ", artista[0])
                            print("Precio: ", artista[tipo_de_sector + 1][0])
                            print("------------------------")

            elif opcion == 9:   # Opción 9
                print()
                print("Ingreso de administrador")
                print("---------------------------")
                print("Ingrese su usuario: ")
                usuario = input()
                print("Ingrese su contraseña: ")
                contrasena = input()
                if usuario == "admin" and contrasena == "admin":
                    opcion_administrador = ""
                    while opcion_administrador != 0:
                        print()
                        print("Bienvenido Administrador")
                        print("---------------------------")
                        print("1. Modificar precios")
                        print("2. Modificar disponibilidad")
                        print("3. Agregar artistas")
                        print("---------------------------")
                        print("0. Salir")
                        print("---------------------------")
                        opcion_administrador = int(input('Seleccione una opcion: '))
                        while opcion_administrador != 1 and opcion_administrador != 2 and opcion_administrador != 3 and opcion_administrador != 0:
                            print("Opción no válida. Por favor, seleccione una opción del menú.")
                            opcion_administrador = int(input('Seleccione una opcion: '))
                        if opcion_administrador == 0:
                            print("Gracias por usar el sistema de venta de entradas.")
                            print("Hasta luego!")
                        if opcion_administrador == 1:
                            print("Modificar precios")
                            modificar_precio()
                        elif opcion_administrador == 2:
                            print("Modificar disponibilidad")
                            modificar_disponibilidad()
                        elif opcion_administrador == 3:
                            nombre = input("Ingrese el nombre del artista: ")
                            while nombre == "":
                                print("El nombre no puede estar vacío.")
                                nombre = input("Ingrese el nombre del artista: ")
                            fechas = input("Ingrese las fechas del artista (separadas por comas) dd/mm/yy: ").split(",")
                            while len(fechas) == 0 or any(fechas) == "":
                                print("Las fechas no pueden estar vacías.")
                                fechas = input("Ingrese las fechas del artista (separadas por comas): ").split(",")
                            precio_campo = int(input("Ingrese el precio del campo: "))
                            while precio_campo <= 0 or precio_campo == "":
                                print("El precio no puede ser negativo ni cero.")
                                precio_campo = int(input("Ingrese el precio del campo: "))
                            disponibilidad_campo = int(input("Ingrese la disponibilidad del campo: "))
                            while disponibilidad_campo < 0 or disponibilidad_campo == "":
                                print("La disponibilidad no puede ser negativa.")
                                disponibilidad_campo = int(input("Ingrese la disponibilidad del campo: "))
                            precio_platea_alta = int(input("Ingrese el precio de la platea alta: "))
                            while precio_platea_alta <= 0 or precio_platea_alta == "":
                                print("El precio no puede ser negativo ni cero.")
                                precio_platea_alta = int(input("Ingrese el precio de la platea alta: "))
                            disponibilidad_platea_alta = int(input("Ingrese la disponibilidad de la platea alta: "))
                            while disponibilidad_platea_alta < 0 or disponibilidad_platea_alta == "":
                                print("La disponibilidad no puede ser negativa.")
                                disponibilidad_platea_alta = int(input("Ingrese la disponibilidad de la platea alta: "))
                            precio_platea_baja = int(input("Ingrese el precio de la platea baja: "))
                            while precio_platea_baja <= 0 or precio_platea_baja == "":
                                print("El precio no puede ser negativo ni cero.")
                                precio_platea_baja = int(input("Ingrese el precio de la platea baja: "))
                            disponibilidad_platea_baja = int(input("Ingrese la disponibilidad de la platea baja: "))
                            while disponibilidad_platea_baja < 0 or disponibilidad_platea_baja == "":
                                print("La disponibilidad no puede ser negativa.")
                                disponibilidad_platea_baja = int(input("Ingrese la disponibilidad de la platea baja: "))
                            agregar_artistas(nombre, fechas,disponibilidad_campo, precio_campo, disponibilidad_platea_alta ,precio_platea_alta, disponibilidad_platea_baja, precio_platea_baja)
                            print("Listado actualizado con exito.")
                            for evento in eventos:
                                print("Artista:", evento[0])
                                print("Fechas:", ", ".join(evento[1]))
                                print("Campo: $", evento[2][0], "(", evento[2][1], "disponibles)")
                                print("Platea Alta: $", evento[3][0], "(", evento[3][1], "disponibles)")
                                print("Platea Baja: $", evento[4][0], "(", evento[4][1], "disponibles)")
                                print("-" * 40)
                else:
                    print("Usuario o contraseña incorrectos.")


# Matriz de eventos
eventos = [
    # Artista, Fechas donde toca     , Precio y disponibilidad de entradas (Campo, platea alta, platea baja )
    ['Tini', ['22/04/25', '23/04/25'], [2000, 1000], [3000, 200], [3500, 100]],
    ['Duki', ['25/04/25', '26/04/25'], [1300, 400], [2500, 400], [1500, 800]],
    ['Airbag', ['28/04/25', '29/04/25'], [2000, 200], [4000, 450], [1500, 200]]
]


# Punto de entrada al programa
main()
