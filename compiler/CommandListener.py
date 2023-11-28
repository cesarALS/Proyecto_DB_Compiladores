# Generated from Command.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx:CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx:CommandParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandParser#createTable.
    def enterCreateTable(self, ctx:CommandParser.CreateTableContext):
        pass

    # Exit a parse tree produced by CommandParser#createTable.
    def exitCreateTable(self, ctx:CommandParser.CreateTableContext):
        pass


    # Enter a parse tree produced by CommandParser#deleteTAble.
    def enterDeleteTAble(self, ctx:CommandParser.DeleteTAbleContext):
        pass

    # Exit a parse tree produced by CommandParser#deleteTAble.
    def exitDeleteTAble(self, ctx:CommandParser.DeleteTAbleContext):
        pass


    # Enter a parse tree produced by CommandParser#attributes.
    def enterAttributes(self, ctx:CommandParser.AttributesContext):
        pass

    # Exit a parse tree produced by CommandParser#attributes.
    def exitAttributes(self, ctx:CommandParser.AttributesContext):
        pass


    # Enter a parse tree produced by CommandParser#compareExp.
    def enterCompareExp(self, ctx:CommandParser.CompareExpContext):
        pass

    # Exit a parse tree produced by CommandParser#compareExp.
    def exitCompareExp(self, ctx:CommandParser.CompareExpContext):
        pass


    # Enter a parse tree produced by CommandParser#parenExp.
    def enterParenExp(self, ctx:CommandParser.ParenExpContext):
        pass

    # Exit a parse tree produced by CommandParser#parenExp.
    def exitParenExp(self, ctx:CommandParser.ParenExpContext):
        pass


    # Enter a parse tree produced by CommandParser#logicalExp.
    def enterLogicalExp(self, ctx:CommandParser.LogicalExpContext):
        pass

    # Exit a parse tree produced by CommandParser#logicalExp.
    def exitLogicalExp(self, ctx:CommandParser.LogicalExpContext):
        pass


    # Enter a parse tree produced by CommandParser#boolean.
    def enterBoolean(self, ctx:CommandParser.BooleanContext):
        pass

    # Exit a parse tree produced by CommandParser#boolean.
    def exitBoolean(self, ctx:CommandParser.BooleanContext):
        pass


    # Enter a parse tree produced by CommandParser#null.
    def enterNull(self, ctx:CommandParser.NullContext):
        pass

    # Exit a parse tree produced by CommandParser#null.
    def exitNull(self, ctx:CommandParser.NullContext):
        pass


    # Enter a parse tree produced by CommandParser#string.
    def enterString(self, ctx:CommandParser.StringContext):
        pass

    # Exit a parse tree produced by CommandParser#string.
    def exitString(self, ctx:CommandParser.StringContext):
        pass


    # Enter a parse tree produced by CommandParser#double.
    def enterDouble(self, ctx:CommandParser.DoubleContext):
        pass

    # Exit a parse tree produced by CommandParser#double.
    def exitDouble(self, ctx:CommandParser.DoubleContext):
        pass


    # Enter a parse tree produced by CommandParser#long.
    def enterLong(self, ctx:CommandParser.LongContext):
        pass

    # Exit a parse tree produced by CommandParser#long.
    def exitLong(self, ctx:CommandParser.LongContext):
        pass



del CommandParser