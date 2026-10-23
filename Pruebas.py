# Importe de librerías
import numpy as np

# Creación de vectores y máscaras
arr = np.array([1, 2, 3])
mascara_mayores_a_uno = arr > 1

palabras = np.array(["hola", "mundo", "hola", "perooo"])
mascara_es_hola = palabras == "hola"

# Impresiones en consola
print("Array original:", arr)
print("Filtrado (> 1):", arr[mascara_mayores_a_uno])

print("Palabras:", palabras)
print("Máscara ('hola'):", mascara_es_hola)
print("Filtrado ('hola'):", palabras[mascara_es_hola])