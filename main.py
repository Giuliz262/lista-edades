#importación de la librería pandas
import pandas as pd

#importación de la función "analisis_estadístico"
from datos import analisis_estadistico

#Realicé una lista con las edades
edades = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

#Llama a la función "analisis_estadistico" con la lista de las edades
resultado = analisis_estadistico(edades)

#Se imprime el resultado
print(resultado)