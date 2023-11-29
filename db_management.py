from collections import OrderedDict
from sys import stdout

"""
Este código maneja la base de datos. Aquí se guardan las tablas de la base de datos, y se proveen las funciones
necesarias para manejarlas.
"""

OPERATION_DONE = 0
ERRORS = 1

num_tables = 1

class DBTable:
    def __init__(self, fields: OrderedDict, initial_registers=None):
        self.fields = fields
        self.registers = initial_registers if initial_registers is not None else []

    def insert_register(self, data: list):
        detected_errors = []
        successful_insertion = False

        i = 0
        for (key, value) in enumerate(self.fields.items()):
            if len(data) < i+1:
                detected_errors.append(f"Insuficientes datos. Se requieren {len(self.fields)}, pero se dieron {len(data)}.")
                break
            d = data[i]
            v = value[1]
            field = value[0]
            if v == 'CAD' and type(d) is not str:
                detected_errors.append(f"El valor dado de {field} no es una cadena de texto ({d})")
            elif v == 'BOOL' and type(d) is not bool:
                detected_errors.append(f"El valor dado de {field} no es un booleano ({d})")
            elif v == 'ENT' and type(d) is not int:
                detected_errors.append(f"El valor dado de {field} no es un entero ({d})")
            elif v == 'DEC' and type(d) is not float:
                detected_errors.append(f"El valor dado de {field} no es un decimal ({d})")
            i += 1

        if len(detected_errors) == 0:
            self.registers.append(data)
            successful_insertion = True

        return [successful_insertion, detected_errors]


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


def init_db():
    _table_registry["ej_telefonos"] = DBTable(OrderedDict({"Nombre": "CAD", "Edad": "ENT", "Telefono": "ENT"}),
                                              [["Carolina", 45, 3140891429], ["Santiago", 39, 5321350894],
                                               ["Ryan", 54, 98764297613]])

def insert_table(tbl_name: str, fields):
    global num_tables
    errors_detected = []
    successful_insertion = False

    if tbl_name in _table_registry:
        errors_detected.append(f"Ya existe una tabla con el nombre \"{table_name}\"")
    else:
        _table_registry[tbl_name] = DBTable(fields)
        num_tables += 1
        successful_insertion = True

    return [successful_insertion, errors_detected]

def delete_table(table_name: str):
    global num_tables
    if table_name in _table_registry:
        del _table_registry[table_name]
        num_tables -= 1
        return [True, None]
    return [False, f"No se puede eliminar la tabla \"{table_name}\" porque no existe"]


def insert_new_register(table_name: str, values: list):
    errors_detected = []
    successful_insertion = False

    if table_name in _table_registry:
        insert_into_table = _table_registry[table_name].insert_register(values)
        successful_insertion = insert_into_table[OPERATION_DONE]
        errors_detected = insert_into_table[ERRORS]
    else:
        errors_detected.append(f"La tabla {table_name} no existe")

    return [successful_insertion, errors_detected]
