from collections import OrderedDict
from sys import stdout

"""
Este código maneja la base de datos. Aquí se guardan las tablas de la base de datos, y se proveen las funciones
necesarias para manejarlas.
"""

TABLE_POSITION = 0
FIELDS = 1

num_tables = 1

class DBTable:
    def __init__(self, fields: OrderedDict, initial_registers=None):
        self.fields = fields
        self.registers = initial_registers if initial_registers is not None else []

    def insert_register(self, data: list):
        pass

    def query_table(self):
        for field in self.fields:
            stdout.write(field)
            stdout.write("  ")
        stdout.flush()

        print("\n")
        for register in self.registers:
            print(register)


# Registro de las bases de datos en existencia
_table_registry = OrderedDict()
_table_registry["ex_telefonos"] = DBTable(OrderedDict({"Nombre": "CAD", "Edad": "ENT", "Telefono": "ENT"}),
                                          [["Carolina", 45, 3140891429], ["Santiago", 39, 5321350894], ["Ryan", 54, 98764297613]])


def insert_table(tbl_name: str, fields):
    global num_tables
    errors_detected = []
    succesful_insertion = False

    if tbl_name in _table_registry:
        errors_detected.append(f"Ya existe una tabla con el nombre \"{table_name}\"")
    else:
        _table_registry[tbl_name] = DBTable(fields)
        num_tables += 1
        succesful_insertion = True

    return [succesful_insertion, errors_detected]

def delete_table(table_name: str):
    global num_tables
    if table_name in _table_registry:
        del _table_registry[table_name]
        num_tables -= 1
        return [True, "Tabla exitosamente eliminada"]
    return [False, f"No se puede eliminar la tabla \"{table_name}\" porque no existe"]

