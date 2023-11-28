# Generated from Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete listener for a parse tree produced by QueryParser.
class QueryListener(ParseTreeListener):

    # Enter a parse tree produced by QueryParser#compareExp.
    def enterCompareExp(self, ctx:QueryParser.CompareExpContext):
        pass

    # Exit a parse tree produced by QueryParser#compareExp.
    def exitCompareExp(self, ctx:QueryParser.CompareExpContext):
        pass


    # Enter a parse tree produced by QueryParser#parenExp.
    def enterParenExp(self, ctx:QueryParser.ParenExpContext):
        pass

    # Exit a parse tree produced by QueryParser#parenExp.
    def exitParenExp(self, ctx:QueryParser.ParenExpContext):
        pass


    # Enter a parse tree produced by QueryParser#logicalExp.
    def enterLogicalExp(self, ctx:QueryParser.LogicalExpContext):
        pass

    # Exit a parse tree produced by QueryParser#logicalExp.
    def exitLogicalExp(self, ctx:QueryParser.LogicalExpContext):
        pass


    # Enter a parse tree produced by QueryParser#boolean.
    def enterBoolean(self, ctx:QueryParser.BooleanContext):
        pass

    # Exit a parse tree produced by QueryParser#boolean.
    def exitBoolean(self, ctx:QueryParser.BooleanContext):
        pass


    # Enter a parse tree produced by QueryParser#null.
    def enterNull(self, ctx:QueryParser.NullContext):
        pass

    # Exit a parse tree produced by QueryParser#null.
    def exitNull(self, ctx:QueryParser.NullContext):
        pass


    # Enter a parse tree produced by QueryParser#string.
    def enterString(self, ctx:QueryParser.StringContext):
        pass

    # Exit a parse tree produced by QueryParser#string.
    def exitString(self, ctx:QueryParser.StringContext):
        pass


    # Enter a parse tree produced by QueryParser#double.
    def enterDouble(self, ctx:QueryParser.DoubleContext):
        pass

    # Exit a parse tree produced by QueryParser#double.
    def exitDouble(self, ctx:QueryParser.DoubleContext):
        pass


    # Enter a parse tree produced by QueryParser#long.
    def enterLong(self, ctx:QueryParser.LongContext):
        pass

    # Exit a parse tree produced by QueryParser#long.
    def exitLong(self, ctx:QueryParser.LongContext):
        pass



del QueryParser