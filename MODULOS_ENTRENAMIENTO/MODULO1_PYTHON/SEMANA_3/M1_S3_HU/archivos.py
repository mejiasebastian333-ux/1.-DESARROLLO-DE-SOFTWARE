
# ---------------------------------------------
# Guardar CSV
# ---------------------------------------------
import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de diccionarios con productos.
        ruta (str): Ruta del archivo CSV a guardar.
        incluir_header (bool): Si True, escribe encabezado.
    """

    # Validar inventario vacío
    if not inventario:
        print("\nNo se puede guardar: el inventario está vacío.\n")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            # Escribir el encabezado
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            # Escribir filas del inventario
            for producto in inventario:
                escritor.writerow([
                    producto["Nombre del producto"],
                    producto["Precio del producto"],
                    producto["Cantidad del producto"]
                ])

        print(f"\nInventario guardado en: {ruta}\n")

    except PermissionError:
        print("\nError: No tienes permisos para escribir en esa ubicación.\n")

    except OSError:
        print("\nError: No se pudo escribir el archivo. Verifica la ruta o permisos.\n")



# ---------------------------------------------
# Cargar CSV
# ---------------------------------------------
import csv

def cargar_csv(ruta, inventario):
    print("\n--- Cargar archivo CSV ---\n")

    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # Validar encabezado
            try:
                encabezado = next(lector)
            except StopIteration:
                print("\nEl archivo CSV está vacío.\n")
                return inventario

            encabezado_esperado = ["nombre", "precio", "cantidad"]
            if [col.lower().strip() for col in encabezado] != encabezado_esperado:
                print("\nError: El encabezado del CSV no es válido. Debe ser:")
                print("nombre,precio,cantidad")
                return inventario

            # Validar filas una por una
            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_cargados.append({
                        "nombre": nombre.strip(),
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1
                    continue

    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo '{ruta}'.")
        return inventario

    except UnicodeDecodeError:
        print("\nError: No se pudo leer el archivo. Codificación inválida.\n")
        return inventario

    except Exception as e:
        print(f"\nError inesperado: {e}")
        return inventario

    # Si no se cargó nada válido
    if not productos_cargados:
        print("\nNo se cargó ningún producto válido desde el CSV.\n")
        return inventario

    # Preguntar sobrescritura o fusión
    print(f"\nProductos válidos encontrados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}\n")

    opcion = input("\n¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == "S":
        inventario = productos_cargados
        print("\nInventario sobrescrito correctamente.\n")
        print(f"Productos cargados: {len(productos_cargados)}")
        print(f"Filas inválidas omitidas: {filas_invalidas}")
        return inventario

    # Si decide fusionar
    print("\nFusionando inventarios...\n")

    inventario_por_nombre = {p["nombre"].lower(): p for p in inventario}

    for producto in productos_cargados:
        nombre = producto["nombre"].lower()

        if nombre in inventario_por_nombre:
            existente = inventario_por_nombre[nombre]

            # Política de fusión:
            # 1. Sumar cantidades
            # 2. Si el precio difiere, actualizar al nuevo precio
            existente["cantidad"] += producto["cantidad"]
            if existente["precio"] != producto["precio"]:
                existente["precio"] = producto["precio"]
        else:
            inventario_por_nombre[nombre] = producto

    inventario = list(inventario_por_nombre.values())

    print("\nInventario fusionado correctamente.\n")
    print(f"Productos añadidos/actualizados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}")

    return inventario



