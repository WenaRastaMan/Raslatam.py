import json
import datetime

# Variables globales necesarias para que las funciones vean que si estan las variables que usaran
asientos = [[' ']*6 for _ in range(7)]
pasajeros = {}

# Función para inicializar los asientos
def inicializar_asientos():
    num_asiento = 1
    for i in range(7):
        for j in range(6):
            asientos[i][j] = str(num_asiento)
            num_asiento += 1

# Función para mostrar los asientos disponibles
def mostrar_asientos():
    for fila in asientos:
        print(' | '.join(fila))
        print()

# Función para guardar datos en un archivo JSON
def guardar_datos():
    with open('pasajeros.json', 'w') as f:
        json.dump(pasajeros, f)

# Función para cargar datos de un archivo JSON
def cargar_datos():
    global pasajeros
    try:
        with open('pasajeros.json', 'r') as f:
            pasajeros = json.load(f)
    except FileNotFoundError:
        pasajeros = {}

# Función para comprar asiento
def comprar_asiento():
    mostrar_asientos()
    asiento = input("Ingrese el número de asiento que desea comprar: ")
    if asiento_disponible(asiento):
        nombre = input("Ingrese su nombre: ")
        rut = input("Ingrese su RUT: ")
        telefono = input("Ingrese su teléfono: ")
        banco = input("Ingrese su banco: ")
        precio = 250000 if int(asiento) > 30 else 80200
        if banco.lower() == "bancoDuoc".lower():
            precio *= 0.85
        pasajeros[asiento] = {
            'nombre': nombre,
            'rut': rut,
            'telefono': telefono,
            'banco': banco,
            'precio': precio
        }
        actualizar_asientos(asiento, 'X')
        guardar_datos()
        print(f"Compra realizada exitosamente. Precio: {precio}")
    else:
        print("El asiento no está disponible.")

# Función para verificar si un asiento está disponible
def asiento_disponible(asiento):
    for fila in asientos:
        if asiento in fila:
            return True
    return False

# Función para actualizar el estado de un asiento
def actualizar_asientos(asiento, estado):
    for i in range(7):
        for j in range(6):
            if asientos[i][j] == asiento:
                asientos[i][j] = estado
                return

# Función para anular pasaje
def anular_pasaje():
    asiento = input("Ingrese el número de asiento que desea anular: ")
    if asiento in pasajeros:
        del pasajeros[asiento]
        actualizar_asientos(asiento, asiento)
        guardar_datos()
        print("Pasaje anulado exitosamente.")
    else:
        print("No se encontró un pasaje para ese asiento.")

# Función para modificar datos del pasajero
def modificar_datos():
    asiento = input("Ingrese el número de asiento: ")
    rut = input("Ingrese su RUT: ")
    if asiento in pasajeros and pasajeros[asiento]['rut'] == rut:
        print("1. Modificar nombre")
        print("2. Modificar teléfono")
        opcion = input("Seleccione la opción: ")
        if opcion == '1':
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            pasajeros[asiento]['nombre'] = nuevo_nombre
        elif opcion == '2':
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            pasajeros[asiento]['telefono'] = nuevo_telefono
        else:
            print("Opción no válida.")
        guardar_datos()
    else:
        print("No se encontró un pasaje para esos datos.")

# Función para mostrar mensaje de salida
def mostrar_mensaje_salida():
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Sistema cerrado. Nombre: [Tu Nombre], Apellido: [Tu Apellido], Fecha: {fecha_actual}")

# Inicializar el sistema
inicializar_asientos()
cargar_datos()
