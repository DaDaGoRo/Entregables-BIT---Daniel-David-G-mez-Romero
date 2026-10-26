import pandas as pd
import numpy as np
ventas_dia = np.array([100, 110, 115, 120, 130, 125, 900])
#   Revisando valores atípicos
q1 = np.percentile(ventas_dia, 25)
q3 = np.percentile(ventas_dia, 75)
iqr = q3 - q1                               #   irq -> Rango inter-quartílico, por sus siglas en inglés

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

atipicos = ventas_dia[
    (ventas_dia < limite_inferior) |
    (ventas_dia > limite_superior)
]

print("Q1: ", q1)
print("Q3: ", q3)
print("IRQ: ", iqr)
print("Límite Inferior: ", limite_inferior)
print("Límite Superior: ", limite_superior)
print("Valores atípicos: ", atipicos)

#   Path de Datos
path = "https://raw.githubusercontent.com/shaadyalii/Dirty-Cafe-Sales-Dataset/main/dirty_cafe_sales.csv"
df = pd.read_csv(path)
print(df.head(7))
print(df.shape)
print(df.info())
print(df.describe())

print("Valores Nulos: \n", df.isnull().sum())                                   #   Revisando Valores Nulos
print("Valores Duplicados: \n", df.duplicated().sum())                          #   Revisando Valores Duplicados

#   Veo muchas cosas con lo mencionado anteriormente, tales como que todas las variables aparecen como "str", inclusive como las de fechas, que deberían ser "date"
#   También la de "Total Spent", "Quantity", "Price per Unit", las cuales son numéticas y deberían ser de tipo "int" o "float". Debemos cambiar varias cosas.
#   Tenemos varios valores Nulos, pero no tenemos valores duplicados.

print(df["Item"].value_counts())                                                #   Veo que aparece unos valores llamados "ERROR" & "UNKNONW", revisaré las otras
print(df["Quantity"].value_counts())                                            #   También aparcen valores con esto, miremos la que sigue
print(df["Price Per Unit"].value_counts())                                      #   También están...haré un conteo en cada columna

for columna in df.columns:
    unknonw = df[columna].isin(["UNKNOWN"]).sum()
    error = df[columna].isin(["ERROR"]).sum()
    if unknonw > 0:
        print(f"Variable: {columna} | Cantidad de UBKNOWN: {unknonw}")
    if error > 0:
        print(f"Variable: {columna} | Cantidad de ERROR: {error}")

#   Tenemos muchísimos valores así...por lo que los pasaré a valores Not a Number (NaN) de la librería Numpy
df = df.replace(["ERROR", "UNKNOWN"], np.nan)
#   Revisando si sigo viendo lo de antes...
print(df["Item"].value_counts())                                                #   Efectivamente ya los logré quitar en este punto
print(df.info())                                                                #   Ya cambiamos los valores a NaN; cambiemos esto en cada variable:

