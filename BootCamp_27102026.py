###     Visualización de datos con MatplotLib - Seaborn     ###
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#   Creando un DataFrame para trabajar las visualizaciones
df_line = pd.DataFrame({
    'Mes' : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    'Ventas' : [10, 35, 24, 50, 74, 80, 64, 95, 110, 104, 88, 120]
})
print(df_line.head(7))

#   Gracfico de Líneas

#   Primero usando MatplotLib
plt.figure(figsize = (6, 4))                    #   Tamaño de la figura
plt.plot(df_line['Mes'], df_line['Ventas'])     #   Eje X & Eje Y
plt.title('Ventas 2024')                        #   Título de la gráfica
plt.xlabel('Mes')                               #   Título del eje X
plt.ylabel('Promedio Ventas (Millones COP $)')  #   Título del eje Y
plt.xticks(df_line["Mes"], rotation = 45)       #   Ajuste en los nombres del eje X (Los rota un poco para leer mejor los meses)
plt.grid()                                      #   Indica que muestre una cuadrícula en el gráfico
plt.show()                                      #   Para que muestre el gráfico

#   Ahora usando Seaborn

#   Convenciones de Seaborn:
#   ha = horizontal alignment: Alinea el texto horizontalmente respecto al punto (izquierda, centro o derecha) 'left', 'center', 'right'
#   va = 	vertical alignment: Alinea el texto verticalmente respecto al punto (arriba, centro o abajo) 'top', 'center', 'bottom', 'baseline'
#   baseline, texto se alinea por su linea base
#   bottom, la parte mas baja del texto queda en el punto
#   center, centro vertical del texto queda en el punto
#   top, la parte mas alta del texto queda en el punto
plt.figure(figsize = (10, 6))
sns.lineplot(data = df_line, x = 'Mes', y = 'Ventas', marker = 's') #   market = 's' -> Le indica a Seaborn que quiero una esfera (sphere) como marcador en la gráfica
# Añadir etiquetas a la grafica
for i, txt in enumerate(df_line['Ventas']):     #   enumerate() -> Ayuda a recorrer la variable pero trayendo también el índice. Ejemplo para la irteración 1:
                                                #   0 - 10 -> Dado que para el índice cer(0) dentro de "Ventas" es diez (10), y así sucesivamente
    plt.text(df_line['Mes'][i], df_line['Ventas'][i], txt, ha = 'right', va = 'bottom')
plt.yticks(df_line['Ventas'], rotation = 35)
plt.xticks(df_line['Mes'], rotation = 45)
plt.title("Ventas 2024 con Seaborn")
plt.grid()
plt.show()

#   Cargar datos IRIS
iris = sns.load_dataset("iris")                 #   Es una base de datos de los pétalos y cépalos precargada para estudio con Seaborn
print(iris.head(7))

###     Reto
#   Datos a trabajar
df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "Ventas": [120, 150, 135, 180, 210, 195],
    "Categoria": ["A", "B", "A", "C", "B", "C"],
    "Unidades": [20, 35, 25, 40, 30, 45]
})
print(df.head(7))

#   MatplotLib
#   Gráfico de Líneas
plt.figure(figsize = (7, 3))                    #   Tamaño de la figura
plt.plot(df['Mes'],                             #   Eje X
         df['Ventas'],                          #   Eje Y
         color = 'red',                         #   Color de la línea
         linestyle = '--',                      #   Estilo de la línea
         linewidth = 2.5,                       #   Grosor de la línea
         marker = '*'                           #   Cambiando el marcador por '*' -> Estrella
         )                
plt.title('Ventas por mes')                     #   Título de la gráfica
plt.xlabel('Mes')                               #   Título del eje X
plt.ylabel('Ventas 1/2 año')                    #   Título del eje Y
plt.xticks(df["Mes"], rotation = 45)            #   Ajuste en los nombres del eje X (Los rota un poco para leer mejor los meses)
plt.grid()                                      #   Indica que muestre una cuadrícula en el gráfico
plt.show()                                      #   Para que muestre el gráfico

#   Seaborn
#   Gráfico de barras
sns.set_style('darkgrid')                       #   Cambiando el estilo visual del fondo
plt.figure(figsize = (10, 5))                   #   Tamaño de la gráfica
sns.barplot(                                    #   Gráfico de barras con Seaborn
    data = df,                                  #   Selección de la data
    x = "Categoria",                            #   Eje X
    y = "Unidades",                             #   Eje Y
    palette = 'bright',                         #   Seleccionando paleta de colores 'Brillante'
    hue = 'Categoria',                          #   Permite diferenciar los datos mediante colores
    legend = True                               #   Controla si se muestra la leyenda
)
plt.xlabel('Categoría')
plt.ylabel('Unidades')
plt.title("Unidades x Categoría con Seaborn")
plt.grid()
plt.show()