"""
Este código implementa la clase MyVisitor, la cual contiene cada una de las funciones que se ejecutan cuando
se recorre el árbol sintáctico producido por el parser.
La clase MyVisitor hereda de la clase CommandVisitor, que antlr crea automáticamente.
Esas funciones verifican de la validez de la información ingresada por el usuario, y llaman
las funciones necesarias en db_management para ejecutar los comandos introducidos.
"""

from collections import OrderedDict

from compiler.CommandVisitor import CommandVisitor
from compiler.CommandParser import CommandParser

import db_management

OPERATION_DONE = db_management.OPERATION_DONE
ERRORS = db_management.ERRORS

class MyVisitor(CommandVisitor):
    def __init__(self):
        super(MyVisitor, self).__init__()
        self.errors_detected = []

    def visitString(self, ctx):
        st = str(ctx.getText())
        return st[1:-1]

    def visitDouble(self, ctx):
        return float(ctx.getText())

    def visitLong(self, ctx):
        return int(ctx.getText())

    def visitBoolean(self, ctx):
        return bool(ctx.getText())

    def visitNull(self, ctx):
        return [None]

    def visitCreateTable(self, ctx: CommandParser.CreateTableContext):

        ATTRIBUTES_POSITION = 4
        table_name = str(ctx.OBJNAME())
        ch = self.visitAttrDeclaration(ctx.getChild(ATTRIBUTES_POSITION)) # Explorar los hijos

        if ch is not None:
            res = db_management.insert_table(table_name, ch)  # Inserción en la base de datos
            if not res[OPERATION_DONE]:
                for error in res[ERRORS]: self.errors_detected.append(error)
            else:
                print(f"Tabla {table_name} creada")

        return None

    def visitAttrDeclaration(self, ctx: CommandParser.AttrDeclarationContext):

        # Se va a comprobar si hay o no campos duplicados. En caso de no haberlos, se crea un diccionario
        # que se introduce luego en la base de datos

        pairs = OrderedDict()
        duplicated_attrs = set([])

        i = 0
        attr, typ = ctx.OBJNAME(i), ctx.TYPE(i)
        while attr is not None:
            attr, typ = str(attr), str(typ)

            if attr in pairs:
                duplicated_attrs.append(attr)

            pairs[attr] = typ

            i = i+1
            attr, typ = ctx.OBJNAME(i), ctx.TYPE(i)

        if len(duplicated_attrs) > 0:

            for attr in duplicated_attrs:
                self.errors_detected.append(f"Campo \"{attr}\" usado más de una vez")
            return None

        return pairs

    def visitDeleteTable(self, ctx: CommandParser.DeleteTableContext):
        tbl_name = str(ctx.OBJNAME())
        res = db_management.delete_table(tbl_name)
        if res[OPERATION_DONE]:
            print("Tabla eliminada")
        else:
            for error in res[ERRORS]:
                self.errors_detected.append(error)

        return None

    # Insertar un registro en una tabla de la base de datos
    def visitInsertRegister(self, ctx: CommandParser.InsertRegisterContext):

        values = []
        i = 0
        child = ctx.getChild(i)

        while child is not None:
            value = self.visit(child)
            if value is not None:  # Solo los nodos tipo "value" devuelven valores no nulos
                if value == [None]:
                    values.append(None)
                else:
                    values.append(value)
            i += 1
            child = ctx.getChild(i)

        tbl_name = str(ctx.OBJNAME())

        if not len(self.errors_detected) > 0:
            res = db_management.insert_new_register(tbl_name, values)
            if not res[OPERATION_DONE]:
                for error in res[ERRORS]:
                    self.errors_detected.append(error)
            else:
                print("Inserción exitosa")

        return values

    def visitLogicalQuery(self, ctx: CommandParser.LogicalQueryContext):
        tbl_name = str(ctx.OBJNAME())
        if ctx.getChild(3) is not None:
            compare_query = self.visit(ctx.getChild(3))
        else:
            compare_query = None

        res = db_management.query_table(tbl_name, compare_query)
        if not res[OPERATION_DONE]:
            for error in res[ERRORS]:
                self.errors_detected.append(error)

        return None

    def visitParenQuery(self, ctx: CommandParser.ParenQueryContext):
        REAL_QUERY_POSITION = 1
        return self.visitCompareQuery(ctx.getChild(REAL_QUERY_POSITION))

    def visitCompareQuery(self, ctx: CommandParser.CompareQueryContext):
        field = str(ctx.OBJNAME())
        op = str(ctx.COMPARISON_OPERATOR())
        val = self.visit(ctx.value())
        if val == [None]:
            val = None
        return [field, op, val]






