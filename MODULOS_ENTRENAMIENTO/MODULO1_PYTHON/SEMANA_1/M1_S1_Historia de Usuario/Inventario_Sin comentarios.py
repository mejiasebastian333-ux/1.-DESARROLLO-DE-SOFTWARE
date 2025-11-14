
nombreProducto = str(input("\nIngrese el nombre del producto: "))

PrecioUnitarioProducto = float(input("\nIngrese el precio unitario del producto: $"))

while PrecioUnitarioProducto <= 0:   
    print("\nEl precio ingresado debe ser mayor a 0. Por favor intente nuevamente\n") 
    PrecioUnitarioProducto = float(input("\nIngrese el precio unitario del producto: $")) 
CantidadProducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: "))

while CantidadProducto <= 0: 
    print("\nLa cantidad ingresada debe ser mayor a 0. Por favor intente nuevamente\n") 
    CantidadProducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: ")) 

confirmar = str(input(f"\nConfirma que deseas agregar {CantidadProducto} unidades del producto '{nombreProducto}' al inventario? (si/no): ")).lower()
while confirmar not in ["si", "no"]: 
    print("\nRespuesta no válida. Por favor responde con 'si' o 'no'.\n") 
    confirmar = str(input(f"\nConfirma que deseas agregar {CantidadProducto} unidades del producto '{nombreProducto}' al inventario? (si/no): ")).lower() 

if confirmar == "si": 
        costoTotal = (PrecioUnitarioProducto * CantidadProducto)
        print(f"\nProducto ingresado exictosamente.\n\n Nombre del producto: {nombreProducto}\n Precio unitario: ${PrecioUnitarioProducto}\n Cantidad ingresada: {CantidadProducto}\n Costo total: ${costoTotal}\n")
else: 
        print("\nOperación cancelada. No se realizaron cambios en el inventario.\n")






