def f():
    try:
        x = int("cuatro")
    except ValueError as e:
        print("La función tiene :-) ", e)
        raise

try:
    f()
except ValueError as e:
    print("Tiene :-) ", e)

print("Sigamos adelante")