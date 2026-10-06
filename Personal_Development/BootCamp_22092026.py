#   Importar Librería Pandas para importación de Excel en DataFrames
import pandas as pd

#   Ruta del Archivo de Excel
path = "P:/Personal/BootCamp in Data Science/Python_Development/Material de Apoyo/Fundamentos/Datasets/Data_22092026.xlsx"

#   Cargando el DataFrame
df = pd.read_excel(path)
#print(df.head(7))    #   Imprimiendo las primeras 7 filas del DataFrame

#   Explorando el DataFrame
print(df.info())    #   Información general del DataFrame

#   Estadísticas descriptivas del DataFrame
print(df.describe())    #   Estadísticas descriptivas del DataFrame

#   Verificacndo posibles valores de la variable "Industria"
print(df['Industria'].value_counts())

print("\nImprimiendo los valores únicos de la Variable 'Industria': \n")
for valores in df['Industria'].unique():
    #print(valores)
    
    #   Segmentando el DataFrame
    df_segmentado = df[df['Industria'] == valores]
    #print(df_segmentado.head(7))    #   Imprimiendo las primeras 7 filas del DataFrame segmentado

    #  Explorando el DataFrame segmentado
    print("\nInformación del DataFrame segmentado para la Industria: ", valores)
    print(df_segmentado.info())    #   Información general del DataFrame segmentado
    print(df_segmentado.describe())    #   Estadísticas descriptivas del DataFrame segmentado