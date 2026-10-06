#   Paso 1
#   Diccionario con datos del producto
producto = {
    "Nombre": "Laptop",
    "Precio": 12000000.00,
    "Cantidad_bodega": 1,
    "Disponible": True,
}

#   Paso 2
#   Calculando el costo del impuesto (19%)
Impuesto = producto["Precio"] * 0.19
print(f"El valor del impuesto es de: {Impuesto}")

#   Paso 3
#   ¿Hay stock disponible Y es mayor a cero?
print("¿Hay stock disponible Y es mayor a cero?")
print((producto["Disponible"] == True) & (producto["Cantidad_bodega"] > 0))

#   Paso 4
#   Confirmar el tipo (type) de cada variable del prodcuto
for key, value in producto.items():
    print(f"El tipo de la variable {key} es de tipo {type(value)}")