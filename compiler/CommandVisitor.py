# Generated from Command.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete generic visitor for a parse tree produced by CommandParser.

class CommandVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx:CommandParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#createTable.
    def visitCreateTable(self, ctx:CommandParser.CreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#deleteTAble.
    def visitDeleteTAble(self, ctx:CommandParser.DeleteTAbleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#attributes.
    def visitAttributes(self, ctx:CommandParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#compareExp.
    def visitCompareExp(self, ctx:CommandParser.CompareExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#parenExp.
    def visitParenExp(self, ctx:CommandParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#logicalExp.
    def visitLogicalExp(self, ctx:CommandParser.LogicalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#boolean.
    def visitBoolean(self, ctx:CommandParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#null.
    def visitNull(self, ctx:CommandParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#string.
    def visitString(self, ctx:CommandParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#double.
    def visitDouble(self, ctx:CommandParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#long.
    def visitLong(self, ctx:CommandParser.LongContext):
        return self.visitChildren(ctx)



del CommandParser