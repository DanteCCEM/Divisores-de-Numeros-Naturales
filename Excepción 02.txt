try:
    x = float(input("Número: "))
    inverse = 1.0 / x
except ValueError:
    print("Debe ser un int o float")
except ZeroDivisionError:
    print("Infinito")
finally:
    print("Puede que haya habido una excepción o no.")
