import matplotlib.pyplot as plt

def visual_zone(ArrayZonas):
    nombres_zonas = ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Out of range"]
    colores_barras = ['skyblue', 'lime', 'gold', 'orange', 'red', 'darkred']

    fig, ax = plt.subplots()

    # Fondo negro para toda la figura
    fig.patch.set_facecolor('black')

    # Fondo negro para el área del gráfico
    ax.set_facecolor('black')

    # Dibujar las barras
    ax.bar(nombres_zonas, ArrayZonas, color=colores_barras)

    # Cambiar color de títulos y etiquetas a blanco
    ax.set_title("Porcentage de zonas trabajadas", color='white')
    ax.set_xlabel("Zonas", color='white')
    ax.set_ylabel("Cantidad de muestras", color='white')

    # Cambiar color de los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.tight_layout()
    plt.show()



