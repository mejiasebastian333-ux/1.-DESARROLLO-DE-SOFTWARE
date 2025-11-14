
## Se declara la variable nombreProducto para almacenar el nombre del producto ingresado por el usuario, tipo de dato str.
## Se solicita al usuario ingresar el nombre del producto que desea registar en el inventario.
nombreProducto = str(input("\nIngrese el nombre del producto: "))

## Se declara la variable PrecioUnitarioProducto para almacenar el precio unitario del producto ingresado por el usuario, tipo de dato float.
## Se solicita al usuario ingresar el precio unitario del producto, validando que sea un valor mayor a 0.
PrecioUnitarioProducto = float(input("\nIngrese el precio unitario del producto: $"))

while PrecioUnitarioProducto <= 0: ## Se inicia un ciclo while, si el precio ingresado es menor o igual a cero se arroja el mensaje de la siguiente liena.   
    print("\nEl precio ingresado debe ser mayor a 0. Por favor intente nuevamente\n") ## Se le indica al usuario que el precio debe ser mayor a 0.
    PrecioUnitarioProducto = float(input("\nIngrese el precio unitario del producto: $")) ## Se le vuelve a solicitar al usuario ingresar el precio unitario del producto hasta que ingrese un valor correcto.
## Se declara la variable CantidadProducto para almacenar la cantidad del producto ingresado por el usuario, tipo de dato int.
## Si el usuario ingresa un valor correcto, se le solicita la cantidad del producto que desea ingresar al inventario.
CantidadProducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: "))

while CantidadProducto <= 0: ## Se inicia un ciclo while, si la cantidad ingresada es menor o igual a cero se arroja el mensaje de la siguiente liena.
    print("\nLa cantidad ingresada debe ser mayor a 0. Por favor intente nuevamente\n") ## Se le indica al usuario que la cantidad debe ser mayor a 0.
    CantidadProducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: ")) ## Se le vuelve a solicitar al usuario ingresar la cantidad del producto hasta que ingrese un valor correcto.

## Se declara la variable confirmar para almacenar la respuesta del usuario sobre si desea agregar el producto al inventario, tipo de dato str.
## Si el usuario ingresa un valor correcto, se le solicita confirmar si desea agregar el producto al inventario mediante la opcion .lower() para evitar errores por mayusculas o minusculas.
confirmar = str(input(f"\nConfirma que deseas agregar {CantidadProducto} unidades del producto '{nombreProducto}' al inventario? (si/no): ")).lower()
while confirmar not in ["si", "no"]: ## Se inicia un ciclo while, si la respuesta ingresada no es "si" o "no", se arroja el mensaje de la siguiente liena.
    print("\nRespuesta no válida. Por favor responde con 'si' o 'no'.\n") ## Se le indica al usuario que la respuesta no es válida y debe responder con "si" o "no".
    confirmar = str(input(f"\nConfirma que deseas agregar {CantidadProducto} unidades del producto '{nombreProducto}' al inventario? (si/no): ")).lower() ## Se le vuelve a solicitar al usuario confirmar si desea agregar el producto al inventario hasta que ingrese un valor correcto.

if confirmar == "si": ## Si el usuario confirma que desea agregar el producto al inventario, se calcula el costo total y se muestra un resumen del producto ingresado.
        costoTotal = (PrecioUnitarioProducto * CantidadProducto)
        print(f"\nProducto ingresado exictosamente.\n\n Nombre del producto: {nombreProducto}\n Precio unitario: ${PrecioUnitarioProducto}\n Cantidad ingresada: {CantidadProducto}\n Costo total: ${costoTotal}\n")
else: ## Si el usuario no confirma que desea agregar el producto al inventario, se muestra un mensaje indicando que la operación fue cancelada.
        print("\nOperación cancelada. No se realizaron cambios en el inventario.\n")






