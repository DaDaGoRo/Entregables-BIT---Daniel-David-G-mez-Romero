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
df_ventas["descuento"] = pd.to_numeric(                                 #   Dado que lo había cambiado a "str" ahora vuelvo la variable numérica de nuevo
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
#   Revisión de Edades
#   Filtro para traer las variables "id_venta", "cliente" y "edad_cliente" pero que solo traiga las filas en las que "edad_cliente" tenga valores menores de 10
#   Otra forma de verlo es que la condicón lógica se aplica, en este ejemplo, en las filas (edad < 10) -> Continuación de la explicación abajo :)
#   Mientras que en las columnas se aplicó el filtro de las columnas que quiero. Por último pido solamente las primeras 25 filas
print(df_ventas[df_ventas["edad_cliente"] < 10][["id_venta", "cliente", "edad_cliente"]].head(25))
print(df_ventas.head())                                                 #   Mirando el DataFrame corto para el ejemplo que quiero hacer.
print(df_ventas["id_venta"][2])                                         #   Trayendo el valor de la fila 3 (Python cuenta desde 0) de la Columna "id_cliente"
print(df_ventas.iloc[2,0])                                              #   Lo mismo pero con la función iloc() -> Aquí primero va la fila y luego la columna (No se cuenta como columna la del índice) 
print(df_ventas.loc[2, "id_venta"])                                     #   Lo mismo pero con la función loc() -> Aquí primero va la fila y luego la columna

#   Existen valores de edad que no son lógicos, mirémoslos:
print(df_ventas[
    (df_ventas["edad_cliente"] < 10 ) |                                 #   Edades menores a 10 años
    (df_ventas["edad_cliente"] > 100)                                   #   Edades mayores a 100 años   
    ][["id_venta", "cliente", "edad_cliente"]])                         #   Columnas que quiero ver. Nota: Si fuera una sola Columna, podría ir sin doble corchete; sin embargo, como son varias Columnas, debo poner doble corchete cuadrado.
#   Dejaré estos valores incrrectos como valores no disponibles (NA -> Not Available) -> Para esto, tomaré el filtro que acabo de crear arriba
df_ventas.loc[(                                                         #   Como mostré antes, con la función loc(), primero debo poner las filas a buscar
    (df_ventas["edad_cliente"] < 10 ) |                                 #   Edades menores a 10 años
    (df_ventas["edad_cliente"] > 100)                                   #   Edades mayores a 100 años   
    ), "edad_cliente"] = pd.NA                                          #   Aqui pondré la columna que quiero modificar en la función loc()
                                                                        #   Con el igual (=) indico que efectivamente esas edades "raras" las cambie por "No disponibles"
#   Revisaré que ya no existan estas edades raras: -> Si vemos el resultado, efectivamente lo logramos, dado que dice "Empty DataFrame", es decir, que quedó bien
print(df_ventas[
    (df_ventas["edad_cliente"] < 10 ) |                                 
    (df_ventas["edad_cliente"] > 100)                                      
    ][["id_venta", "cliente", "edad_cliente"]])

#   Revisaré ahora la variable cantidad para verificar si existen valores por debajo de cero:
print(df_ventas[df_ventas["cantidad"] <= 0]["cantidad"].head(7))        #   Como solo quise ver la variable "cantidad", pude usar solo un corchete cuadrado al final
#   Como se vio, existen valores negaticos que no tienen sentido, por lo cual los eleminaré del DataFrame, pero antes de eso, sacaré esos datos y los guardaré
#   en otra variable por si los necesitaré a futuro. Esto lo haré con la función copy(), así:
backup_cantidad = df_ventas["cantidad"].copy()
print(backup_cantidad)

#   Sacando un backup de la base de datos antes de borrar la información de "cantidad" que no tienen sentido en sus números
backup_ventas = df_ventas.copy()
print(backup_ventas)
print(df_ventas["cantidad"].describe())                                 #   Revisando la cantidad de información en la variable "cantidad" antes de borrar
#   Mirando todas las filas a eliminar -> En total son 28
print(df_ventas[df_ventas["cantidad"] <= 0][["id_venta", "cliente", "precio_unitario", "cantidad"]].head(30))
#   Sacando el ínidice de esos 28 registros:
print(df_ventas[df_ventas["cantidad"] <= 0].index)                      #   Con el atrinbuto "index" puedo específicamente solicitar los ínidex del filtro realizado
#   Eliminando información errada mediante los índices:
df_ventas.drop(df_ventas[df_ventas["cantidad"] <= 0].index, inplace = True)
#   inplace=True indica que drop() debe modificar directamente el DataFrame df_ventas, en lugar de devolver otro DataFrame con las filas eliminadas. Por eso no fue necesario escribir df_ventas = ...
print(df_ventas["cantidad"].describe())                                 #   Revisando la cantidad de información en la variable "cantidad" luego de borrar
print(df_ventas.shape)

#   Revisando ahora valores en la variable "precio_unitario"
print("Variable precio_unitario")
print(df_ventas["precio_unitario"].unique())
print(df_ventas["precio_unitario"].describe())
#   Veo que hay valores como 0, también -50000, NA, entre otros. Veamolos en un filtro:
print(df_ventas[df_ventas["precio_unitario"] <= 0])
#   Veo que no son tantos, por lo que los voy a sumar para ver cuantos son:
print("La cantidad de filas son: ", (df_ventas["precio_unitario"] <= 0).sum())
#   Pero también veo que hay valores cercanos a 100 Millones. Esos los veremos con el siguiente filtro:
print(df_ventas[df_ventas["precio_unitario"] >= 99000000])
#   Veo que no son tantos (igual que los valores que son por debajo de 0), por lo que los voy a sumar y verificar cuantos son:
print("Las filas en total que tienen ese número tan grande son: ", (df_ventas["precio_unitario"] >= 99000000).sum())
#   Vamos a eliminar ambos valores atipicos (tanto los iguales o menores de 0 y los cercanos a 100 Millones), es decir, eliminaremos 29 registros
#   Primero los 16 menores o iguales a 0:
df_ventas.drop(df_ventas[df_ventas["precio_unitario"] <= 0].index, inplace = True)
#   Ahora vamos por las 13 que son cercanas a los 100 Millones
df_ventas.drop(df_ventas[df_ventas["precio_unitario"] >= 99000000].index, inplace = True)
print(df_ventas.shape)                                                  #   Aqui quiero ver que el DataFrame tenga un tamaño de 1223 - 29 = 1194 y las 12 variables

#   A partir de ahora, miraré cada variable en orden para no olvidar ninguna.
#   Ya he revisado y modificado las varibles de "id_venta", "fecha", "ciudad", por lo que voy a seguir con "producto"
#   No mencioné nada sobre la variable "cliente", dado que son nombres propios, no corresponde revisarla para modificarla
print(df_ventas["producto"].unique())                                   #   Revisando valores unicos en la variable "producto"
print(df_ventas["producto"].value_counts())                             #   Revisandolos en detalle y contándolos

#   La variable se ve bien y no parece necesitar "limpiarla", por lo que seguiré con la siguiente que es "metodo_pago": 
print(df_ventas["metodo_pago"].unique())                                #   Revisando valores unicos en la variable "producto"
print(df_ventas["metodo_pago"].value_counts())                          #   Revisandolos en detalle y contándolos
#   Se ve que tiene varios valores por mejorar y corregir ortografía, por lo que haremos el tratamiento:
df_ventas["metodo_pago"] = (df_ventas["metodo_pago"].str.strip()
                            .str.title())
#   Revisemos si quedó bien: -> Si, efectivamente ya quedaron bien
print(df_ventas["metodo_pago"].unique())                                #   Revisando valores unicos en la variable "metodo_pago"
print(df_ventas["metodo_pago"].value_counts())                          #   Revisandolos en detalle y contándolos

#   Finalmente queda revisar la variable "vendedor", dado que las otras ya las trabajé: -> Veo que también está bien.
print(df_ventas["vendedor"].unique())                                   #   Revisando valores unicos en la variable "vendedor"
print(df_ventas["vendedor"].value_counts())                             #   Revisandolos en detalle y contándolos
#   Crear una variable llamada "subtotal"
df_ventas["subtotal"] = df_ventas["precio_unitario"] * df_ventas["cantidad"]
#   Crear una variable llamada "valor_descuento"
df_ventas["valor_descuento"] = df_ventas["subtotal"] * df_ventas["descuento"]

#   La data está correcta y limpia, por lo que veré el resultado final:
print("\nEl resultado final luego de la limpieza es: \n")
print("DataFrame Head: \n", df_ventas.head(7))
print("\nDataFrame Tail: \n", df_ventas.tail(7))
print("\nInformación: \n"), df_ventas.info()
print("\nDescripción: \n", df_ventas.describe(include = "all"))
print("\nEl tamaño del DataFrame luego de la limpieza es: ", df_ventas.shape)
#   Guardando la data limpia en un nuevo archivo de Excel en este caso (index=False le indica a pandas que debe guardar el Excel sin incluir el índice del DataFrame. Si pusiera index=True, lo incluirá como una columna adicional a la izquierda de tus datos. Además, True es el valor predeterminado si no especifico ese parámetro):
df_ventas.to_excel("P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/df_ventas_limpio.xlsx", index = False)