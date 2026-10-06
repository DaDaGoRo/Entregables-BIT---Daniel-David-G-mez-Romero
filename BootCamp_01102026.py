#   Challenge del 01/10/2026
#   Inventario de una Tienda
inventario = [
    {"producto" : "camisa",
    "precio" : 25900,
    "stock" : "11"},
    {"producto" : "pantalón",
     "precio" : 39900,
     "stock" : "23"}
]

#   Paso 1 -> Agregar un nuevo producto al inventario
inventario.append({"producto" : "abrigo", "precio" : 50000, "stock" : "2"})
print("Inventario actualizado: ", inventario)

#  Paso 2 -> Convertir los valores de la variable "stock" a tipo entero
for item in inventario:
    item["stock"] = int(item["stock"])
print("Inventario con stock convertido a entero: ", inventario)

#  Paso 3 -> Actualiza el Precio de cada Producto Sumando 10000 al precio original
for precio in inventario:
    precio["precio"] += 10000
print("Inventario con precios actualizados: ", inventario)

#  Paso 4 -> Imprimir cada producto del Inventario con el formato "Print(f....)"
for item in inventario:
    print(f"Hay {item['stock']} unidades del producto {item['producto']}. Su precio por unidad es de {item['precio']}")