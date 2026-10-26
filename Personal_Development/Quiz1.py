#   Pregunta 1
x = 10
x += 5
print(x)

#   Pregunta 3
precio = 15000
cantidad = 4
total = precio * cantidad
print(total)

#   Pregunta 6
ciudades = ["Bogotá" , "Pereira" , "Cali"]
print(ciudades[1])

#   Pregunta 7
numeros = [10, 20, 30, 40]
print(numeros[-1])

#   Pregunta 10
estudiante = {"nombre" : "Laura",
              "nota" : 4.2}
estudiante["ciudad"] = "Cali"
print(estudiante["ciudad"])

#   Pregunta 11
producto = {"nombre" : "Teclado",
            "precio" : 80000}
print(producto["precio"])

#   Pregunta 13
ventas = 850000
if ventas >= 1000000:
    print("Meta Alcanzada")
else:
    print("Meta Pendiente")

#   Pregunta 14
nota = 4
if nota >= 3 and nota <= 5:
    print("Aprobado")
else:
    print("Reprobado")

#   Pregunta 15
contador = 0
while contador < 3:
    print(contador)
    contador += 1

#   Pregunta 17
for i in range (1, 4):
    print(i)

#   Pregunta 19
productos = {"mouse" : 3,
             "teclado" : 8,
             "monitor" : 0}
for nombre, cantidad in productos.items():
    if cantidad == 0:
        print(nombre, "Agotado")