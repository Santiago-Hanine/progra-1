import json

def cargar_eventos():
    try:
        archivo = open('Eventos.json', 'rt', encoding='utf-8')
        datos = json.load(archivo)
        archivo.close()
        return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error de formato en Eventos.json")
        return []

def guardar_eventos(eventos):
    try:
        archivo = open('Eventos.json', 'wt', encoding='utf-8')
        json.dump(eventos, archivo, indent=4)
        archivo.close()
    except Exception as error:
        print("Error al guardar los eventos:", error)

def seleccionar_artistas():
    eventos = cargar_eventos()
    if not eventos:
        print("No hay artistas disponibles.")
        return None
    print("Seleccione su artista")
    for i in range(len(eventos)):
        print(f"{i + 1}. {eventos[i][0]}")
    opcion = int(input("Ingrese el número del evento: "))
    while opcion < 1 or opcion > len(eventos):
        print("Opción inválida.")
        opcion = int(input("Ingrese el número del evento: "))
    return opcion - 1

def seleccionar_sector(indice_artista):
    eventos = cargar_eventos()
    artista = eventos[indice_artista]
    print("Seleccione el sector:")
    print("1. Campo")
    print("2. Platea Alta")
    print("3. Platea Baja")
    opcion = int(input("Ingrese el sector: "))
    while opcion not in [1, 2, 3]:
        print("Opción inválida.")
        opcion = int(input("Ingrese el sector: "))
    if artista[opcion + 1][1] > 0:
        print("Disponibilidad:", artista[opcion + 1][1])
        print("Precio:", artista[opcion + 1][0])
        return opcion + 1
    else:
        print("No hay disponibilidad en ese sector.")
        return None

def comprar_entradas():
    indice = seleccionar_artistas()
    if indice is None:
        return
    sector = seleccionar_sector(indice)
    if not sector:
        return
    eventos = cargar_eventos()
    max_disponible = eventos[indice][sector][1]
    cantidad = int(input("Cantidad de entradas: "))
    while cantidad < 1 or cantidad > max_disponible:
        print("Cantidad inválida.")
        cantidad = int(input("Cantidad de entradas: "))
    eventos[indice][sector][1] -= cantidad
    total = cantidad * eventos[indice][sector][0]
    guardar_eventos(eventos)
    print(f"Compra realizada con éxito. Total: ${total}")

def ver_fechas_del_artista(indice):
    eventos = cargar_eventos()
    return eventos[indice][1]

def ver_disponibilidad():
    indice = seleccionar_artistas()
    if indice is None:
        return
    eventos = cargar_eventos()
    artista = eventos[indice]
    print("Fechas disponibles:")
    for fecha in artista[1]:
        print("-", fecha)
    fecha_busqueda = input("Ingrese la fecha a consultar: ")
    if fecha_busqueda in artista[1]:
        print("Campo:", artista[2][1], "disponibles")
        print("Platea Alta:", artista[3][1], "disponibles")
        print("Platea Baja:", artista[4][1], "disponibles")
    else:
        print("Esa fecha no está disponible para este artista.")

def modificar_precio():
    indice = seleccionar_artistas()
    if indice is None:
        return
    sector = seleccionar_sector(indice)
    if not sector:
        return
    nuevo_precio = int(input("Nuevo precio: "))
    while nuevo_precio <= 0:
        nuevo_precio = int(input("Ingrese un precio válido: "))
    eventos = cargar_eventos()
    eventos[indice][sector][0] = nuevo_precio
    guardar_eventos(eventos)
    print("Precio actualizado correctamente.")

def modificar_disponibilidad():
    indice = seleccionar_artistas()
    if indice is None:
        return
    print("1. Campo\n2. Platea Alta\n3. Platea Baja")
    sector = int(input("Seleccione el sector: "))
    while sector not in [1, 2, 3]:
        sector = int(input("Seleccione un sector válido: "))
    nueva_disp = int(input("Nueva disponibilidad: "))
    while nueva_disp < 0:
        nueva_disp = int(input("Ingrese una cantidad válida: "))
    eventos = cargar_eventos()
    eventos[indice][sector + 1][1] = nueva_disp
    guardar_eventos(eventos)
    print("Disponibilidad actualizada correctamente.")

def agregar_artista():
    nombre = input("Nombre del artista: ")
    fechas = input("Fechas separadas por coma (ej: 10-06,11-06): ").split(',')
    campo_disp = int(input("Disponibilidad Campo: "))
    campo_precio = int(input("Precio Campo: "))
    alta_disp = int(input("Disponibilidad Platea Alta: "))
    alta_precio = int(input("Precio Platea Alta: "))
    baja_disp = int(input("Disponibilidad Platea Baja: "))
    baja_precio = int(input("Precio Platea Baja: "))
    nuevo = [nombre, fechas, [campo_precio, campo_disp], [alta_precio, alta_disp], [baja_precio, baja_disp]]
    eventos = cargar_eventos()
    eventos.append(nuevo)
    guardar_eventos(eventos)
    print("Artista agregado correctamente.")

def main():
    while True:
        print("\nMENÚ DEL SISTEMA")
        print("[1] Ver artistas y comprar entradas")
        print("[2] Ver disponibilidad por fecha")
        print("[3] Modificar precio (admin)")
        print("[4] Modificar disponibilidad (admin)")
        print("[5] Agregar artista (admin)")
        print("[0] Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 0:
            print("Gracias por usar el sistema.")
            break
        elif opcion == 1:
            comprar_entradas()
        elif opcion == 2:
            ver_disponibilidad()
        elif opcion == 3:
            modificar_precio()
        elif opcion == 4:
            modificar_disponibilidad()
        elif opcion == 5:
            agregar_artista()
        else:
            print("Opción no válida.")

main()
