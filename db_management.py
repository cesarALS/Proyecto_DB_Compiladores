"""
Este código maneja la base de datos. Aquí se guardan las tablas de la base de datos, y se proveen las funciones
necesarias para manejarla.
"""


# Registro de las bases de datos en existencia
_database_registry = {"ex_telefonos": [["Nombre", "STRING"], ["Edad", "INT"], ["Telefono", "INT"]]}

# Bases de datos guardadas. Se guardan como listas de listas
_dbs = [[["Ryan", 45, 2430909388], ["Daniela", 34, 3450890871], ["Flor", 42, 89098019288]]]

def existent_db(name: str):
    return True if name in _database_registry else False
