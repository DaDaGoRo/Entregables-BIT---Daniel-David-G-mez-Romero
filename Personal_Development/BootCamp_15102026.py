import numpy as np                                                                  #   Importación de librería Numpy
print("Versión de Numpy: ", np.__version__)                                         #   Imprimiendo la versión de Numpy instalada

#   Explorando funcionalidades de Numpy
ventas = np.array([120, 150, 90, 200, 180])
print("Ventas: ", ventas)
print("Tipo de Objeto: ", type(ventas))
print("Tamaño: ", ventas.shape)
print("Número de dimensiones: ", ventas.ndim)
print("Tipo de Dato: ", ventas.dtype)
print("Cantidad de elementos (size): ", ventas.size)
ventas_ajustadas = ventas * 1.10                                                    #   Aumentando un 10%
print("Ventas originales: ", ventas)
print("Ventas ajustadas: ", ventas_ajustadas)
print("Tipo de Dato: ", ventas_ajustadas.dtype)                                     #   Como luego del cálculo salió un punto ".", usé esto para cobfirmar que es Float
#   ¿Qué pasaría si quisiera operarlo con Listas en lugar de un arreglo de Numpy?
lista_ventas = list((120, 150, 90, 200, 180))                                       #   La función list() recibe un iterable, no varios valores por separado
lista_ajustada = lista_ventas * 2                                                   #   Primera restricción, no puedo operar una lista por valores "float", debe ser de tipo entero (int)
print(lista_ventas)
print(lista_ajustada)                                                               #   Segunda restricción, la operación que hizo fue "duplicar" la información de la lista, no operar valor por valor....tendría que hacer un ciclo for y operar cada elemento, pero es poco práctico

#   Realizando la "Actividad 1"
print("\nActividad 1: ")
#   1. Las ventas con un descuento Equivalente al 5% del valor original
ventas_reduccion = ventas * 0.95
print(f"Las ventas con un 5% de descuento son: ", ventas_reduccion)
#   2. Ventas Incrementas en 25 Unidades
ventas_incrementadas25 = ventas + 25
print("Ventas incrementasa en 25 Unidades: ", ventas_incrementadas25)
#   3. El doble de cada valor vendido
ventas_dobles = ventas * 2
print("El doble de cada valor vendido es: ", ventas_dobles)

#   Arrays de varias dimensiones
ventas_sucursales = np.array([
    [120, 150, 100],                                                                #   Sucursal A
    [90, 200, 170],                                                                 #   Sucursal B
    [160, 140, 210]                                                                 #   Sucursal C
])
print(ventas_sucursales)
print("Forma: ", ventas_sucursales.shape)
print("Primera Sucursal: ", ventas_sucursales[0])
print("Segundo día de todas las sucursales: ", ventas_sucursales[:, 1])

#   Realizando la "Actividad 2"
print("\nActividad 2: ")
#   Utilizar la indexación para obtener: 1. Las ventas de la tercera sucursal
print("Las ventas de la 3ra sucursal fueron: ", ventas_sucursales[2])
#   2. Ventas del primera día de todas las sucursales
print("Ventas del 1er día de TODAS las sucursales fueron: ", ventas_sucursales[:, 0])
#   3. La venta del segundo día de la Sucursal B
print("La venta del 2do día de la Sucursal B fue: ", ventas_sucursales[1, 1])

#   Estadística Descriptiva
ventas_semana = np.array([120, 150, 90, 200, 180, 160, 140])
print("Total vendido: ", np.sum(ventas_semana))
print("Promedio: ", np.mean(ventas_semana))
print("Mediana: ", np.median(ventas_semana))
print("Desviación estándar: ", np.std(ventas_semana))
print("Mínimo: ", np.min(ventas_semana))
print("Máximo: ", np.max(ventas_semana))
print("Percentil 75: ", np.percentile(ventas_semana, 75))

