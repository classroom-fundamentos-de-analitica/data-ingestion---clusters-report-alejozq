"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    df = open('clusters_report.txt', "r")
    lines = df.readlines()
    df.close()
    for index, line in enumerate(lines):
        lines[index] = line.strip()

    df_result = pd.DataFrame(columns=('cluster','cantidad','porcentaje','palabras'))
    i = 0  
    first_col = "" 
    second_col = ""  
    for line in lines:
        if 'X' in line:
            first_col = line.replace(' ', "_")
        else:
            second_col = re.sub(r' \(.*', "", line)
            df_result.loc[i] = [first_col, second_col]
            i =i+1

    return df_result
print(ingest_data())