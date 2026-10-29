#   Impportación de librerías
import pandas as pd                 #   Trabajar con DataFrames - Pandas
import numpy as np                  #   Trabajar con Arreglos y Cálculos Numéricos (Numeric Python) - NumPy
import kagglehub                    #   API para carga de información directa desde Kaggle
#   Carga de Data
#   link = https://www.kaggle.com/datasets/joannanplkrk/dirty-data-to-clean-whats-wrong-with-this-dataset"
#   Fue necesario registrarse en Kaggle para poder permitir la descarga y tienen la opción de descarga mediante su API, así que instalé la librería kagglehub
#   pip install kagglehub
#   Ruta donde deseo que se envíe la data descargada
ruta_Download = "P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/Actividad_2"
path_kaggle = kagglehub.dataset_download("joannanplkrk/dirty-data-to-clean-whats-wrong-with-this-dataset", output_dir = ruta_Download)
print("Ruta de los archivos Dataset: ", path_kaggle)
path = "P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/Actividad_2/animal_data_dirty1.csv"
df = pd.read_csv(path, sep = ";")   #   Le indico a Pandas que el sepatador del archiv es ';' y no la ',' tradicional
#   Explorando la carga de información
print("Head: \n", df.head(7))
print("Info:"), df.info()
print("Describe: \n", df.describe())
print("Valores Nulos: \n", df.isnull().sum())
print("Valores Duplicados: \n", df.duplicated().sum())
df_original = df.copy()             #   Dado que el ejercicio de exploración lo hice por mi cuenta, copio el DataFrame original en otro para responder las preguntas
"""
  ¿Que veo?
  11 Columnas, 1011 registros, varios valores Not a Number (NaN), Fecha en Formato dd.mm.aaaa, varibale "Observation date" de tipo "str" y no de fecha
  Variable "Weight kg" con pesos de -0.252 & variable "Body Length" cpm longitudes de -19, que ambas no tienen sentido
  Variable "Animal code" no tiene información, todo es NaN.
  La varibale "Animal name" tiene 806 NaN, es demasiado para una BBDD de 1011 registros (79%)
  167 Valores Duplicados
"""
df = df.drop_duplicates()                                       #   Empezaré por eliminar duplicados
print("Valores Duplicados luego del Cambio: \n", df.duplicated().sum())
df.drop(columns = ["Animal code"], inplace = True)              #   Eliminando la variable llamada "Animal code"
print("Head: \n", df.head(7))
print(df["Data compiled by"].value_counts())                    #   Veo que la varible "Data compiled by" está bien con solo 4 posibles valores
#   Tratemos la variable "Observation date" para que se vea como fecha
df["Observation date"] = pd.to_datetime(df["Observation date"], errors = "coerce")  #   Lo logramos pero nos da 391 valores NaT (Not a Time)
#   Comentaré la secuencia de lo que haré para llenar los NaT con la mediana, calculada sin contar los NaT (Seguir los números a modo de pasos):
df["Observation date"] = df["Observation date"].fillna(         #   4. Llenando los NaT con el valor de Pandas de Fecha
    pd.to_datetime(                                             #   3. Pasando el resultado de Numpy a formato fecha con Pandas
        np.nanmedian(df["Observation date"]                     #   1. Sacando la mediana de las fechas sin contar los NaT
                     .astype("int64"))                          #   2. Convierto la fecha en formato numérico para que Numpy la pueda trabajar
    )
)
#   Ahora vamos a revisar ahora variable por variable y tomar decisiones, empezaremos con la variable "Animal type"
print("Animal type: \n", df[df["Animal type"].isna()])          #   Mirando los 19 registros NaN de "Animal type" (Aparecen también los 11 NaN de "Country")
print("Weight kg: \n", df[df["Weight kg"].isna()])              #   Mirando los 20 registros de "Weight" que son los mismos de "Body Lenght", los trataremos igual
print("Gender: \n", df[df["Gender"].isna()])                    #   Mirando los 15 registros de "Gender"

#   Verificando valores en variable "Animal Type" y "Country"
print("\nVerificando valores únicos en variable 'Animal type':\n", df["Animal type"].unique())
print("\nVerificando valores únicos en variable 'Country':\n", df["Country"].unique())
#   Veo que no son homogeneos, por los que los trataré a ambos igualmente:
df["Animal type"] = (df["Animal type"].str.strip().
                     str.title()
                     .str.replace("European Bison™", "European Bison", regex = False)       #   regex = False -> Buscará exactamente ese texto
                     .str.replace("European Bisson", "European Bison", regex = False)
                     .str.replace("European Buster", "European Bison", regex = False)
                     .str.replace("Red Squirel", "Red Squirrel", regex = False)
                     .str.replace("Red Squirrell", "Red Squirrel", regex = False)
                     .str.replace("Lynx?", "Lynx", regex = False)
                     .str.replace("Ledgehod", "Hedgehog", regex = False)
                     .str.replace("Wedgehod", "Hedgehog", regex = False)
                     )
