#   Parte 1
edades = [12, 17, 8, 15, 22, 9, 30, 25]                     #   Lista de edades
print("Challenge del 06/10/2026 | Parte 1")
#   Iteraciones sobre la lista de edades
for edad in edades:
    #print(f"La edad es: {edad}")                           #   Revisando que recorra la lista correctamente
    if edad == 25:
        print(f"Encontramos al estudiante de {edad} años. Deteniendo el análisis")
        break;
    elif edad < 10:
        continue;
    elif edad >= 18:
        print(f"Adulto: {edad} años")
    else:
        print(f"Menor: {edad} años")

#   Parte 2
nombres = ["Juan", "Pedro", "Jorge", "María", "Ana"]        #   Lista de nombres
print("Challenge del 06/10/2026 | Parte 2")
contador = 0;
while contador < len(nombres):
    #print("Los nombres son: ", nombres[contador])          #   Imprimiendo los nombres de la lista
    contador += 1
    if nombres[contador] == "Ana":
        print(f"{nombres[contador]} está en la lista. Deteniendo el análisis")
        break;
    elif "J" in nombres[contador]:
        continue;
    else:
        print(f"Imprimiendo el nombre: {nombres[contador]}")