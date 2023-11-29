"""
DBMS. Un pequeño proyecto con antlr, basado en la idea de Ab Rhmn. Idea original disponible en
https://medium.com/@ab.rhmn97/build-an-api-query-language-with-antlr-in-python-7313dba222e7

César Lemos
David Alarcón

Compiladores
Prof. Arles Rodriguez
Semestre 2023-II
Proyecto Final

El proyecto consiste en un pequeño DBMS que se puede manejar por medio de comandos introducidos en la línea de comandos.
Se usa antlr para implementar el lexer y el parser.
"""

from antlr4 import *
from compiler.CommandLexer import CommandLexer
from compiler.CommandParser import CommandParser
from data_validation import MyVisitor

from sys import stdin
from sys import stdout

import db_management

from help_module import print_help


def process_command(command: str):
    command = InputStream(command)

    # lexer
    lexer = CommandLexer(command)
    stream = CommonTokenStream(lexer)

    # parser
    parser = CommandParser(stream)
    tree = parser.command()

    visitor = MyVisitor()
    visitor.visit(tree)

    if len(visitor.errors_detected) == 1:
        print("Error:", visitor.errors_detected[0])
    elif len(visitor.errors_detected) > 1:
        print("Errores: ")
        for error in visitor.errors_detected:
            print("   ", error)


def main():
    print("\nBienvenido a la base de datos")
    print("Introduce el comando \"ayuda\" para más información sobre los comandos")
    print("Presiona \"q\" para salir\n")

    while True:
        stdout.write("> ")
        stdout.flush()
        input_console = stdin.readline().strip()

        if input_console == "q":
            print("¡Vuelve pronto!")
            break
        elif input_console == "ayuda":
            print_help()
            continue

        # Se hace el proceso de análisis léxico, sintáctico, y de validación de la información
        process_command(input_console)
        print(db_management._table_registry)


if __name__ == "__main__":
    main()
