from sys import stdin
from sys import stdout

def print_help():

    continue_help = True

    while continue_help:
        print("Comandos de ayuda:")
        print(" crear - insertar - consultar - eliminar")
        stdout.write("> ")
        stdout.flush()
        input_console = stdin.readline().strip()
        if input_console == "crear":
            print("Para crear tabla:")
            print(" CREAR TABLA <NOMBRE_TABLA> CON {<ATR1> <TIPO1>, <ATR2> <TIPO2>, ... ,<ATR_N> <TIPO_N>}")
            print("Estos son los tipos de dato:")
            print(" CADENA DE TEXTO: CAD")
            print(" ENTERO:          ENT")
            print(" BOOLEANO:        BOOL")
            print(" DECIMAL:         DEC\n")
        elif input_console == "insertar":
            print("Para insertar:")
            print("INSERTAR EN <NOMBRE_TABLA> {VALOR1, VALOR2, ... , VALOR N\n")
        elif input_console == "consultar":
            print("Para consultar:")
            print("CONSULTAR <NOMBRE_TABLA> (DONDE <ATR_N> (==|!=) VALOR)?\n")
        elif input_console == "eliminar":
            print("Para eliminar tabla:")
            print(" ELIMINAR TABLA <NOMBRE_TABLA>\n")
        else:
            print("Comando no válido")

        print("¿Deseas continuar en la guía? s-n")
        valid_answer = False
        while not valid_answer:
            stdout.write("> ")
            stdout.flush()
            input_console = stdin.readline().strip()
            if input_console == "s":
                valid_answer = True
            elif input_console == "n":
                valid_answer = True
                continue_help = False
                print("Saliendo de la ayuda\n")
                print("Introduce un comando:")
            else:
                print("Respuesta no válida\n")
