from inventario import (
    agregar_libro, mostrar_inventario, buscar_libro, actualizar_libro, eliminar_libro
)
from clientes import (
    crear_cliente, mostrar_clientes, buscar_cliente, actualizar_cliente, eliminar_cliente
)

from ventas import (
    buscar_cliente_por_documento, buscar_libro_por_titulo, registrar_venta, mostrar_ventas, buscar_venta
)
from archivos import (
    guardarInventario_csv, guardarClientes_csv
)

inventario = []
clientes = []
ventas = []

while True:
    print("")    
    print("===== MENÚ PRINCIPAL =====")
    print("")
    print("1. Gestión del inventario")
    print("2. Gestión de ventas")
    print("3. Gestión de clientes")
    print("4. Reportes")
    print("5. Salir")


    opcion1 = input("\nSelecciona una opción: ")


    if opcion1 == "1":
        
        while True:
            print("")    
            print("===== GESTIÓN DEL INVENTARIO =====")
            print("")
            print("1. Agregar libro")
            print("2. Mostrar inventario")
            print("3. Buscar libro")
            print("4. Actualizar libro")
            print("5. Eliminar libro")
            print("6. Salir")

            opcion2 = input ("\nSelecciona una opción: ")

            if opcion2 == "1":
                agregar_libro(inventario)

            elif opcion2 == "2":
                mostrar_inventario(inventario)

            elif opcion2 == "3":
                buscar_libro(inventario)

            elif opcion2 == "4":
                actualizar_libro(inventario)

            elif opcion2 == "5":
                eliminar_libro(inventario)

            elif opcion2 == "6":
                print("\nSaliendo del programa...\n")
                break
            else:
                print("\nOpción inválida. Intenta nuevamente.\n")

    elif opcion1 == "2":
            
            while True:
                print("")    
                print("===== GESTIÓN DE VENTAS =====")
                print("")
                print("1. Registrar venta")
                print("2. Mostrar lista de ventas")
                print("3. Buscar venta")
                print("4. Salir")

                opcion2 = input ("\nSelecciona una opción: ")

                if opcion2 == "1":
                    registrar_venta ()

                elif opcion2 == "2":
                    mostrar_ventas()

                elif opcion2 == "3":
                    buscar_venta ()

                elif opcion2 == "4":
                    print("\nSaliendo del programa...\n")
                    break
                else:
                    print("\nOpción inválida. Intenta nuevamente.\n")
        
    elif opcion1 == "3":
        
        while True:
            print("")    
            print("===== GESTIÓN DE CLIENTES =====")
            print("")
            print("1. Crear cliente")
            print("2. Mostrar clientes")
            print("3. Buscar cliente")
            print("4. Actualizar cliente")
            print("5. Eliminar cliente")
            print("6. Salir")

            opcion2 = input ("\nSelecciona una opción: ")

            if opcion2 == "1":
                crear_cliente(clientes)

            elif opcion2 == "2":
                mostrar_clientes(clientes)

            elif opcion2 == "3":
                buscar_cliente (clientes)

            elif opcion2 == "4":
                actualizar_cliente(clientes)
            
            elif opcion2 == "5":
                eliminar_cliente(clientes)

            elif opcion2 == "6":
                print("\nSaliendo del programa...\n")
                break
            else:
                print("\nOpción inválida. Intenta nuevamente.\n")

    elif opcion1 == "4":
        
        while True:
            print("")    
            print("===== REPORTES =====")
            print("")
            print("1. Mostrar el top 3 de productos más vendidoS")
            print("2. ventas totales por autor")
            print("3. ingreso neto y bruto")
            print("4. Salir")

            opcion2 = input ("\nSelecciona una opción: ")

            if opcion2 == "1":
                crear_cliente(clientes)

            elif opcion2 == "2":
                mostrar_clientes(clientes)

            elif opcion2 == "3":
                buscar_cliente (clientes)

            elif opcion2 == "4":
                print("\nSaliendo del programa...\n")
                break
            else:
                print("\nOpción inválida. Intenta nuevamente.\n")

    elif opcion1 == "5":
        print("\nSaliendo del programa...\n")
        break
        
    else:
        print("\nOpción inválida. Intenta nuevamente.\n")