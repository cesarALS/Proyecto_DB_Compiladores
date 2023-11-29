"""
Este código maneja la base de datos. Aquí se guardan las tablas de la base de datos, y se proveen las funciones
necesarias para manejarlas.
"""

TABLE_POSITION = 0
FIELDS = 1

db_counter = 1

# Registro de las bases de datos en existencia
_table_registry = {"ex_telefonos": [0, {"Nombre": "CAD", "Edad": "ENT", "Telefono": "ENT"}]}

# Bases de datos guardadas. Se guardan como listas de listas
_tables = [[["Ryan", 45, 2430909388], ["Daniela", 34, 3450890871], ["Flor", 42, 89098019288]]]

def existent_db(name: str):
    return True if name in _table_registry else False

def insert_table(tbl_name: str, fields):
    global db_counter
    _table_registry[tbl_name] = [db_counter, fields]
    db_counter += 1