#   Empezaré con "Item", cambiando los NaN por "Unknown", esto con el ánimo de sea un cambio controlado
df["Item"] =  df["Item"].fillna("Unknown")
print("Conteo de NaN en Item: ", df["Item"].isnull().sum())                     #   Ya hemos quitado los NaN en "Item"; sin embargo, las variables siguen como "str"
print(df["Quantity"].value_counts())                                            #   A pesar de ser solo números visualmente, no lo toma así, transformémolos:
df["Quantity"] = pd.to_numeric(df["Quantity"], errors = "coerce")               #   Los valores que no puedan convertirse, páselos a valores "NaN"
print(df.info())                                                                #   Ya logré volver la variable "Quantity" a formato numérico, ahora veré los NaN
df["Quantity"] = df["Quantity"].fillna(np.nanmedian(df["Quantity"]))            #   Cambié los NaN por la mediana (median), pero sin contar los NaN en el cálculo
print("Conteo de NaN en Quantity: ", df["Quantity"].isnull().sum())             #   Vemos que ya es Cero también. Ahora revisaré "Price per Unit"
print(df["Price Per Unit"].value_counts())                                      #   Pasa lo mismo que con el anterior, se "ve" como número, pasémolo:
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors = "coerce")
df["Price Per Unit"] = df["Price Per Unit"].fillna(np.nanmedian(df["Price Per Unit"]))
print("Conteo de NaN en Price Per Unit: ", df["Price Per Unit"].isnull().sum())
print(df.info())                                                                #   Vamos bien, revisemos la varibale "Total Spent":
print(df["Total Spent"].value_counts())                                         #   Igual que las anteriores...transformémosla:
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors = "coerce")         #   Creo que esto no es necesario dado que lo voy a recalcular...
df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]                       #   Recalculando ahora que "Quantity" & "Price per Unit" son numéricos
print(df["Total Spent"].head(7))                                                #   Revisando que si tenga sentido lo que acabo de hacer
print(df.info())                                                                #   Lo logramos, vamos a revisar ahora la varible "Payment Method"
print(df["Payment Method"].value_counts())                                      #   Se ve bien...revisaré sus posibles valores únicos...
print(df["Payment Method"].unique())                                            #   Se sigue viendo bien, ahora reemplazaré los NaN
#   En este caso, reemplazaré los NaN por la moda (mode) dado que la moda, en estadísitca es valor o categoría que aparece con mayor frecuencia en un 
#   conjunto de datos, y en este caso, tiene todo el sentido, dado que esta variable (Payment Method) es categórica:
#   En la siguiente linea, el [0] extrae el primer valor del resultado de .mode(). Lo necesito en esa línea porque .mode() devuelve una Serie de pandas, 
#   incluso cuando encuentra una sola moda, y yo quiero un único valor para rellenar los datos faltantes.
df["Payment Method"] = df["Payment Method"].fillna(df["Payment Method"].mode()[0])
print("Conteo de NaN en Payment Method: ", df["Payment Method"].isnull().sum()) #   Vamos bien, por lo que pasaré a la siguiente, que es "Location"
print(df["Location"].value_counts())                                            #   También se ve bien, haré los valores únicos para corroborar:
print(df["Location"].unique())                                                  #   Confirmo que esta bien, pero le haré el tema de los NaN:
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("Conteo de NaN en Location: ", df["Location"].isnull().sum())             #   Confirmo que está bien, solo me resta revisar la variable "Transaction Date"
print(df["Transaction Date"].value_counts)                                      #   Veo solo fechas aparentemente...intentaré pasarlos a formato fecha:
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"], errors = "coerce")
#   la función .astype() sirve para convertir la variable en un tipo de formato en específico, en este caso la convierto a int64 dado que Numpy debe trabajar 
#   con números. También es importante mencionar que aqui volví a usar la función de Pandas de to_timedate() dado que para sacar la mediana, debo sacarla sin
#   tener en cuenta los valores NaT (Not a Time) y esta estaba como valor numérico por el tratamiendo realizado en la librería de Numpy de nanmedian():
df["Transaction Date"] = df["Transaction Date"].fillna(
    pd.to_datetime(np.nanmedian(df["Transaction Date"].astype("int64"))))
print("Conteo de NaN en Transaction Date: ", df["Transaction Date"].isnull().sum())
print(df.info())                                                                #   Revisamos que efectivamente quedó bien hecho y las variables quedaron bien
print("Valores Nulos luego de los cambios: \n", df.isnull().sum())              #   Revisando Valores Nulos
#   Ahora que la BBDD está limpia y correcta, podemos crear nuevas variables y operar:
df["Revenue_Calculated"] = df["Quantity"] * df["Price Per Unit"]
#   Guardando la data limpia en un nuevo archivo de Excel en este caso (index=False le indica a pandas que debe guardar el Excel sin incluir el índice del DataFrame. Si pusiera index=True, lo incluirá como una columna adicional a la izquierda de tus datos. Además, True es el valor predeterminado si no especifico ese parámetro):
df.to_excel("P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/df_limpio.xlsx", index = False)
print("Se ha exportado la nueva BBDD limpia en Excel, con numbre 'df_limpio.xlsx' a la siguiente ruta:")
print("P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/df_limpio.xlsx")