import pandas as pd                             #   Librería para manejar los DataFrames
#   Cargando el archivo de Excel
path = "P:/Personal/BootCamp in Data Science/Python_Development/Personal_Development/Datasets/Ventastaller.xlsx"
ventas = pd.read_excel(path)

#   Mini Reto 
# Pregunta 1 -> Imprimir las primeras 10 filas del DataFrame
print("Imprimiendo las primeras 10 filas del DataFrame")
print(ventas.head(10))
# Pregunta 2 -> Impimir el número de filas y columnas del DataFrame
print("Imprimiendo el número de filas y columnas del DataFrame")
print(ventas.shape)         # -> Tiene 51 filas y 9 columnas
# Pregunta 3 -> Imprimir las columnas Producto y Precio_Unitario del DataFrame
print("Imprimiendo las columnas Producto y Precio_Unitario del DataFrame")
print(ventas[["Producto", "Precio_Unitario"]])
# Pregunta 4 -> Imprimir las filas donde el Precio_Unitario sea mayor a 100.000
print("Imprimiendo las filas donde el Precio_Unitario sea mayor a 100.000")
print(ventas[ventas["Precio_Unitario"] > 100000][["Producto", "Precio_Unitario"]])
# Pregunta 5 -> Crear una columna con el Precio Final
print("Creando una columna con el Precio Final")
ventas["IVA"] = ventas["Precio_Unitario"] * 0.19
ventas["Precio_Final"] = ventas["Precio_Unitario"] + ventas["IVA"]
print(ventas.head(7))
# Pregunta 6 -> Imprimir las filas donde el Producto sea Laptop
print("Imprimiendo las filas donde el Producto sea Laptop") 
print(ventas[ventas["Producto"] == "Laptop"])