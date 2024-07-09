import funciones

def mostrar_menu():
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            funciones.mostrar_asientos()
        elif opcion == '2':
            funciones.comprar_asiento()
        elif opcion == '3':
            funciones.anular_pasaje()
        elif opcion == '4':
            funciones.modificar_datos()
        elif opcion == '5':
            funciones.mostrar_mensaje_salida()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