df["Country"] = (df["Country"].str.strip()
                 .str.replace("PL", "Poland", regex = False)
                 .str.replace("Hungry", "Hungary", regex = False)
                 .str.replace("HU", "Hungary", regex = False)
                 .str.replace("DE", "Germany", regex = False)
                 .str.replace("CC", "Czech", regex = False)
                 .str.replace("CZ", "Czech", regex = False)
                 .str.replace("Czech Republic", "Czech", regex = False)
                 )

print(df[df["Gender"] == "not determined"])                     #   Existen 5 animales con género "Sin determinar", Index: 3, 43, 103, 238, 791
df.loc[df["Gender"] == "not determined", "Gender"] = np.nan     #   Cambiaré estos 5 por un NaN para que se cambién por la moda en el "for" siguiente:

#   Dado que estas variables son Categóricas, voy a imputar esos valores por la Moda (El valor que más se repite en esa variable) y lo haré en ciclo for:
for variable in df[["Animal type", "Country", "Gender"]]:
    print(f"La Moda de la variable {variable} es: ", df[variable].mode()[0])
    df[variable] = df[variable].fillna(df[variable].mode()[0])
#   Tratando los datos que son numéricos, impuntando los NaN con la mediana, pero calculándola sin tener en cuenta los NaN:
#   Revisando ahora los datos de las variables "Latitude" & "Longitude" (Son en total 92):
# print("Latitude & Longitude:\n", df.loc[df["Latitude"].isna(), ["Latitude", "Longitude"]].head(95).to_string(index = True))     #   .to_string(index = True) es para que Pandas no me trunque la visión de los 95 registros del head(95)
for variable in df[["Weight kg", "Body Length cm", "Latitude", "Longitude"]]:
    print(f"La Mediana de la {variable} es: ", np.nanmedian(df[variable]))      #   Sacando la mediana de las variables sin tener en cuenta los NaN
    df[variable] = df[variable].fillna(np.nanmedian(df[variable]))

#   Dado que la variable "Animal name" tiene un 79% de datos faltantes, pasaré los NaN a "Unknown" dado que efectivamente son desconocidos
df["Animal name"] = df["Animal name"].fillna("Unknown")