#   Realizando la "Actividad 3"
print("\nActividad 3: ")
#   Usar filtros para responder: 1. ¿Que ventas fueron inferiores a 100?
print("La(s) venta(s) inferior(es) a 100, fueron en total de: ", np.sum([ventas < 100]))
print("La(s) ventas(s) menor(es) a 100 fue(ron) de: ", ventas[ventas < 100])
#   2. Qué ventas fueron iguales o superiores a 180?
print("La(s) venta(s) que fueron iguales o superiores a 100, fueron en total de: ", np.sum([ventas >= 100]))
print("Las ventas mayores o iguales a 100 fueron de: ", ventas[ventas >= 100])
#   3. Qué porcentaje de días tuvo ventas inferiores a 100?
print("El porcentaje de días de ventas inferiores a 100 fue de: ", ( np.sum(ventas < 100) / ventas.shape[0] ) * 100, " %")

#   Valores faltantes y funciones:
ventas_incompletas = np.array([120, 150, np.nan, 200, 180, np.nan])
print("Máscara de valores faltantes: ", np.isnan(ventas_incompletas))
print("Cantidad de valores faltantes: ", np.sum(np.isnan(ventas_incompletas)))
print("Promedio normal: ", np.mean(ventas_incompletas))
print("Promedio ignorando NaN: ", np.nanmean(ventas_incompletas))

#   Agregaciones por filas y columnas
ventas_sucursales2 = np.array([
    [120, 150, 180],
    [90, 200, 170],
    [160, 140, 210]
])
print("Total por sucursal: ", np.sum(ventas_sucursales2, axis = 1))                 #   Axis = 1 -> Indica a Python que opere sobre las filas
print("Total por día: ", np.sum(ventas_sucursales2, axis = 0))                      #   Axis = 0 -> Indica a Python que opere sobre las columnas
print("Promedio por sucursal: ", np.mean(ventas_sucursales2, axis = 1))

#   Realizando la "Actividad 4"
print("\nActividad 4: ")
#   1. Calcula el promedio de ventas por día entre las tres sucursales
print("Promedio de ventas por día de las 3 Sucursales: ", np.mean(ventas_sucursales2, axis = 0))
#   2. ¿Qué sucursal tiene el mayor total vendido?
print("La sucursal con mayor ventas es la: ", 
      np.argmax(np.sum(ventas_sucursales2, axis = 1)) + 1,                          #   np.argmax() -> Devuelve la posición donde está el máximo
      ". Dado que el total de esta fue de: ",                                       #   En el anterior, le sumé 1, dado que el inidice empieza en 0
      np.max(np.sum(ventas_sucursales2, axis = 1)))

#   Tareas
#   Resuelve las siguientes preguntas usando Numpy:
print("\nTareas")
#   1. Calcula el total de unidades vendidas.
print("La cantidad de unidades venidas en todas las sedes es: ", np.sum(ventas_sucursales2))
#   2. Calcula el promedio y la mediana.
print("Promedio: ", np.mean(ventas_sucursales2, axis = 1), "\nMediana: ", np.median(ventas_sucursales2, axis = 1))
#   3. Identifica los días con ventas inferiores a 100.
print("Días con ventas < a 100: ", np.sum(ventas_sucursales2 < 100))
#   4. Calcula el porcentaje de días con ventas superiores a 150.
print("Porcentaje de días con ventas > 150 es del ", np.mean((np.sum(ventas_sucursales2, axis=0)) > 150) * 100, "%")
#   5. Usa np.where() para asignar la etiqueta "ALERTA" a las ventas inferiores a 100 y "NORMAL" al resto.
print("Usando la función np.where(): \n", np.where(ventas_sucursales2<100, "ALERTA", "NORMAL"))
#   6. Escribe dos conclusiones que puedan ser útiles para el gerente.
print("Solo en el primer día las ventas en la Sucursal B fueron inferiores a 100, además en promedio, todas las sucursales son vendieron en promedio más de 100 unidades por día y la Sucursal C es la más próspera")