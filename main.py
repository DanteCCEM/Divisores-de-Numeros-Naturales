def calcular_divisores():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                print("Por favor, ingrese un número natural mayor que cero.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    print("Los divisores de", numero, "son:", divisores)

    # Preguntar al usuario si desea ingresar otro número
    while True:
        opcion = input("¿Desea calcular los divisores de otro número? (s/n): ").lower()
        if opcion == 's':
            calcular_divisores()
            break
        elif opcion == 'n':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' para sí o 'n' para no.")

calcular_divisores()
