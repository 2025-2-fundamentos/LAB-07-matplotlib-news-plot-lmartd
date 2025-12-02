import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Genera la gráfica de tendencias de fuentes de noticias.
    Guarda la imagen como 'files/plots/news.png'.
    """

    # Crear figura
    plt.figure()

    # Colores por categoría
    colores_medios = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    # Z-order y grosor de línea por categoría
    orden_z = {"Television": 1, "Newspaper": 1, "Internet": 2, "Radio": 1}

    ancho_linea = {"Television": 2, "Newspaper": 2, "Internet": 4, "Radio": 2}

    # Cargar datos
    datos = pd.read_csv("files/input/news.csv", index_col=0)

    # Graficar líneas
    for medio in datos.columns:
        plt.plot(
            datos[medio],
            color=colores_medios[medio],
            label=medio,
            zorder=orden_z[medio],
            linewidth=ancho_linea[medio],
        )

    # Estilo del gráfico
    plt.title("How people get their news", fontsize=16)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_visible(False)

    # Etiquetas iniciales y finales por medio
    for medio in datos.columns:
        anio_inicio = datos.index[0]
        valor_inicio = datos.loc[anio_inicio, medio]

        plt.scatter(
            anio_inicio,
            valor_inicio,
            color=colores_medios[medio],
            zorder=orden_z[medio],
        )
        plt.text(
            anio_inicio - 0.2,
            valor_inicio,
            f"{medio} {valor_inicio}%",
            ha="right",
            va="center",
            color=colores_medios[medio],
        )

        anio_fin = datos.index[-1]
        valor_fin = datos.loc[anio_fin, medio]

        plt.scatter(
            anio_fin, valor_fin, color=colores_medios[medio], zorder=orden_z[medio]
        )
        plt.text(
            anio_fin + 0.2,
            valor_fin,
            f"{valor_fin}%",
            ha="left",
            va="center",
            color=colores_medios[medio],
        )

    # Etiquetas en eje x
    plt.xticks(ticks=datos.index, labels=datos.index, ha="center")

    # Guardar imagen
    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()  # Cerrar la figura para liberar memoria