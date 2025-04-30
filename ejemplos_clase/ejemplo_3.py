#!/usr/bin/env python
"""
JSON ETL [Python] - Ejemplo 3
------------------------------
Ejemplo de proceso ETL con datos desde una API
y visualización animada con matplotlib.
"""

import json
import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def extract(url):
    """Extraer el JSON desde la URL proporcionada."""
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    """Transformar los datos JSON en listas separadas para graficar."""
    x = [item['time'] for item in data]
    y = [item['signal'] for item in data]
    return x, y


def load(x, y):
    """Actualizar los datos del gráfico."""
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return line,


def update_animation(frame):
    """Actualizar animación con nuevos datos extraídos de la API."""
    url = 'http://inove.pythonanywhere.com/monitor/sensor'
    data = extract(url)
    x, y = transform(data)
    return load(x, y)


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("# ---- Ejemplo ETL con animación ---- #")

    # Inicializar gráfico
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_title("Sensor en tiempo real")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Señal")

    # Crear animación
    animation = FuncAnimation(fig, update_animation, interval=1000)

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()

    print("Finalizado.")
