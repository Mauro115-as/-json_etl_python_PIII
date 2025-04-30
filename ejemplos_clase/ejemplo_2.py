#!/usr/bin/env python
"""
JSON ETL [Python] - Ejemplo 2
------------------------------
Ejemplo de consumo de datos desde una API y procesamiento JSON.
"""

import json
import requests


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("# ---- Ejemplos con JSON Request ---- #")

    url_single = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url_single)
    data = response.json()

    print("Primer JSON desde la nube:")
    print(json.dumps(data, indent=4))

    url_all = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url_all)
    data = response.json()

    print("\nMostrando tareas de usuarios con userId <= 2:")
    for user in data:
        if user['userId'] > 2:
            break
        print(f"Usuario {user['userId']} completó '{user['title']}'? {user['completed']}")

    print("Finalizado.")
'''