#   Revisando valores atipicos:
for variable in df[["Weight kg", "Body Length cm"]]:
    q1 = np.percentile(df[variable], 25)
    q3 = np.percentile(df[variable], 75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    atipicos = df[
        (df[variable] < limite_inferior) |
        (df[variable] > limite_superior)
    ]
    print(f"Q1 de {variable} es: ", q1)
    print(f"Q3 de {variable} es: ", q3)
    print(f"IQR de {variable} es: ", iqr)
    print(f"Límite Inferior de {variable} es: ", limite_inferior)
    print(f"Límite Superior de {variable} es: ", limite_superior)
    print(f"Valores Atípicos de {variable} son: \n", atipicos)  #   Veo que son 134 y 145, respectivamente en cada variable
    df.loc[df[variable] <= 0, variable] = np.nanmedian(df[variable])    #   Imputando los valores <= 0 por la mediana sin contar los NaN
    """Nota importante: NO cambio los valores grandes de 727, 1100 Kg, dado que veo que son de Bisontes y los bisontes pueden pesar hasta 1350 Kg aproximadamente"""
    # print("Revisando nuevamente los valores menores de 0 luego del cambio:\n", df[(df[variable] <= 0)])

#   El método reset_index() de Pandas restablece el índice del DataFrame con números consecutivos desde 0 hasta el último registro.
df = df.reset_index(drop=True)
#   Verificando nuevamente los valores Nulos luego del tratamiento de datos:
print("Valores Nulos:\n", df.isnull().sum())                    #   Con esto confirmamos que ya no tenemos nulos
#   Verifiquemos que los datos tengan el tipo de datos (dtype) que debería tener:
print("Info luego de los cambios:")
df.info()
print("Describe() luego de los cambios: \n", df.describe())

###     Realizando el Ejercicio Propuesto       ###
print("1. Diagnóstico inicial")
print("¿Cuántas filas y columnas tiene el DataFrame?\nRta: Tiene la siguiente dimensión: ", df_original.shape) # -> Tiene 11 Variables y 1011 registros
print("¿Cuáles son las columnas y que tipo de dato tiene cada una?\nRta: Son de este tipo:"), df_original.info()# -> Tiene 5 Variables tipo float, el resto son str
print("¿Cuántos valores faltantes existen por columna?\nRta: Verificamos valores Nulos (Not a Number | NaN & Not a Time | NaT):\n", df_original.isnull().sum())
print("¿Cuántos registros duplicados existen?\nRta: Se tienen los siguientes registros duplicados: ", df_original.duplicated().sum())
print("Utiliza unique() o value_counts() para identificar categorías inconsistentes o valores sospechosos\n" \
"Rta: Usando función unique() para identificar valores sospechosos:")
for variable in df_original.columns:
    if variable == "Animal code":
        break
    else:
        print(f"Para la variable {variable}, tenemos los siguientes valores únicos:\n", df[variable].unique())
print("De todo lo anterior veo lo siguiente:")
print("11 Columnas, 1011 registros, varios valores Not a Number (NaN), Fecha en Formato dd.mm.aaaa, varibale 'Observation date' de tipo 'str' y no de fecha"
"Variable 'Weight kg' con pesos de -0.252 & variable 'Body Length' cpm longitudes de -19, que ambas no tienen sentido"
"Variable 'Animal code' no tiene información, todo es NaN."
"La varibale 'Animal name' tiene 806 NaN, es demasiado para una BBDD de 1011 registros (79%)"
"167 Valores Duplicados")

print("\n2. Limpieza de Datos")
print("La Data limpia es la siguiente:"), df.info()             #   Esta es toda la data limpia que trabajé antes de revisar las intrucciones del ejercicio

print("\n3. NumPy")
print("Creación de la nueva variable con np.where(): ")
print("Elegí la variable 'Observation date' para ver si las observaciones fueorn realizadas antes del año 2000 y categorizarlas:")
# -> Si es menor del año 2000, se cataloga como antigua (Ancient), sino como reciente (Recent)
df["Antique"] = np.where(df["Observation date"] < pd.Timestamp("2000-01-01 00:00:00"), "Ancient", "Recent")
print(df["Antique"].value_counts())                             #   Verificando que haya quedado bien, al final quedaron 453 en Recent & 391 como Ancient
print("Utilizar una función estadísitca de NumPy y explicar el significado:")
print("Para la limpieza de datos se usó np.nanmedian() con el ánimo de calcular la mediana de variables como 'Weight kg', 'Body Length cm' e imputar valores" \
" Nulos o NaN (Not a Number). Es de importacia entender que se uso la función de NumPy de NaNmedian() dado que para realizar el cálculo, este no tiene en cuenta" \
"los NaN, de tal forma su resultado es mucho más confiable dado que estos NaN no se contemplan en el cálculo")
print("A continuación pongo un ejemplo usado más arriba de este código para la limpieza de datos:")
print(f"La Mediana de la variable 'Weight kg' es: ", np.nanmedian(df["Weight kg"]))
print("Lo que representa que el valor que divide los datos exactamente a la mitad del peso de los animales observados es de 0.35 Kg")
print("Y esto tiene sentido, dado que al calcular la moda de la variable 'Animal type' da como resultado: Ardilla Roja (red squirrel)")

print("\n4. Análisis con groupby()")
print("¿Cúal es el número de observaciones por tipo de animal?")
print(df.groupby("Animal type")                                 #   groupby("Animal type"): agrupa las filas según el tipo de animal.
      .size()                                                   #   size(): cuenta el número de filas (observaciones) de cada grupo.
      .sort_values(ascending = False))                          #   Para mostrar primero los animales con más observaciones (No ascendente)
print("¿Cúal es el promedio de una variable numérica según el tipo de animal")
print("Mostrando le promedio de pesos por animal:\n", df.groupby("Animal type")
      ["Weight kg"]                                             #   Selecciona únicamente la columna "Weight kg" de todas las posibles.
      .mean()                                                   #   La función mean() calcula la media o el promedio de los valores de cada grupo.
      )
print("¿Cuál es el promedio de una variable numérica según el país?")
print("Mostrando el promedio de longitud corporal por pais:\n", df.groupby("Country")
      ["Body Length cm"]
      .mean()
      )
print("Mostrando el promedio de longitud corporal por tipo de animal:\n", df.groupby("Animal type")
      ["Body Length cm"]
      .mean()
      )

print("\n5. Interpretación de resultados\n")
print(df.groupby(["Country", "Animal type"]).size().reset_index(name = "Number of observations"))
print("\nConteo de tipos de animales:\n", df["Animal type"].value_counts())
print("\nTabla de porcentajes de los tipos de animales:\n", (df["Animal type"].value_counts(normalize=True) * 100).round(2))
print("\nTabla de generos de los animales:\n", df["Gender"].value_counts())
print("\nTabla de generos por animales:\n", pd.crosstab(df["Animal type"], df["Gender"]))
print("\nTabla de generos pero con porcentajes:\n", (pd.crosstab(df["Animal type"], df["Gender"], normalize = "index") * 100).round(2))

print("\nConclusiones: ")
print("\nEl animal que más presencia presenta es la Ardilla Roja (Red Squirrel) en paises como Polonia y Alemania, dado que presentan 125 y 116 vistas, respectivamente")
print(f"Así mismo, la ardilla roja representa el 51.18% de la información de los animales, mientras que el segundo es el erizo con el 32.94%")
print(f"El animal con menor avistamientos de la BBDD es el bisonte, con apenas un 7.46% de la información (63 datos)")
print("Finalmente, vemos que la repartición de géneros de los animales está muy equilibrada, pues como se ve en las tablas, se tiene 443 machos Vs 401 hembras")
print(f"Esto en términos general vemos que es muy homogéneo, dado que los porcentajes están en alrededor de 55% al 44% de la repartición de la muestra.")