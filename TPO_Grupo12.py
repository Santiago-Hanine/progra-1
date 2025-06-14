import json
import random


def crear_asientos():
    # Cargar datos del archivo JSON
    with open('Eventos.json', 'r', encoding='utf-8') as archivo:
        eventos = json.load(archivo)
    
    # Mostrar lista de artistas disponibles
    print("\nArtistas disponibles:")
    artistas = []
    for id_evento, datos in eventos.items():
        if datos["Artista"] not in artistas:
            artistas.append(datos["Artista"])
            print(f"{len(artistas)}. {datos['Artista']}")
    
    # Selección del artista
    while True:
        try:
            opcion_artista = int(input("\nSeleccione el número del artista: ")) - 1
            if 0 <= opcion_artista < len(artistas):
                artista_seleccionado = artistas[opcion_artista]
                break
            else:
                print("Opción inválida. Por favor, seleccione un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Mostrar fechas disponibles para el artista seleccionado
    print(f"\nFechas disponibles para {artista_seleccionado}:")
    fechas_disponibles = []
    for id_evento, datos in eventos.items():
        if datos["Artista"] == artista_seleccionado:
            for fecha in datos["Fechas"]:
                if fecha not in fechas_disponibles:
                    fechas_disponibles.append(fecha)
                    print(f"{len(fechas_disponibles)}. {fecha}")
    
    # Selección de la fecha
    while True:
        try:
            opcion_fecha = int(input("\nSeleccione el número de la fecha: ")) - 1
            if 0 <= opcion_fecha < len(fechas_disponibles):
                fecha_seleccionada = fechas_disponibles[opcion_fecha]
                break
            else:
                print("Opción inválida. Por favor, seleccione un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print(f"\nAsientos disponibles para {artista_seleccionado} - {fecha_seleccionada}:")

    # Crear matrices con valores aleatorios 0 (disponible) y 1 (ocupado)
    platea_alta = [[random.choice([0, 1]) for _ in range(10)] for _ in range(10)]
    platea_baja = [[random.choice([0, 1]) for _ in range(10)] for _ in range(10)]

    # Mostrar disponibilidad
    print("\nPlatea Alta:")
    for fila in platea_alta:
        print(fila)
    print("\nPlatea Baja:")
    for fila in platea_baja:
        print(fila)
    
    return platea_alta, platea_baja




def creacion_usuario():
    nombre = input("Ingrese su nombre: ")
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese su nombre: ")
    dni = input("Ingrese su DNI: ")
    while len(dni) != 8:
        print("DNI no válido. Debe tener 8 dígitos.")
        dni = input("Ingrese su DNI: ")

    try: 
        entrada = open('usuarios.txt', 'rt', encoding='utf-8')
        linea = entrada.readline()
        while linea:
            linea = linea.strip()
            if linea:
                partes = linea.split(';')
                if len(partes) >= 2:
                    dni_existente = partes[0]
                    while dni_existente == dni:
                        print("El DNI ya está registrado. Por favor, ingrese otro.")
                        dni = input("Ingrese su DNI: ")
                else:
                    print("Línea mal formada:", linea)
            else:
                print("Línea mal formada:", linea)
            linea = entrada.readline()
            
    except FileNotFoundError:
        print("Error, archivo no encontrado.")
    finally:
        entrada.close()    
        
    try: 
        archivo = open('usuarios.txt', 'a', encoding='utf-8')
        archivo.write(dni + ';' + nombre + '\n')
        print(f"Usuario {nombre} creado exitosamente.")
        print("Bienvenido", nombre)
    except IOError:
        print("Error al escribir en el archivo usuarios.txt.")
    finally:
        archivo.close()

def ingreso_usuario():
    input_dni = input("Ingrese su DNI: ")
    while len(input_dni) != 8:
        print("DNI no válido. Debe tener 8 dígitos.")
        input_dni = input("Ingrese su DNI: ")

    try:
        archivo = open('usuarios.txt', 'rt', encoding='utf-8')
        linea = archivo.readline()
        while linea:
            linea = linea.strip()
            if linea:
                dni, nombre_apellido,eventos = linea.split(';')
                if dni == input_dni:
                    print()
                    print()
                    print(f"Bienvenido {nombre_apellido}")
                    return True
            
            else:
                print("Línea mal formada:", linea)
            linea = archivo.readline()
            return False
    except FileNotFoundError:
        print("El archivo usuarios.txt no existe.")
        return
    finally:
        archivo.close()

   

            

def cargar_eventos():
    """Carga los eventos desde el archivo JSON y los devuelve en la estructura de lista."""
    try:
        archivo = open('Eventos.json', 'rt', encoding='utf-8')
        eventos_json = json.load(archivo)
        archivo.close()

        lista_eventos = []
        i = 1
        while str(i) in eventos_json:
            evento = eventos_json[str(i)]
            # Construimos la estructura de lista que usas para cada evento
            nuevo_evento = [
                evento['Artista'],          # nombre artista
                evento['Fechas'],           # lista fechas
                [evento['Sectores']['Campo']['Precio'], evento['Sectores']['Campo']['Disponibilidad']],
                [evento['Sectores']['Platea Alta']['Precio'], evento['Sectores']['Platea Alta']['Disponibilidad']],
                [evento['Sectores']['Platea Baja']['Precio'], evento['Sectores']['Platea Baja']['Disponibilidad']]
            ]
            lista_eventos.append(nuevo_evento)
            i += 1
        return lista_eventos

    except FileNotFoundError:
        print("Archivo Eventos.json no encontrado. Se crea lista vacía.")
        return []
    except json.JSONDecodeError:
        print("Error al leer JSON. Verifica el formato.")
        return []

def guardar_eventos(eventos):
    """Guarda toda la lista de eventos en el archivo JSON con la estructura correcta."""
    data = {}
    i = 1
    while i <= len(eventos):
        evento = eventos[i-1]
        data[str(i)] = {
            'Artista': evento[0],
            'Fechas': evento[1],
            'Sectores': {
                'Campo': {
                    'Precio': evento[2][0],
                    'Disponibilidad': evento[2][1]
                },
                'Platea Alta': {
                    'Precio': evento[3][0],
                    'Disponibilidad': evento[3][1]
                },
                'Platea Baja': {
                    'Precio': evento[4][0],
                    'Disponibilidad': evento[4][1]
                }
            }
        }
        i += 1
    try:
        archivo = open('Eventos.json', 'wt', encoding='utf-8')
        json.dump(data, archivo, indent=4, ensure_ascii=False)
        archivo.close()
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Cargamos los eventos al inicio para trabajar con ellos
eventos = cargar_eventos()

def comprobar_disponibilidad(artista, opcion_sector):
    """
    Verifica si en un sector del artista hay entradas disponibles.
    artista: índice 1-based del artista en la lista eventos
    opcion_sector: 1=Campo, 2=Platea Alta, 3=Platea Baja
    """
    if opcion_sector in [1, 2, 3]:
        # En tu estructura, sectores están en índices 2, 3 y 4 respectivamente
        return eventos[artista-1][opcion_sector + 1][1] > 0
    return False

def seleccionar_artistas(eventos):
    """Muestra artistas y devuelve el índice elegido (1-based)."""
    print("Seleccione su artista:")
    i = 0
    while i < len(eventos):
        print("%d. %s" % (i + 1, eventos[i][0]))
        i += 1
    opcion_elegida = int(input("Ingrese el número del evento: "))
    while opcion_elegida < 1 or opcion_elegida > len(eventos):
        print("Opción no válida. Por favor seleccione una opción del menú.")
        opcion_elegida = int(input("Ingrese el número del evento: "))
    return opcion_elegida

def ver_fechas_del_artista(artista):
    """Devuelve la lista de fechas disponibles para un artista."""
    fechas = []
    i = 0
    while i < len(eventos[artista - 1][1]):
        fechas.append(eventos[artista - 1][1][i])
        i += 1
    return fechas

def seleccionar_sector(artista):
    """
    Muestra sectores para seleccionar y devuelve el índice correcto
    o False si el sector no tiene disponibilidad.
    """
    print("Seleccione el sector:")
    print("1. Campo")
    print("2. Platea Alta")
    print("3. Platea Baja")
    opcion_sector = int(input("Ingrese el sector: "))
    while opcion_sector < 1 or opcion_sector > 3:
        print("Opción no válida. Por favor seleccione una opción del menú.")
        opcion_sector = int(input("Ingrese el sector: "))

    if comprobar_disponibilidad(artista, opcion_sector):
        print("El sector tiene disponibilidad.")
        print("Disponibilidad:", eventos[artista - 1][opcion_sector + 1][1], "entradas disponibles")
        if opcion_sector == 1:
            print("Precio Campo:", eventos[artista - 1][2][0])
            return 2
        elif opcion_sector == 2:
            print("Precio Platea Alta:", eventos[artista - 1][3][0])
            return 3
        elif opcion_sector == 3:
            print("Precio Platea Baja:", eventos[artista - 1][4][0])
            return 4
    else:
        print("El sector no tiene disponibilidad.")
        return False

def modificar_precio():
    """Modifica el precio de un sector de un artista y guarda los cambios."""
    print("---------------------------")
    artista = seleccionar_artistas(eventos)
    sector = seleccionar_sector(artista)
    if not sector:
        print("No hay disponibilidad en el sector seleccionado para modificar el precio.")
        return
    nuevo_precio = int(input("Ingrese el nuevo precio: "))
    while nuevo_precio <= 0:
        print("El precio debe ser un número positivo.")
        nuevo_precio = int(input("Ingrese el nuevo precio: "))
    if sector == 2:
        eventos[artista - 1][2][0] = nuevo_precio
        print("Precio Campo actualizado a:", nuevo_precio)
    elif sector == 3:
        eventos[artista - 1][3][0] = nuevo_precio
        print("Precio Platea Alta actualizado a:", nuevo_precio)
    elif sector == 4:
        eventos[artista - 1][4][0] = nuevo_precio
        print("Precio Platea Baja actualizado a:", nuevo_precio)
    guardar_eventos(eventos)

def agregar_artistas(nombre, fechas, disp_campo, precio_campo, disp_platea_alta, precio_platea_alta, disp_platea_baja, precio_platea_baja):
    """Agrega un artista nuevo y guarda en el JSON."""
    nuevo_artista = [
        nombre,
        fechas,
        [precio_campo, disp_campo],
        [precio_platea_alta, disp_platea_alta],
        [precio_platea_baja, disp_platea_baja]
    ]
    eventos.append(nuevo_artista)
    guardar_eventos(eventos)
    print("Artista agregado con éxito.")

def modificar_disponibilidad():
    """Modifica la disponibilidad de un sector y guarda cambios."""
    print("---------------------------")
    artista = seleccionar_artistas(eventos)
    print("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): ")
    sector = int(input())
    while sector not in [1, 2, 3]:
        print("Opción no válida. Por favor seleccione una opción del menú.")
        sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
    nueva_disponibilidad = int(input("Ingrese la nueva disponibilidad: "))
    while nueva_disponibilidad < 0:
        print("La disponibilidad no puede ser negativa.")
        nueva_disponibilidad = int(input("Ingrese la nueva disponibilidad: "))
    if sector == 1:
        eventos[artista - 1][2][1] = nueva_disponibilidad
        print("Disponibilidad Campo actualizada a:", nueva_disponibilidad)
    elif sector == 2:
        eventos[artista - 1][3][1] = nueva_disponibilidad
        print("Disponibilidad Platea Alta actualizada a:", nueva_disponibilidad)
    elif sector == 3:
        eventos[artista - 1][4][1] = nueva_disponibilidad
        print("Disponibilidad Platea Baja actualizada a:", nueva_disponibilidad)
    guardar_eventos(eventos)
    
def bajar_fecha():
    """Bajar una fecha de un artista y guarda los cambios."""
    print("---------------------------")
    artista = seleccionar_artistas(eventos)
    print(f"Fechas disponibles: {eventos[artista - 1][1]}")
    fecha = input("Ingrese la fecha a bajar: ")
    while fecha not in eventos[artista - 1][1]:
        print("Fecha no encontrada.")
    eventos[artista - 1][1].remove(fecha)
    guardar_eventos(eventos)
    print("Fecha eliminada con éxito.")

def bajar_sector():
    """Da de Baja un sector de un artista y guarda los cambios."""
    artista = seleccionar_artistas(eventos)
    sector = seleccionar_sector(artista)
    print(f"Sector seleccionado: {sector}")
    if not sector:
        print("No hay disponibilidad en el sector seleccionado para bajar.")
        return
    eventos[artista - 1][sector][1] = 0
    guardar_eventos(eventos)
    print("Sector eliminado con éxito.")

def agregar_fecha():
    """Agregar una fecha a un artista y guarda los cambios."""
    print("---------------------------")
    artista = seleccionar_artistas(eventos)
    fecha = input("Ingrese la fecha a agregar: ")
    eventos[artista - 1][1].append(fecha)
    guardar_eventos(eventos)
    

def ver_entradas_disponibles(opcion_fecha):
    """Muestra las entradas disponibles para una fecha específica."""
    print("Entradas disponibles para la fecha:", opcion_fecha)
    print("---------------------------")
    for evento in eventos:
    	if opcion_fecha in evento[1]:  # Verifica si la fecha está en las fechas del artista
            print("Artista:", evento[0])
            print("Campo:", evento[2][1], "entradas disponibles")
            print("Platea Alta:", evento[3][1], "entradas disponibles")
            print("Platea Baja:", evento[4][1], "entradas disponibles")
            print("---------------------------")
	

def validar_opcion_menu(opciones_validas):
	"""Valida que la opción ingresada sea válida."""
	opcion = input("Seleccione una opción: ")
	while opcion not in opciones_validas:
		print("Opción no válida. Por favor, seleccione una opción del menú.")
		opcion = input("Seleccione una opción: ")
	return opcion

def procesar_opcion_usuario(opcion):
	"""Procesa las opciones del usuario en el menú principal."""
	if opcion == "1":
		procesar_opcion_ver_artistas()
	elif opcion == "2":
		filtrar_artistas_por_precio()
	elif opcion == "3":
		crear_asientos()
	elif opcion == "9":
		ingresar_administrador()

def procesar_opcion_ver_artistas():
	"""Procesa la opción de ver artistas y sus subopciones."""
	artista = int(seleccionar_artistas(eventos))
	print("Artista elegido: ", eventos[artista - 1][0])
	print("---------------------------")
	print("¿Qué desea hacer?")
	print("---------------------------")
	print("[1] Proceder con la compra")
	print("[2] Ver fechas disponibles")
	print("[3] Ver entradas disponibles")
	opcion_elegida = validar_opcion_menu(["1", "2", "3"])
	
	if opcion_elegida == "1":
		proceder_con_compra(artista)
	elif opcion_elegida == "2":
		mostrar_fechas_disponibles(artista)
	elif opcion_elegida == "3":
		ver_entradas_disponibles_por_fecha(artista)

def proceder_con_compra(artista):
	"""Permite al usuario proceder con la compra de entradas."""
	sector = seleccionar_sector(artista)
	while not sector:
		print("Sector sin entradas disponibles.")
		sector = seleccionar_sector(artista)
	cantidad_de_entradas = int(input("Ingrese la cantidad de entradas: "))
	while cantidad_de_entradas > eventos[artista - 1][sector][1] or cantidad_de_entradas <= 0:
		print("Cantidad no válida. Verifique la disponibilidad o ingrese un número positivo.")
		cantidad_de_entradas = int(input("Ingrese la cantidad de entradas: "))
	total = cantidad_de_entradas * eventos[artista - 1][sector][0]
	print(f"Total a pagar: {total}")
	print("Entradas compradas con éxito. ¡Gracias por su compra!")

def mostrar_fechas_disponibles(artista):
	"""Muestra las fechas disponibles para un artista."""
	fechas = ver_fechas_del_artista(artista)
	print("Fechas disponibles:")
	for fecha in fechas:
		print("-", fecha)

def ver_entradas_disponibles_por_fecha(artista):
	"""Muestra las entradas disponibles para una fecha específica."""
	print("Ver entradas disponibles")
	print("---------------------------")
	fechas_disponibles = ver_fechas_del_artista(artista)
	for fecha in fechas_disponibles:
		print(fecha)
	opcion_fecha = input("Ingrese la fecha: ")
	while opcion_fecha not in fechas_disponibles:
		print("Fecha no válida.")
		opcion_fecha = input("Ingrese la fecha: ")
	ver_entradas_disponibles(opcion_fecha)
 



 

def filtrar_artistas_por_precio():
	"""Permite filtrar artistas por precio y sector."""
	print("Filtrar artistas por precio")
	print("---------------------------")
	opcion_de_filtro = input("¿Desea filtrar por mayor o menor precio? (mayor/menor): ")
	while opcion_de_filtro not in ["mayor", "menor"]:
		print("Opción no válida.")
		opcion_de_filtro = input("¿Desea filtrar por mayor o menor precio? (mayor/menor): ")
	precio = int(input("Ingrese el precio: "))
	while precio <= 0:
		print("El precio debe ser un número positivo.")
		precio = int(input("Ingrese el precio: "))
	tipo_de_sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
	while tipo_de_sector not in [1, 2, 3]:
		print("Opción no válida.")
		tipo_de_sector = int(input("Ingrese el tipo de sector: campo(1), platea alta(2), platea baja(3): "))
	
	if opcion_de_filtro == "mayor":
		artistas_filtrados = [artista for artista in eventos if artista[tipo_de_sector + 1][0] > precio]
	else:
		artistas_filtrados = [artista for artista in eventos if artista[tipo_de_sector + 1][0] < precio]
	
	if not artistas_filtrados:
		print(f"No hay artistas con precios {opcion_de_filtro} a {precio}.")
	else:
		for artista in artistas_filtrados:
			print(f"Artista: {artista[0]}, Precio: {artista[tipo_de_sector + 1][0]}")

def ingresar_administrador():
	"""Permite el ingreso al menú de administrador."""
	print("Ingreso de administrador")
	print("---------------------------")
	usuario = input("Ingrese su usuario: ")
	contrasena = input("Ingrese su contraseña: ")
	if usuario == "admin" and contrasena == "admin":
		mostrar_menu_administrador()
	else:
		print("Usuario o contraseña incorrectos.")

def mostrar_menu_administrador():
	"""Muestra el menú de administrador y procesa sus opciones."""
	opcion_administrador = ""
	while opcion_administrador != "0":
		print()
		print("Bienvenido Administrador")
		print("---------------------------")
		print("[1] Modificar precios")
		print("[2] Modificar disponibilidad")
		print("[3] Agregar artistas")
		print("[4] Ver Usuarios")
		print("[5] Baja fecha")
		print("[6] Baja sector")
		print("[7] Agregar fecha")
		print("---------------------------")
		print("[0] Salir")
		print("---------------------------")
		opcion_administrador = validar_opcion_menu(["1", "2", "3", "4", "5", "6", "7", "0"])
		
		if opcion_administrador == "1":
			modificar_precio()
		elif opcion_administrador == "2":
			modificar_disponibilidad()
		elif opcion_administrador == "3":
			agregar_nuevo_artista()
		elif opcion_administrador == "4":
			mostrar_usuarios()
		elif opcion_administrador == "5":
			bajar_fecha()
		elif opcion_administrador == "6":
			bajar_sector()
		elif opcion_administrador == "7":
			agregar_fecha()

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def es_fecha_valida(fecha):
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        año = int(partes[2])

    except ValueError:
        return False
    
    if año < 1 or mes < 1 or mes > 12 or dia < 1:
        return False
    
    dias_por_mes = [31, 29 if es_bisiesto(año) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia > dias_por_mes[mes - 1]:
        return False
    
    return True


def agregar_nuevo_artista():
	"""Permite agregar un nuevo artista al sistema."""
	nombre = input("Ingrese el nombre del artista: ")
	while not nombre:
		print("El nombre no puede estar vacío.")
		nombre = input("Ingrese el nombre del artista: ")
	
	fechas = input("Ingrese las fechas del artista (separadas por comas) dd/mm/yy: ").split(",")
    
	for i in range(len(fechas)):
		fechas[i] = fechas[i].strip()
		while not es_fecha_valida(fechas[i]):
			print('Fecha no valida. Debe estar en formato dd/mm/yy y ser una fecha real.')
			fechas[i] = input("Ingrese la fecha nuevamente: ").strip()

	print("Fechas válidas ingresadas:")

	for fecha in fechas:
		print("- ", fecha)

	precio_campo = int(input("Ingrese el precio del campo: "))
	while precio_campo <= 0:
		print("El precio debe ser un número positivo.")
		precio_campo = int(input("Ingrese el precio del campo: "))
	disponibilidad_campo = int(input("Ingrese la disponibilidad del campo: "))
	while disponibilidad_campo < 0:
		print("La disponibilidad no puede ser negativa.")
		disponibilidad_campo = int(input("Ingrese la disponibilidad del campo: "))
	precio_platea_alta = int(input("Ingrese el precio de la platea alta: "))
	while precio_platea_alta <= 0:
		print("El precio debe ser un número positivo.")
		precio_platea_alta = int(input("Ingrese el precio de la platea alta: "))
	disponibilidad_platea_alta = int(input("Ingrese la disponibilidad de la platea alta: "))
	while disponibilidad_platea_alta < 0:
		print("La disponibilidad no puede ser negativa.")
		disponibilidad_platea_alta = int(input("Ingrese la disponibilidad de la platea alta: "))
	precio_platea_baja = int(input("Ingrese el precio de la platea baja: "))
	while precio_platea_baja <= 0:
		print("El precio debe ser un número positivo.")
		precio_platea_baja = int(input("Ingrese el precio de la platea baja: "))
	disponibilidad_platea_baja = int(input("Ingrese la disponibilidad de la platea baja: "))
	while disponibilidad_platea_baja < 0:
		print("La disponibilidad no puede ser negativa.")
		disponibilidad_platea_baja = int(input("Ingrese la disponibilidad de la platea baja: "))
	
	agregar_artistas(nombre, fechas, disponibilidad_campo, precio_campo, disponibilidad_platea_alta, precio_platea_alta, disponibilidad_platea_baja, precio_platea_baja)
	print("Artista agregado con éxito.")

def mostrar_usuarios():
    """Muestra los usuarios en forma de tabla desde usuarios.txt."""
    try:
        archivo = open('usuarios.txt', 'rt', encoding='utf-8')

        print('Usuarios Registrados: ')
        print(f"{'DNI':<15}{'Nombre y Apellido':<30}{'Eventos':<20}")
        print(f"{'-'*15}{'-'*30}{'-'*20}")
        linea = archivo.readline()
        while linea:
            linea = linea.strip()  # Quitar salto de línea final
            if linea:  # Solo procesar si no está vacía
                dni, nombre_apellido, eventos = linea.split(';')
                eventos = eventos[:-2]
                print(f"{dni:<15}{nombre_apellido:<30}{eventos:<20}")
            else:
                print("Línea mal formada:", linea)
            linea = archivo.readline()

        archivo.close()

    except FileNotFoundError:
        print("El archivo usuarios.txt no existe.")
        
def opcion_de_ingreso():
    opcion_inicio = validar_opcion_menu(["1", "2"])
	
    if opcion_inicio == "1":
        creacion_usuario()
    else:
        validacion = False
        while not validacion:
            validacion = ingreso_usuario()
            if not validacion:	
                print("DNI no encontrado. Por favor, ingrese un DNI válido.")


#PROGRAMA PRINCIPAL
def main():
	print("---------------------------")
	print("BIENVENIDO AL SISTEMA     ")
	print("---------------------------")
	print("[1] Crear usuario")
	print("[2] Ingresar con DNI")
	print("---------------------------")
	
	opcion_de_ingreso()
		
            
	print()
	print("---------------------------")
	print("MENÚ DEL SISTEMA           ")
	print("---------------------------")
	print("[1] Ver artistas")
	print("[2] Filtrar artistas por precio")
	print("[3] ver disponibilidad de asientos")
	print("[9] Ingresar Administrador")
	print("---------------------------")
	print("[0] Salir del programa")
	print()


	opcion = ""
	while opcion != "0":
		opcion = validar_opcion_menu(["0", "1", "2", "3", "9"])
		procesar_opcion_usuario(opcion)
	print("Gracias por usar el sistema de venta de entradas. ¡Hasta luego!")

main()