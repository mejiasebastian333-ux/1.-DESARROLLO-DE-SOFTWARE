inventario = []

# ---------------------------------------------
# Función para agregar libros al inventario
# ---------------------------------------------
def agregar_libro(inventario):
    print("\n--- Agregar libro ---\n")

    titulo_libro = input("Ingresa el titulo del libro: ")

    autor_libro = input("\nIngresa el nombre del autor: ")

    categoria_libro = input("\nIngresa la categoria del libro: ")

    # Validar precio unitario
    while True:
        try:
            precio_unitario_libro = float(input("\nIngrese el precio unitario del libro: "))
            if precio_unitario_libro > 0:
                break
            else:
                print("\nError: el precio debe ser mayor a 0.\n")
        except ValueError:
            print("\nError: ingresa un número válido.\n")

    # Validar stock
    while True:
        try:
            stock_libro = int(input("\nDigite el stock que desea ingresar al inventario: "))
            if stock_libro > 0:
                break
            else:
                print("Error: El stock debe ser mayor a 0.")
        except ValueError:
            print("Error: ingresa un número entero válido.")

    valor_total = precio_unitario_libro * stock_libro
    print(f"\nEl valor total a ingresar al inventario de '{titulo_libro}' es: ${valor_total:,.0f}\n")

    confirmar = input(f"¿Deseas agregar '{titulo_libro}' al inventario? (si/no): ").lower()
    while confirmar not in ["si", "no"]:
        confirmar = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

    if confirmar == "si":
        libro = {
            "Titulo del libro": titulo_libro,
            "Autor del libro": autor_libro,
            "Categoria del libro": categoria_libro,
            "Precio del libro": precio_unitario_libro,
            "stock del libro": stock_libro,
            "Total": valor_total
        }

        inventario.append(libro)
        print("\nlibro agregado correctamente.\n")
    else:
        print("\nOperación cancelada.\n") 

# ---------------------------------------------
# Mostrar inventario
# ---------------------------------------------
def mostrar_inventario(inventario):
    print("\n--- Inventario ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    for libro in inventario:
        print(
            f"libro: {libro['Titulo del libro']} | "
            f"Autor: {libro['Autor del libro']} | "
            f"Categoría: {libro['Categoria del libro']} | "
            f"Precio: ${libro['Precio del libro']:,.0f} | "
            f"stock: {libro['stock del libro']} | "
            f"Total: ${libro['Total']:,.0f}"
        )
    print()

# ---------------------------------------------
# Buscar libro por nombre
# ---------------------------------------------
def buscar_libro(inventario):
    print("\n--- Buscar libro ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el titulo del libro: ").lower()

    for libro in inventario:
        if libro["Titulo del libro"].lower() == nombre_buscar:
            print("\nlibro encontrado:\n")
            print(f"Libro: {libro['Titulo del libro']}")
            print(f"Autor: {libro['Autor del libro']}")
            print(f"Categoría: {libro['Categoria del libro']}")
            print(f"Precio: ${libro['Precio del libro']:,.0f}")
            print(f"stock: {libro['stock del libro']}")
            print(f"Total: ${libro['Total']:,.0f}\n")
            return

    print(f"\nNo se encontró el libro '{nombre_buscar}'.\n")

# ---------------------------------------------
# Actualizar información libro
# ---------------------------------------------
def actualizar_libro(inventario):
    print("\n--- Actualizar libro ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el titulo del libro a actualizar: ").lower()

    for libro in inventario:
        if libro["Titulo del libro"].lower() == nombre_buscar:

            print("\nlibro encontrado:")
            print(f"1. Titulo actual    : {libro['Titulo del libro']}")
            print(f"2. Autor actual     : {libro['Autor del libro']}")
            print(f"3. Categoria actual : {libro['Categoria del libro']}")
            print(f"4. Precio actual    : ${libro['Precio del libro']:,.0f}")
            print(f"5. stock actual  : {libro['stock del libro']}")
            print(f"Total actual        : ${libro['Total']:,.0f}\n")

            while True:
                print("¿Qué deseas actualizar?")
                print("1. Titulo")
                print("2. Autor")
                print("3. Categoria")
                print("4. Precio")
                print("5. stock")
                print("6. Cancelar")

                opcion = input("\nSelecciona una opción (1-6): ")

                # Actualizar titulo
                if opcion == "1":
                    nuevo_titulo = input("\nNuevo titulo: ")
                    libro["Titulo del libro"] = nuevo_titulo
                    print("\nTitulo actualizado.\n")
                    break

                # Actualizar autor
                if opcion == "2":
                    nuevo_autor = input("\nNuevo titulo: ")
                    libro["Autor del libro"] = nuevo_autor
                    print("\nAutor actualizado.\n")
                    break

                # Actualizar categoría
                if opcion == "3":
                    nueva_categoria = input("\nNueva categoría: ")
                    libro["Categoria del libro"] = nueva_categoria
                    print("\nACategoría actualizada.\n")
                    break

                # Actualizar precio
                elif opcion == "4":
                    while True:
                        try:
                            nuevo_precio = float(input("\nNuevo precio: "))
                            if nuevo_precio > 0:
                                libro["Precio del libro"] = nuevo_precio
                                libro["Total"] = nuevo_precio * libro["stock del libro"]
                                print("\nPrecio actualizado.\n")
                                break
                            else:
                                print("El precio debe ser mayor a 0.")
                        except ValueError:
                            print("Ingresa un número válido.")
                    break

                # Actualizar stock
                elif opcion == "5":
                    while True:
                        try:
                            nueva_stock = int(input("\nNuevo stock: "))
                            if nueva_stock > 0:
                                libro["stock del libro"] = nueva_stock
                                libro["Total"] = nueva_stock * libro["Precio del libro"]
                                print("\nstock actualizado.\n")
                                break
                            else:
                                print("El stock debe ser mayor a 0.")
                        except ValueError:
                            print("Ingresa un número válido.")
                    break

                elif opcion == "6":
                    print("\nOperación cancelada.\n")
                    return

                else:
                    print("\nOpción inválida. Intenta nuevamente.\n")

            return

    print(f"\nNo se encontró el libro '{nombre_buscar}'.\n")

# ---------------------------------------------
# Eliminar libro
# ---------------------------------------------
def eliminar_libro(inventario):
    print("\n--- Eliminar libro ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el titulo del libro a eliminar: ").lower()

    for libro in inventario:
        if libro["Titulo del libro"].lower() == nombre_buscar:

            print("\nlibro encontrado:\n")
            print(f"Libro: {libro['Titulo del libro']}")
            print(f"Autor: {libro['Autor del libro']}")
            print(f"Categoría: {libro['Categoria del libro']}")
            print(f"Precio: ${libro['Precio del libro']:,.0f}")
            print(f"stock: {libro['stock del libro']}")
            print(f"Total: ${libro['Total']:,.0f}\n")

            confirmar = input(f"¿Eliminar '{libro['Titulo del libro']}'? (si/no): ").lower()

            while confirmar not in ["si", "no"]:
                confirmar = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

            if confirmar == "si":
                inventario.remove(libro)
                print("\nlibro eliminado.\n")
            else:
                print("\nOperación cancelada.\n")

            return

    print(f"\nNo se encontró el libro '{nombre_buscar}'.\n")

