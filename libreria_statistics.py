# La libreria statistics nos permiterealizar cálculos estadísticos sobre conjuntos de datos.
# Para los ejemplos imprtaremos la libreria statistics y nos ayudaremos de la libreria random para generar conjuntos de datos aleatorios.

import statistics, random

# Creamos una variable 'valores' que será nuestro conjunto de datos para trabajar con los ejemplos.
valores = random.sample(range(10), 8)
print()
print(f"Numeros aleatorios generados: {valores}")
print()
# Funcion mean, calcula la media de un listado de números dados en parametro.
print("mean - Calcula la media: ", statistics.mean(valores))
print()
# Funcion median, calcula la mediana de un listado de números dados en parametro.
print("median - Calcula la mediana: ", statistics.median(valores))
print()
# Funcion median_low, calcula la mediana inferior de un listado de números dados en parametro.
print("median_low - Calcula la mediana inferior: ", statistics.median_low(valores))
print()
# Funcion median_high, calcula la mediana superior de un listado de números dados en parametro.
print("median_high - Calcula la mediana superior: ", statistics.median_high(valores))
print()
# Funcion mode, calcula la moda (devuelve el valor más frecuente en la lista) de un listado de números dados en parametro.
print("mode - Calcula la moda: ", statistics.mode(valores))
print()
# Funcion variance, calcula la varianza de un listado de números dados en parametro.
print("variance - Calcula la varianza: ", statistics.variance(valores))
print()