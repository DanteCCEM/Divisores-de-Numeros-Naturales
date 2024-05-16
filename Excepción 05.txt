try:
    a = float(input("Dividendo: "))
    b = float(input("Divisor: "))
    if a <= 0 or b <= 0:
        raise ZeroDivisionError
    print(a/b)
except ValueError:
    print("Debe ser un int o float")
except ZeroDivisionError:
    print("Por favor, ingrese un valor mayor que CERO")
