import pandas as pd

def analisis_estadistico(valores):
    if not valores or not isinstance(valores, list):
        raise ValueError("La lista no puede estar vacía")

    df = pd.DataFrame(valores, columns=["Valor"])

    df['fi'] = df['Valor'].map(df['Valor'].value_counts())
    df['Fi'] = df['fi'].cumsum()
    df['ri'] = df['fi'] / df['fi'].sum()
    df["Ri"] = df["ri"].cumsum()
    df["pi%"] = df["ri"] * 100
    df["Pi%"] = df["pi%"].cumsum()

    return df
