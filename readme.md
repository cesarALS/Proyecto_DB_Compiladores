Proyecto DB para compiladores

Basado en:
https://medium.com/@ab.rhmn97/build-an-api-query-language-with-antlr-in-python-7313dba222e7

Se debe instalar antlr4. https://github.com/antlr/antlr4/blob/master/doc/python-target.md 

El repositorio ya trae los archivos del compilador generado por antlr. Sin embargo, de ser necesario, se pueden generar esos archivos con el siguiente comando:

antlr4 -Dlanguage=Python3 Command.g4 -visitor -no-listener -o compiler

Con -visitor se especifica que se cree un visitor para recorrer los árboles sintácticos.
Con -no-listener se especifica que no se creen listeners. En este proyecto no son necesarios
los listeners para recorrer el árbol.