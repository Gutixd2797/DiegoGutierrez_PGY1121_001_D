import os
edificio = [[True for a in range(4)] for a in range(10)]
costo = [[3800, 3000, 2800, 3500] for a in range(10)]
letra = ["A", "B", "C", "D"]
clientes = []


os.system("cls")
def mostrar_menu():
    print("*************************              ")
    print("        CASA FELIZ                     ")
    print("*************************              ")
    print("1- Comprar departamento                ")
    print("2- Mostrar departamentos disponibles   ")
    print("3- Ver listado de compradores          ")
    print("4- Mostrar ganancias totales           ")
    print("5- Salir                               ")
    opcion = input("Ingrese una opcion del 1 al 5:")
    return opcion

def validar_opcion(opcion):
    try:
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            raise ValueError
        return True
    except ValueError:
        return False

def validar_piso(piso):
    try:
        piso = int(piso)
        if piso < 1 or piso > 10:
            raise ValueError
        return True
    except ValueError:
        return False

def validar_tipo(tipode):
    if len(tipode) == 1 and tipode.isalpha():  # (((devolverá True si la cadena sólo contiene caracteres alfabéticos (letras) y al menos un carácter)))
        tipode = tipode.upper()  # (((convierte a mayus)))
        if tipode in letra:
            return True
    return False

def validar_rut(rut):
    if len(rut) == 8 and rut.isdigit():  #(((((devuelve un valor distinto de cero si es un dígito decimal)))
        return True
    return False

def comprar_departamento():
    mostrar_departamentos()
    piso = input("Ingrese el piso del departamento que quieras comprar del 1 al 10: ")
    tipode = input("Ingrese el tipo del departamento que quieras comprar que pueden ser: A, B, C o D ")
    if validar_piso(piso) and validar_tipo(tipode):
        piso = int(piso) - 1
        tipode = letra.index(tipode.upper())
        if edificio[piso][tipode]:
            rut = input("Ingrese el rut del comprador (sin guion ni puntos): ")
            if validar_rut(rut):
                edificio[piso][tipode] = False
                clientes.append((rut, piso + 1, tipode + 1))
                print(f"La compra del departamento {letra[tipode]}{piso + 1} se ha realizado correctamente.")
            else:
                print("El rut ingresado no es válido. Intente nuevamente.")
        else:
            print(f"El departamento {letra[tipode]}{piso + 1} no está disponible. Intente con otro.")
    else:
        print("""
        El piso o la letra del departamento no son validos, 

        intenta nuevamente...
        """)
        






def mostrar_departamentos():
    print("Departamentos disponibles:")
    print("Piso\tA\tB\tC\tD") #Menu 1
    for i in range(10):  
        print(f"{i + 1}", end="\t")
        for j in range(4):
            if edificio[i][j]:
                print(letra[j], end="\t") #limp
            else:
                print("X", end="\t")
        print()









def ver_compradores():
    clientes.sort()
    print("Listado de compradores:")
    print("rut\t")("Departamento\t",piso,tipode)
    for rut, piso, tipode in clientes:
        print(f"{rut}\t{letra[tipode - 1]}{piso}")












def mostrar_ganancias():
    cantidades = [0, 0, 0, 0]
    totales = [0, 0, 0, 0]
    for _, piso, tipode in clientes:
        tipode -= 1
        cantidades[tipode] += 1
        totales[tipode] += costo[piso][tipode]
    print("Ganancias totales de los departamentos:")
    print("Tipo de Departamento\tCantidad\tTotal")
    for i in range(4):
        print(f"{letra[i]}\t\t\t{cantidades[i]}\t\t{totales[i]} UF")
    total_general = sum(totales)
    print(f"TOTAL\t\t\t{len(clientes)}\t\t{total_general} UF")



continuar = True
def salir():
    print(f"""
    Gracias por usar nuestro programa,
    mi nombre es Diego Gutierrez y la fecha de hoy es 11/07/2023
    """)
while continuar:
    opcion = mostrar_menu()
    if validar_opcion(opcion):
        opcion = int(opcion)
        if opcion == 1:
            os.system("cls") 
            comprar_departamento()
        elif opcion == 2:
            os.system("cls")
            mostrar_departamentos()
        elif opcion == 3:
            os.system("cls")
            ver_compradores()
        elif opcion == 4:
            os.system("cls")
            mostrar_ganancias()
        elif opcion == 5:
            os.system("cls")
            salir()
            continuar = False
    else:
        print("La opción ingresada no es válida. Intente nuevamente.")
