# Actividad Asincrona Semana 10.

# Mensaje de bienvenida.
print('\033[1m', "\nBienvenid@ a nuestro programa.", '\033[0m')

# Datos que se usaran en el programa:

# Variable del menú que muestre los productos que ofrece la tienda.

menu = (f'''\tArticulo                    Precio
                     Ropa
        1. Pantalones ............. $20
        2. Camisas ................ $10
        3. Sudaderas .............. $15
        4. Zapatos de marca ....... $375

            Articulos tecnologicos

        5. Iphone 14 Pro MAX ...... $1500
        6. PlayStation 5 .......... $700
        7. MacBook Pro ............ $2000
        8. AirPods ................ $150
        
        Si usted gasta $500 o más, tendra un descuento del 5%
        Si usted gasta $1000 o más, tendrá un descuento del 10%.''')

# Variables que nos serviran para el bucle While.
x = "si"
a = 0
b = 0

# Desarollo del codigo

# Imprimir el menú
print("\nProductos disponibles en la tienda:\n")
print(menu)

# Bucle While.
while x == "si" or x == "1" or x == "s":
    b = a

    # Variable que permita digitar el precio del producto desde teclado.
    a = int(input("\nIngrese el precio del articulo que desea comprar -> "))

    while a != 20 and a != 10 and a != 15 and a != 375 and a != 1500 and a != 700 and a != 2000 and a != 150:
        if a != 20 and a != 10 and a != 15 and a != 375 and a != 1500 and a != 700 and a != 2000 and a != 150:
            a = int(input('\033[1m'+"\nIngrese un precio que esté en el menú de arriba. -> "+'\033[0m'))

    # Condición en caso de que el usuario ingrese un número negativo.
    if a <= 0:
        a = 0
        print("\n"'\033[1m'+ "Por favor introduzca un precio real."+ '\033[0m')
       
    c = b + a
    a = c

    # Menú para que el usuario elija si comprará otro producto o no.

    menu2 = 1
    while menu2 != "1" and menu2 != "2" and menu2 != "si" and menu2 != "no" and menu2 != "s" and menu2 != "n":
        menu2 = input('''\n\t¿Desea comprar otro articulo?
                  
                    1. Si
                    2. No
                  
                     Eliga una opcion 1 o 2 -> ''').lower()
        if menu2 != "1" and menu2 != "2" and menu2 != "si" and menu2 != "no" and menu2 != "s" and menu2 != "n":
            print("\n"'\033[1m'+"Asegurate de escribir una opción de menú que sea correcta."+'\033[0m')

        x = menu2

    # Fin del bucle While.

# Condición para agregar el respectivo descuento al usuario.
if a >= 500 and c <= 999:
    a = c - (c)*0.05
    print(f"\nPrecio total = ${c}. Se aplicó el 5% de descuento a su compra, el precio a pagar es de: ${a}")
    print(f"Usted ahorró la cantidad de ${(c)*0.05}\n")
    
elif a >= 1000:
    a = c - (c)*0.1
    print(f"\nPrecio total = ${c}. Se aplicó un 10% de descuento a su compra, el precio a pagar es de: ${a}")
    print(f"Usted ahorró la cantidad de ${(c)*0.1}\n")

else:
    print(f"\nEl precio a pagar por su compra es de: ${a}\n")

# Mensaje de cierre.
print('\033[1m', "Fin del programa.\n", '\033[0m', sep="")