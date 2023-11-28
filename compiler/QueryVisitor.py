# Generated from Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryParser#compareExp.
    def visitCompareExp(self, ctx:QueryParser.CompareExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#parenExp.
    def visitParenExp(self, ctx:QueryParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#logicalExp.
    def visitLogicalExp(self, ctx:QueryParser.LogicalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#boolean.
    def visitBoolean(self, ctx:QueryParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#null.
    def visitNull(self, ctx:QueryParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#string.
    def visitString(self, ctx:QueryParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#double.
    def visitDouble(self, ctx:QueryParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#long.
    def visitLong(self, ctx:QueryParser.LongContext):
        return self.visitChildren(ctx)



del QueryParser