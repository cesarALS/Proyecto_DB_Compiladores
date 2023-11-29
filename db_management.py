"""
Este código maneja la base de datos. Aquí se guardan las tablas de la base de datos, y se proveen las funciones
necesarias para ejecutar los comandos del usuario.
"""

from collections import OrderedDict
from sys import stdout


OPERATION_DONE = 0
ERRORS = 1

num_tables = 1



class DBTable:
    def __init__(self, fields: OrderedDict, initial_registers=None):
        self.fields = fields
        self.registers = initial_registers if initial_registers is not None else []
        self.max_sizes = []  # Máximo tamaño de dato que hay en cada campo
        for field in fields:
            self.max_sizes.append(len(field))


    def insert_register(self, data: list):
        detected_errors = []
        successful_insertion = False

        for (key, value) in enumerate(self.fields.items()):
            if len(data) < key+1:
                detected_errors.append(f"Insuficientes datos. Se requieren {len(self.fields)}, pero se dieron {len(data)}.")
                break

            d = data[key]  # Dato ingresado por el usuario
            field = value[0]  # Campo
            v = value[1]  # Tipo de dato esperado para el campo dado

            if d is not None:
                if v == 'CAD' and type(d) is not str:
                    detected_errors.append(f"El valor dado de {field} no es una cadena de texto ({d})")
                elif v == 'BOOL' and type(d) is not bool:
                    detected_errors.append(f"El valor dado de {field} no es un booleano ({d})")
                elif v == 'ENT' and type(d) is not int:
                    detected_errors.append(f"El valor dado de {field} no es un entero ({d})")
                elif v == 'DEC' and type(d) is not float:
                    detected_errors.append(f"El valor dado de {field} no es un decimal ({d})")

        if len(detected_errors) == 0:

            # Actualizar tamaño máximo:
            i = 0
            for d in data:
                # if (type(d) is not bool or d is not None) and len(str(d)) > self.max_sizes[d]:
                if type(d) is not bool or d is not None:
                    size = len(str(d)) if (type(d) is int or type(d) is float) else len(d)
                    if size > self.max_sizes[i]:
                        self.max_sizes[i] = size
                i += 1

            # Insertar el registro
            self.registers.append(data)
            successful_insertion = True

        return [successful_insertion, detected_errors]

    def _print_line(self, reg: list or OrderedDict):
        i = 0
        for entry in reg:
            needed_space = 2
            evaluation_size = len(entry) if type(entry) is str else len(str(entry))
            if evaluation_size < self.max_sizes[i]:
                needed_space += (self.max_sizes[i] - evaluation_size)
            stdout.write(f"{entry}{' '*needed_space}")
            i += 1
        stdout.write('\n')
        stdout.flush()

    def query_table(self, table_name=None, condition=None):
        errors_detected = []
        successful_query = False

        if table_name is not None:
            print(f"TABLA {table_name}:")
        if condition is None:
            self._print_line(self.fields)

            print("------------------------------")
            for register in self.registers:
                self._print_line(register)
            successful_query = True

        else:
            field = condition[0]
            op = condition[1]
            constant = condition[2]

            field_position = 0
            if field not in self.fields:
                errors_detected.append(f"El campo \"{field}\" no es parte de la tabla")
            else:
                for (key, value) in enumerate(self.fields.items()):
                    if value[0] == field:
                        field_position = key

                self._print_line(self.fields)

                for register in self.registers:
                    data_to_evaluate = register[field_position]
                    cond = (data_to_evaluate == constant) if (op == "==") else (data_to_evaluate != constant)
                    if cond is True:
                        self._print_line(register)

                successful_query = True


        return[successful_query, errors_detected]


# Registro de las bases de datos en existencia
_table_registry = OrderedDict()


def init_db():
    insert_table("Ej_telefonos", OrderedDict({"Nombre": "CAD", "Edad": "ENT", "Telefono": "ENT"}))
    insert_new_register("Ej_telefonos", ["Carolina", 45, 3140891429])
    insert_new_register("Ej_telefonos", ["Santiago", 39, 5321350894])
    insert_new_register("Ej_telefonos", ["Ryan", 54, 9876429761])
    insert_new_register("Ej_telefonos", ["Camilo", 31, 7951564342])
    insert_new_register("Ej_telefonos", ["María", 28, 4214653285])

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
    return [False, [f"No se puede eliminar la tabla \"{table_name}\" porque no existe"]]


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

def query_table(table_name: str, condition=None):
    errors_detected = []
    successful_insertion = False

    if table_name in _table_registry:
        res = _table_registry[table_name].query_table(table_name, condition)
        successful_insertion = res[OPERATION_DONE]
        errors_detected = res[ERRORS]
    else:
        errors_detected.append(f"La tabla {table_name} no se puede consultar porque no existe")

    return [successful_insertion, errors_detected]

