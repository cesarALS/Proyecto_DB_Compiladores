from antlr4 import *
from compiler.CommandLexer import CommandLexer
from compiler.CommandParser import CommandParser
from data_validation import MyVisitor

import db_management

def process_query(command: str):
    command = InputStream(command)

    # lexer
    lexer = CommandLexer(command)
    stream = CommonTokenStream(lexer)

    # parser
    parser = CommandParser(stream)
    tree = parser.command()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    return visitor.res

def main():
    print("Bienvenido a la base de datos")
    print("Introduce un comando: \n")

    while True:
        input_console = input()

        if input_console == "exit":
            print("Vuelve pronto")
            break

        query_object = process_query(input_console)
        print(query_object)


if __name__ == "__main__":
    main()



