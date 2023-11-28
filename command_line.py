from antlr4 import *
from compiler.QueryLexer import QueryLexer
from compiler.QueryParser import QueryParser
from compiler.QueryVisitor import QueryVisitor

class MyVisitor(QueryVisitor):
    def __init__(self):
        super(MyVisitor, self).__init__()
        self.res = {}

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

def process_query(command: str):
    command = InputStream(command)

    # lexer
    lexer = QueryLexer(command)
    stream = CommonTokenStream(lexer)

    # parser
    parser = QueryParser(stream)
    tree = parser.query()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    return visitor.res

def main():
    print("Bienvenido a la base de datos")
    print("Introduce un comando: \n")

    while True:
        input_console = input()

        if input_console == "exit":
            break

        query_object = process_query(input_console)
        print(query_object)



main()



