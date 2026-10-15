import pandas as pd                                                     #   Librería para manejar los DataFrames
#   Cargando el archivo de Excel    
path = "P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/df_ventas.csv"
df_ventas = pd.read_csv(path)       
print(df_ventas.head(7))                                                #   Imprimiendo las primeras 7 filas del DataFrame
df_ventas.info()                                                        #   Información general del DataFrame
print(df_ventas.describe(include = "all"))                              #   Estadísticas descriptivas del DataFrame
print(df_ventas.isnull())                                               #   Verificando si hay valores nulos en el DataFrame
print(df_ventas.isnull().sum())                                         #   Contando los valores nulos por columna
print(df_ventas[df_ventas["ciudad"].isnull()].head(30))                 #   Mirando los 26 registros de la columna "ciudad"
#   Para el caso de la variable "ciudad", los NaN los cambiaré por texto con el valor de "Desconocida" con la función "fillna()"
df_ventas["ciudad"] = df_ventas["ciudad"].fillna("Desconocida")
print(df_ventas.isnull().sum())                                         #   Contando los valores nulos por columna luego del cambio en la viariable "ciudad"
print(df_ventas[df_ventas["edad_cliente"].isnull()].head(30))           #   Mirando los 28 registros de la columna "edad_cliente"
#   Para el caso de la variable "edad_cliente", los NaN los cambiaré por la mediana de la edad
df_ventas["edad_cliente"] = df_ventas["edad_cliente"].fillna(df_ventas["edad_cliente"].median())
print(df_ventas.isnull().sum())                                         #   Contando los valores nulos por columna luego del cambio en la viariable "edad_cliente"
print(df_ventas.duplicated())                                           #   Revisando valores duplicados
print(df_ventas.duplicated().sum())                                     #   Contando valores duplicados -> Dice que tiene 24 valores duplicados
print(df_ventas.iloc[df_ventas.duplicated()])                           #   Mostrando los 24 valores duplicados mediante la función "iloc"
#   Eliminando los datos Duplicados
df_ventas = df_ventas.drop_duplicates()
print(df_ventas.shape)                                                  #   Mirando el nuevo tamaño de los datos
#   Unificando información sobre la variable "ciudad"
print(df_ventas["ciudad"])                                              #   Se imprimen los valores y se evidencia que tienen diferentes formas de escritura
df_ventas["ciudad"] = df_ventas["ciudad"].str.strip()                   #   Elimina espacios al inicio y al final
df_ventas["ciudad"] = df_ventas["ciudad"].str.title()                   #   Deja las iniciales en Mayúscula y el resto en Minúsculas
#   Escribiendo correctamente el nombre de la capital de Colombia
new_ventas = df_ventas["ciudad"].str.replace("Bogota", "Bogotá")        #   Escribiendo correctamente el nombre de la capital de Colombia.
df_ventas["ciudad"] = new_ventas                                        #   Recordar que la función str.replace no modifica la cadena original, por eso cree otra
new_ventas = df_ventas["ciudad"].str.replace("Medellin", "Medellín")    #   Haciendo lo mismo para la capital del Departamento de Antioquia
df_ventas["ciudad"] = new_ventas
print(df_ventas["ciudad"])                                              #   Revisando cambios
print(df_ventas["ciudad"].value_counts())                               #   Revisando que las ciudades hayan quedado bien escritas y sean únicas
#   Revisando la variable "categoria"
print(df_ventas["categoria"].value_counts())
#   Arreglando la categoría "Tecnología" en una sola linea y finalmente haciendo lo propio con "Papelería":
df_ventas["categoria"] = (df_ventas["categoria"].str.strip().           #   Quitando espacios a inicio y final
                          str.title().                                  #   Dejando la primera en Mayúscula y el resto en Minúscula
                          str.replace("Tecnologia", "Tecnología", regex = False).   #   Reemplazando el Texto sin tilde sin necesidad de otra variable
                          str.replace("Papeleria", "Papelería", regex = False)      #   regex = False -> Buscará exactamente ese texto
                          )   
print(df_ventas["categoria"].value_counts())                            #   Revisando cambios
df_ventas["cliente"] = df_ventas["cliente"].str.strip()                 #   Quitando espacios a inicio y final
print(df_ventas.info())                                                 #   Revisando estadísticas del DataFrame
#   Realizando lo propio con "precio_unitario"
print(df_ventas["precio_unitario"].head(7))
df_ventas["precio_unitario"] = (df_ventas["precio_unitario"]
                                .astype("string")                       #   Convierto toda la variable en texto para poder eliminar los símbolos "$" y "."
                                .str.replace("$", "", regex = False)    #   Quitando el símbolo "$"
                                .str.replace(".", "", regex = False)    #   Quitando el símbolo "."
                                )
df_ventas["precio_unitario"] = pd.to_numeric(                           #   Dado que lo había cambiado a "str" ahora vuelvo la variable numérica de nuevo
    df_ventas["precio_unitario"],
    errors = "coerce"                                                   #   Los valores que no puedan convertirse, páselos a valores "NaN"
    )          
print(df_ventas["precio_unitario"].head(7))                             #   Revisando cambios
print(df_ventas.info())                                                 #   Revisando estadísticas del DataFrame
print(df_ventas.isnull().sum())                                         #   Contando los valores nulos por columna
print(df_ventas[df_ventas["precio_unitario"].isnull()])                 #   Revisando los valores nulos que quedaron en "precio_unitario"
#   Realizando lo propio con "descuentos"
print(df_ventas["descuento"].head(7))
df_ventas["descuento"] = (df_ventas["descuento"]
                                .astype("string")                       #   Convierto toda la variable en texto para poder eliminar el símbolo "%"
                                .str.replace("%", "", regex = False)    #   Quitando el símbolo "%"
                                )
df_ventas["descuento"] = pd.to_numeric(                           #   Dado que lo había cambiado a "str" ahora vuelvo la variable numérica de nuevo
    df_ventas["descuento"],
    errors = "coerce"                                                   #   Los valores que no puedan convertirse, páselos a valores "NaN" (Not a Nummber)
    )
df_ventas["descuento"] = df_ventas["descuento"] / 100                   #   Para que quede en lugar de 10% quede en 0.1, a modo de ejemplo
print(df_ventas["descuento"].head(7))                                   #   Revisando los cambios
print(df_ventas.info())                                                 #   Revisando estadísticas del DataFrame     
#   Cambiando un poco el formato de la variable "fecha"
df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"],                 #   Cambiando el tipo de variable "fecha" y poniendolo en formato valido de Fecha
                                    format = "mixed",                   #   Para que revise cada valor de "fecha" de forma individual
                                    dayfirst = True,                    #   La documentación menciona que si pones "mixed" en format, acompáñalo de dayfirst
                                    errors = "coerce"                   #   Los valores que no puedan convertirse, páselos a valores "NaT" (Not a Time)
                                    )                  
print(df_ventas.info())                                                 #   Revisando estadísticas del DataFrame