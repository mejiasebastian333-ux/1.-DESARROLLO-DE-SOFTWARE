clientes = []

# ---------------------------------------------
# Función para crear clientes 
# ---------------------------------------------
def crear_cliente(clientes):
    print("\n--- Crear cliente---\n")
    
    try: 
        nombre_cliente = input("\nIngrese el nombre del cliente: ").lower() 
        documento_cliente= int(input("\nIngrese el numero de documento del cliente: "))
        celular_cliente = int(input("\nIngrese el numero de celular del cliente: "))
        correo_cliente = input("\nIngrese el correo electronico del cliente: ").lower() 
        
    except ValueError:
        print("\nAgregue parametros correctos\n")


    clientes.append({"Nombre del cliente":nombre_cliente,
                    "Documento del cliente":documento_cliente, 
                    "Celular del cliente":celular_cliente, 
                    "Correo del cliente":correo_cliente })
    
    print("\ncliente creado con exito\n")

# ---------------------------------------------
# Mostrar lista de clientes
# ---------------------------------------------
def mostrar_clientes(clientes):
    print("\n--- Lista de clientes ---\n")

    if not clientes:
        print("La lista de clientes está vacía.\n")
        return

    for cliente in clientes:
        print(
            f"cliente: {cliente['Nombre del cliente']} | "
            f"Documento: {cliente['Documento del cliente']} | "
            f"Celular: {cliente['Celular del cliente']} | "
            f"Correo: ${cliente['Correo del cliente']}"
        )
    print()

# ---------------------------------------------
# Buscar clientes por documento
# ---------------------------------------------
def buscar_cliente (clientes):
    print("\n--- Buscar cliente ---\n")

    if not clientes:
        print("La lista de clientes está vacía.\n")
        return

    documento_buscar = int(input("\nIngresa el documento del cliente: "))

    for cliente in clientes:
        if cliente["Documento del cliente"] == documento_buscar:
            print("\ncliente encontrado:\n")
            print(f"cliente: {cliente['Nombre del cliente']}")
            print(f"Documento: {cliente['Documento del cliente']}")
            print(f"Celular: {cliente['Celular del cliente']}")
            print(f"Correo: ${cliente['Correo del cliente']}")
            return

    print(f"\nNo se encontró el cliente '{documento_buscar}'.\n")

# ---------------------------------------------
# Actualizar información clientes
# ---------------------------------------------
def actualizar_cliente(clientes):
    if not clientes:
        print("\nLa lista de clientes está vacía\n")
        return
    while True:
        try:
            documento_buscar = int(input("\nIngrese el documento del cliente: "))
        except ValueError:
            print("\nDígite un número válido\n")
        
        # Buscar cliente por documento
        for cliente in clientes:
            if cliente["Documento del cliente"] == documento_buscar: 
                print("\ncliente encontrado:\n")
                print(cliente)

                print("\n¿Qué deseas actualizar?\n")
                print("1. Nombre")
                print("2. Documento")
                print("3. Número de celular")
                print("4. Correo electronico\n")

                while True:
                    try:
                        opcion = int(input("Selecciona una opción: "))

                        if opcion == 1:
                            cliente["Nombre del cliente"] = input("\nNuevo nombre: ").lower()
                        elif opcion == 2:
                            cliente["Documento del cliente"] = int(input("\nNuevo documento: "))
                        elif opcion == 3:
                            cliente["Celular del cliente"] = int(input("\nNuevo número de celular: "))
                        elif opcion == 4:
                            cliente["Correo del cliente"] = input("\nNuevo correo electronico: ").lower()
                        else:
                            print("\nOpción no válida\n")
                    except ValueError:
                        print("\ningrese un un valor valido\n")

                    print("\nDatos actualizados con éxito.\n")
                    return
            
            print("\nNo se encontró un cliente con ese documento.\n")

# ---------------------------------------------
# Eliminar cliente
# ---------------------------------------------
def eliminar_cliente(clientes):

    while True:
        try:
            documento_buscar = int(input("Ingrese el documento del cliente: "))
        except ValueError:
            print("\nDigite un numero valido\n")
            return
        for cliente in clientes:
            if cliente["Documento del cliente"] == documento_buscar:
                clientes.remove(cliente)
                print("\ncliente eliminado con exito\n")
                return