"""
Este código implementa la clase MyVisitor, la cual contiene cada una de las funciones que se ejecutan cuando
se recorre el árbol sintáctico producido por el parser.
La clase MyVisitor hereda de la clase CommandVisitor, que antlr crea automáticamente.
Esas funciones verifican de la validez de la información ingresada por el usuario
"""

from collections import OrderedDict

from compiler.CommandVisitor import CommandVisitor
from compiler.CommandParser import CommandParser

import db_management

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
        return str(ctx.getText())

    def visitDouble(self, ctx):
        return float(ctx.getText())

    def visitLong(self, ctx):
        return int(ctx.getText())

    def visitBoolean(self, ctx):
        return bool(self, ctx.getText())

    def visitNull(self, ctx):
        return None

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
            if res[0] is False:
                for error in res[1]: self.errors_detected.append(error)

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
        if res[0]:
            print(res[1])
        else:
            self.errors_detected.append(res[1])

        return self.visitChildren(ctx)



