"""
Este código implementa la clase MyVisitor, la cual contiene cada una de las funciones que se ejecutan cuando
se recorre el árbol sintáctico producido por el parser.
La clase MyVistor hereda de la clase CommandVisitor, que antlr crea automáticamente.
Esas funciones verifican de la validez de la información ingresada por el usuario
"""

from collections import Counter

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

        table_name = str(ctx.OBJNAME())

        if db_management.existent_db(table_name):
            self.errors_detected.append(f"Ya existe una tabla con el nombre \"{table_name}\"")

        return self.visitChildren(ctx)

    def visitAttrDeclaration(self, ctx: CommandParser.AttrDeclarationContext):

        attr_names = []
        duplicated_attrs = []

        i = 0
        attr = ctx.OBJNAME(i)
        while attr is not None:
            attr = str(attr)
            if attr in attr_names:
                duplicated_attrs.append(attr)
            attr_names.append(attr)
            i = i+1
            attr = ctx.OBJNAME(i)

        duplicated_attrs = set(duplicated_attrs)
        for attr in duplicated_attrs:
            self.errors_detected.append(f"Campo \"{attr}\" usado más de una vez")

        return self.visitChildren(ctx)


