#!/usr/bin/env python
"""
JSON ETL [Python] - Ejemplos de clase corregidos
Autor: Mauro Gabriel Gonza Roda
Version: 2.1

Descripcion:
Ejemplos de creación, serialización y deserialización de JSON en Python
"""

import json

def crear_json():
    max_json = {
        "nombre": "Max",
        "apellido": "Power",
        "hijos": [
            {"firstName": "Alice", "age": 6},
            {"firstName": "Bob", "age": 8}
        ]
    }

    emma_json = {
        "nombre": "Emma",
        "apellido": "Thompson",
        "hijos": []
    }

    json_test = {"max": max_json, "emma": emma_json}

    print("--- JSON como objeto ---")
    print(emma_json)

    print("--- JSON serializado (string) ---")
    print(json.dumps(emma_json, indent=4))

    print("--- JSON combinado como objeto ---")
    print(json_test)

    print("--- JSON combinado serializado ---")
    print(json.dumps(json_test, indent=4))

def serializar_json():
    estudiante = {
        "nombre": "Max",
        "apellido": "Power",
        "materias": [
            {"asignatura": "matematica", "estado": "en curso"},
            {"asignatura": "lengua", "estado": "finalizado"}
        ]
    }

    with open('mi_json.json', 'w') as jsonfile:
        json.dump([estudiante], jsonfile, indent=4)

def deserializar_json():
    nuevo_estudiante = {
        "nombre": "Jean",
        "apellido": "Gray",
        "materias": [
            {"asignatura": "matematica", "estado": "finalizado"},
            {"asignatura": "lengua", "estado": "finalizado"}
        ]
    }

    with open('mi_json.json', 'r') as jsonfile:
        datos = json.load(jsonfile)

    datos.append(nuevo_estudiante)

    with open('mi_json.json', 'w') as jsonfile:
        json.dump(datos, jsonfile, indent=4)

    print("--- Contenido actualizado de mi_json.json ---")
    with open('mi_json.json', 'r') as jsonfile:
        print(json.dumps(json.load(jsonfile), indent=4))

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("# ---- Ejemplos con JSON ---- #")
    crear_json()
    serializar_json()
    deserializar_json()
    print("Terminamos")
