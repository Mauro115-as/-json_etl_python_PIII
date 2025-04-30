# JSON ETL [Python]
# Ejercicio 2 - Consumo de API y gráfico de barras

import json
import requests
import matplotlib.pyplot as plt

def bar_plot(lista_userId, lista_completed):
    """Genera un gráfico de barras de tareas completadas por usuario."""
    fig = plt.figure()
    fig.suptitle('Títulos completados por usuario', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(lista_userId, lista_completed, color='skyblue')
    ax.set_xlabel("User ID")
    ax.set_ylabel("Títulos completados")
    ax.set_facecolor('whitesmoke')
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.legend(["Títulos completados"])
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print("Ejecutando ejercicio 2...")

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    # Convertimos la respuesta a JSON
    data = response.json()

    # Contador de tareas completadas por usuario
    completados_por_usuario = {user_id: 0 for user_id in range(1, 11)}

    for item in data:
        if item['completed']:
            completados_por_usuario[item['userId']] += 1

    # Preparar datos para graficar
    lista_userId = list(completados_por_usuario.keys())
    lista_completed = list(completados_por_usuario.values())

    # Mostrar gráfico
    bar_plot(lista_userId, lista_completed)

    print("Finalizado.")
