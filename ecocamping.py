print("Gestion de eco camping 'Bosque vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENU DE CONTROL DE REGISTROS")
    print("1.- Ver sitios disponibles")
    print("2.- Registros de nuevos vehiculos en el sitio (Entrada)")
    print("3.- Registro de salida de vehiculos (Salida)")
    print("4.- Estado actual del camping")
    print("5.- Salir")
    try: 
        opcion = int(input("Seleccione una opcion (1-5)"))
    except ValueError:
        print("Opcion no valida, por favor seleccione entre 1 y 5")
        continue
    #Despliegue de opciones
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres para recibir vehiculos: {disponibles}")
    elif opcion ==2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print("Lo sentimos, no quedan espacios en el camping")
        else:
            try:
                ingreeso = int(input("¿Cuantos sitios o vehiculos van a ingresar?"))
                if ingreeso <= 0:
                    print ("Error : La cantidad de ingresos debe ser mayor a 0")
                elif ingreeso > sitios_libres:
                    print(f"Solo pueden ingresae un maximo de {sitios_libres} sitios")
                else: 
                    sitios_ocupados += ingreeso
                    print(f"Ingreso registrado, se han ocupado {ingreeso} de sitios")
            except ValueError:
                print ("Error: debe ingresar un numero valido")
    elif opcion == 3:
        
    else:
        print("Opcion fuera de rango")