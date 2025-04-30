# JSON ETL [Python]
# Ejercicio 1 - Serialización y deserialización

import json

def serializar():
    """Genera y guarda un archivo JSON con datos personales simulados."""
    print("Función que genera un archivo JSON")

    persona = {
        "nombre": "Juan",
        "apellido": "Pérez",
        "DNI": "12345678",
        "elementos_vestir": [
            {"prenda": "zapatilla", "cantidad": 3},
            {"prenda": "campera", "cantidad": 2}
        ]
    }

    with open('mi_persona_json.json', 'w', encoding='utf-8') as archivo:
        json.dump([persona], archivo, indent=4)
        print("Archivo 'mi_persona_json.json' generado con éxito.")


def deserializar():
    """Lee un archivo JSON, muestra el contenido de forma formateada."""
    print("Función que lee un archivo JSON")

    try:
        with open('mi_persona_json.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        json_string = json.dumps(datos, indent=4)
        print("Contenido del archivo:")
        print(json_string)
    except FileNotFoundError:
        print("No se encontró el archivo. Asegúrese de ejecutar primero 'serializar()'.")


if __name__ == '__main__':
    print("Ejecutando ejercicio 1...")
    serializar()
    deserializar()
    print("Finalizado.")
