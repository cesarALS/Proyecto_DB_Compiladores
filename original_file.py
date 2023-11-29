"""
Código original del ejercicio. Disponible en:
https://medium.com/@ab.rhmn97/build-an-api-query-language-with-antlr-in-python-7313dba222e7
"""

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

from antlr4 import *
from compiler.QueryLexer import QueryLexer
from compiler.QueryParser import QueryParser
from compiler.QueryVisitor import QueryVisitor

app = Flask(__name__)
api = Api(app)
parser1 = reqparse.RequestParser()
parser1.add_argument('find', type=str, location='args')

users = [
    {"user": "arya", "age": 22, "salary": 3000},
    {"user": "john", "age": 34, "salary": 2300},
    {"user": "mike", "age": 34, "salary": 4500},
    {"user": "arya", "age": 34, "salary": 5000},
    {"user": "snow", "age": 18, "salary": 3000},
]

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
             'eq': lambda: {str(l):r[1:-1]} if type(r)==str else {str(l):r},
             'in': lambda: {str(l): r[1:-1]} if type(r) == str else {str(l): r}
        }
        self.res.update(operation.get(op, lambda: None)())

def getQuery(data):
    # lexer
    lexer = QueryLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = QueryParser(stream)
    tree = parser.query()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    return visitor.res

def findUserSalary(users, queryobject):
    print(queryobject)
    for i in users:
        if queryobject['user'] == i['user'] and queryobject['age'] == i['age']:
            return {"salary": i['salary']}
    return 'not found'


class salary(Resource):
    def get(self):
        args = parser1.parse_args()
        queryobject = getQuery(InputStream(args['find']))
        result = findUserSalary(users, queryobject)
        return result, 200


api.add_resource(salary, "/salary")

if __name__ == "__main__":
    app.run(debug=True)
