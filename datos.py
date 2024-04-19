#importación de la librería pandas
import pandas as pd

#Definición de la función llamada "analisis_estadistico" y toma una lista de Edades
def analisis_estadistico(valores):
    
    #Se verifica si la lista está vacía o si no es una lista
    if not valores or not isinstance(valores, list):
        
        #Si no se cumple con esa condición, devuelve un error de ValueError
        raise ValueError("La lista no puede estar vacía")

    #Se crea un Dataframe
    df = pd.DataFrame(valores, columns=["Edad"])

    #Se calcula la frecuencia absoluta de cada valor de la columna "Edad"
    df['fi'] = df['Edad'].map(df['Edad'].value_counts())
    #Se calcula la frecuencia absoluta
    df['Fi'] = df['fi'].cumsum()
    #Se calcula la frecuencia relativa
    df['ri'] = df['fi'] / df['fi'].sum()
    #Se calcula la frecuencia relativa acumulada
    df["Ri"] = df["ri"].cumsum()
    #Se calcula el porcentaje de la frecuencia relativa
    df["pi%"] = df["ri"] * 100
    #Se calcula el porcentaje acumulado
    df["Pi%"] = df["pi%"].cumsum()

    #Devuelve el DataFrame
    return df
