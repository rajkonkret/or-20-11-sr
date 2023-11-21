try:
    # print("12" + 34)  # TypeError: can only concatenate str (not "int") to str
    # print(5 / 0)  # ZeroDivisionError: division by zero
    # print("A" + 5)
    # raise ValueError("Błąd wartości")
    raise NameError("Błąd nazwy")
    # print(6 + 8)
except TypeError:
    print("Bład typu")
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład ", e)  # Bład  Błąd nazwy
else:
    print("Napis pojawi się tylko gdy nie ma błedu")
finally:
    print("Wypisze niezależnie od tego czy bład się pojawił")

print("Program nadal działa")
