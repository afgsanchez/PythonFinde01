print("Iniciando programa!")
try:
    print(3/1)
except ZeroDivisionError:
    print("Error de division por CERO")
except:
    print("Error General")
else:
    print("No hay errores")
finally:
    print("Programa acabado")