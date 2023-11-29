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


    # Visit a parse tree produced by CommandParser#deleteTable.
    def visitDeleteTable(self, ctx:CommandParser.DeleteTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#insertRegister.
    def visitInsertRegister(self, ctx:CommandParser.InsertRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#attrDeclaration.
    def visitAttrDeclaration(self, ctx:CommandParser.AttrDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#logicalQuery.
    def visitLogicalQuery(self, ctx:CommandParser.LogicalQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#parenQuery.
    def visitParenQuery(self, ctx:CommandParser.ParenQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#compareQuery.
    def visitCompareQuery(self, ctx:CommandParser.CompareQueryContext):
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