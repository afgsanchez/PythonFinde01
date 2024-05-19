'''Vamos a ver los metodos que tienen los diccionarios'''
# Creamos el diccionario
numerosingles = {"uno" : "one", "dos": "two", "tres" : "three", "cuatro": "four", "cinco": "five", "seis" : "six", "siete" : "seven", "ocho" : "eight", "nueve": "nine"}

# Mostramos el diccionario original
print("Diccionario original: ", numerosingles)
print()

# Metodo copy: realiza una copia del diccionario y lo devuelve como resultado de la ejecucion
diccionariocopia = numerosingles.copy()
print("copy: ", diccionariocopia)
print()

# Metodo clear: elimina el contenido de un diccionario
diccionariocopia.clear()
print(f"clear: {diccionariocopia} -> contenido de diccionario copia borrado.")
print()

# Metodo pop: obtiene el valor de una clave del diccionario, la devuelve como resultado de la
# ejecución y lo elimina del diccionario
print("pop: Elimina el valor y la clave 'dos': ", numerosingles.pop("dos"))
# Ahora vemos como ha quedado la lista
print(numerosingles)
print()

# Metodo popitem: hace lo mismo que pop pero con el ultimo elemento del diccionario.
print("popitem: Elimina el ultimo elemento del diccionario: ", numerosingles.popitem())
# Ahora vemos como ha quedado la lista
print(numerosingles)
print()

# Metodo del: elimina un elemento especificado
print(f"del: Eliminamos la clave:valor 'seis'") 
del numerosingles["seis"]
# Ahora vemos como ha quedado la lista
print(numerosingles)
print()

# Metodo get: devuelve el valor de la clave especificada, si no lo encuentra, nos devuelve el segundo parametro.
print("get: devuelve el valor de la clave 'siete': ", numerosingles.get("siete", "Valor no encontrado!"))
print()

# Metodo update: añade elementos al diccionario, hay que especificar los nuevo elementos en forma de diccionario.
# si repetimos alguna clave, se reemplazará el valor por el nuevo.
numerosingles.update({"ocho" : "REEMPLAZADO", "diez" : "ten", "once" : "eleven"})
print("update: anadimos los valores 'diez y once' y reemplazamos el valor del 'ocho': -> ", numerosingles)
print()

# Metodo setdefault: inserta un nuevo elemento, si ya existe devuelve el valor del existente - v1
print("setdefault: Insertamos el doce:twelve: ", numerosingles.setdefault("doce" , "twelve"))
print(numerosingles)
print()
# Metodo setdefault: inserta un nuevo elemento, si ya existe devuelve el valor del existente - v2
print("setdefault: Ejemplo existente, Intentamos insertar la clave 'cuatro' con el valor nuevo 'FOUR': ", numerosingles.setdefault("cuatro" , "FOUR"),  "<- Nos muestra el valor original y no lo reemplaza")
print()
print("Vemos como mantiene en el diccionario el valor 'four' original", numerosingles)
print()

# Metodo items: nos devuelve un objeto iterable (una lista) compuesto por los elementos del diccionario
print("items: devuelve un objeto iterable: ", numerosingles.items())
print()

# Metodo keys: nos devuelve un objeto iterable (una lista) compuesto por las claves del diccionario
print("keys: devuelve las claves en forma de objeto iterable: ", numerosingles.keys())
print()

# Metodo values: nos devuelve un objeto iterable (una lista) compuesto por los valores del diccionario
print("values: devuelve los valores en forma de objeto iterable: ", numerosingles.values())
print()