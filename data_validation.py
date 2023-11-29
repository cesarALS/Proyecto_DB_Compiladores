"""
Este código implementa la clase MyVisitor, la cual contiene cada una de las funciones que se ejecutan cuando
se recorre el árbol sintáctico producido por el parser.
La clase MyVisitor hereda de la clase CommandVisitor, que antlr crea automáticamente.
Esas funciones verifican de la validez de la información ingresada por el usuario, y, de ser válida, llaman
a las funciones necesarias para manejar la base de datos
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
        self.res = {}
        self.errors_detected = []

    def visitParenExpr(self, ctx):
        return self.visit(ctx.query())

    def visitLogicalExp(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

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

    def visitCompareExp(self, ctx):
        l = ctx.ATTRNAME()
        r = self.visit(ctx.value())

        op = ctx.op.text

        operation = {
            'eq': lambda: {str(l): r[1:-1]} if type(r) == str else {str(l): r},
            'in': lambda: {str(l): r[1:-1]} if type(r) == str else {str(l): r}
        }
        self.res.update(operation.get(op, lambda: None)())

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
        tbl_name = ctx.OBJNAME()
        res = db_management.delete_table(tbl_name)
        if res[OPERATION_DONE]:
            print("Tabla eliminada")
        else:
            for error in res[ERRORS]:
                self.errors_detected.append(error)

        return None

    def visitInsertRegister(self, ctx: CommandParser.InsertRegisterContext):

        values = []
        i = 0
        child = ctx.getChild(i)
        while child is not None:
            value = self.visit(child)
            if value is not None:
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



