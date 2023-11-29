# Generated from Command.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,3,0,15,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,
        2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,3,1,3,1,3,1,3,3,3,55,8,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,5,1,5,3,5,71,
        8,5,1,5,1,5,3,5,75,8,5,3,5,77,8,5,1,5,0,0,6,0,2,4,6,8,10,0,0,85,
        0,14,1,0,0,0,2,38,1,0,0,0,4,40,1,0,0,0,6,50,1,0,0,0,8,63,1,0,0,0,
        10,76,1,0,0,0,12,15,3,2,1,0,13,15,3,6,3,0,14,12,1,0,0,0,14,13,1,
        0,0,0,15,1,1,0,0,0,16,17,5,1,0,0,17,18,5,17,0,0,18,19,5,2,0,0,19,
        20,5,3,0,0,20,21,3,4,2,0,21,22,5,4,0,0,22,39,1,0,0,0,23,24,5,5,0,
        0,24,39,5,17,0,0,25,26,5,6,0,0,26,27,5,17,0,0,27,28,5,3,0,0,28,33,
        3,10,5,0,29,30,5,7,0,0,30,32,3,10,5,0,31,29,1,0,0,0,32,35,1,0,0,
        0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,
        5,4,0,0,37,39,1,0,0,0,38,16,1,0,0,0,38,23,1,0,0,0,38,25,1,0,0,0,
        39,3,1,0,0,0,40,41,5,17,0,0,41,47,5,13,0,0,42,43,5,7,0,0,43,44,5,
        17,0,0,44,46,5,13,0,0,45,42,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,
        47,48,1,0,0,0,48,5,1,0,0,0,49,47,1,0,0,0,50,51,5,8,0,0,51,54,5,17,
        0,0,52,53,5,9,0,0,53,55,3,8,4,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,
        1,0,0,0,56,57,5,10,0,0,57,58,3,8,4,0,58,59,5,11,0,0,59,64,1,0,0,
        0,60,61,5,17,0,0,61,62,5,14,0,0,62,64,3,10,5,0,63,56,1,0,0,0,63,
        60,1,0,0,0,64,9,1,0,0,0,65,77,5,15,0,0,66,77,5,16,0,0,67,77,5,18,
        0,0,68,77,5,19,0,0,69,71,5,12,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,
        72,1,0,0,0,72,74,5,20,0,0,73,75,5,21,0,0,74,73,1,0,0,0,74,75,1,0,
        0,0,75,77,1,0,0,0,76,65,1,0,0,0,76,66,1,0,0,0,76,67,1,0,0,0,76,68,
        1,0,0,0,76,70,1,0,0,0,77,11,1,0,0,0,9,14,33,38,47,54,63,70,74,76
    ]

class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREAR TABLA'", "'CON'", "'{'", "'}'", 
                     "'ELIMINAR TABLA'", "'INSERTAR EN'", "','", "'CONSULTAR'", 
                     "'DONDE'", "'('", "')'", "'-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'NULO'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE", "COMPARISON_OPERATOR", "BOOLEAN", 
                      "NULL", "OBJNAME", "STRING", "DOUBLE", "INT", "EXP", 
                      "WS" ]

    RULE_command = 0
    RULE_table_management = 1
    RULE_tbl_attributes = 2
    RULE_query = 3
    RULE_atomic_query = 4
    RULE_value = 5

    ruleNames =  [ "command", "table_management", "tbl_attributes", "query", 
                   "atomic_query", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    TYPE=13
    COMPARISON_OPERATOR=14
    BOOLEAN=15
    NULL=16
    OBJNAME=17
    STRING=18
    DOUBLE=19
    INT=20
    EXP=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_management(self):
            return self.getTypedRuleContext(CommandParser.Table_managementContext,0)


        def query(self):
            return self.getTypedRuleContext(CommandParser.QueryContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.table_management()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.query()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_managementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_table_management

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CreateTableContext(Table_managementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Table_managementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJNAME(self):
            return self.getToken(CommandParser.OBJNAME, 0)
        def tbl_attributes(self):
            return self.getTypedRuleContext(CommandParser.Tbl_attributesContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateTable" ):
                return visitor.visitCreateTable(self)
            else:
                return visitor.visitChildren(self)


    class InsertRegisterContext(Table_managementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Table_managementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJNAME(self):
            return self.getToken(CommandParser.OBJNAME, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.ValueContext)
            else:
                return self.getTypedRuleContext(CommandParser.ValueContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertRegister" ):
                return visitor.visitInsertRegister(self)
            else:
                return visitor.visitChildren(self)


    class DeleteTableContext(Table_managementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Table_managementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJNAME(self):
            return self.getToken(CommandParser.OBJNAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteTable" ):
                return visitor.visitDeleteTable(self)
            else:
                return visitor.visitChildren(self)



    def table_management(self):

        localctx = CommandParser.Table_managementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_table_management)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CommandParser.CreateTableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(CommandParser.T__0)
                self.state = 17
                self.match(CommandParser.OBJNAME)
                self.state = 18
                self.match(CommandParser.T__1)
                self.state = 19
                self.match(CommandParser.T__2)
                self.state = 20
                self.tbl_attributes()
                self.state = 21
                self.match(CommandParser.T__3)
                pass
            elif token in [5]:
                localctx = CommandParser.DeleteTableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(CommandParser.T__4)
                self.state = 24
                self.match(CommandParser.OBJNAME)
                pass
            elif token in [6]:
                localctx = CommandParser.InsertRegisterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(CommandParser.T__5)
                self.state = 26
                self.match(CommandParser.OBJNAME)
                self.state = 27
                self.match(CommandParser.T__2)
                self.state = 28
                self.value()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 29
                    self.match(CommandParser.T__6)
                    self.state = 30
                    self.value()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(CommandParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tbl_attributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_tbl_attributes

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttrDeclarationContext(Tbl_attributesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Tbl_attributesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.OBJNAME)
            else:
                return self.getToken(CommandParser.OBJNAME, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.TYPE)
            else:
                return self.getToken(CommandParser.TYPE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrDeclaration" ):
                return visitor.visitAttrDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def tbl_attributes(self):

        localctx = CommandParser.Tbl_attributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tbl_attributes)
        self._la = 0 # Token type
        try:
            localctx = CommandParser.AttrDeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CommandParser.OBJNAME)
            self.state = 41
            self.match(CommandParser.TYPE)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 42
                self.match(CommandParser.T__6)
                self.state = 43
                self.match(CommandParser.OBJNAME)
                self.state = 44
                self.match(CommandParser.TYPE)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicalQueryContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.QueryContext
            super().__init__(parser)
            self.left = None # Atomic_queryContext
            self.copyFrom(ctx)

        def OBJNAME(self):
            return self.getToken(CommandParser.OBJNAME, 0)
        def atomic_query(self):
            return self.getTypedRuleContext(CommandParser.Atomic_queryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalQuery" ):
                return visitor.visitLogicalQuery(self)
            else:
                return visitor.visitChildren(self)



    def query(self):

        localctx = CommandParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_query)
        self._la = 0 # Token type
        try:
            localctx = CommandParser.LogicalQueryContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(CommandParser.T__7)
            self.state = 51
            self.match(CommandParser.OBJNAME)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 52
                self.match(CommandParser.T__8)
                self.state = 53
                localctx.left = self.atomic_query()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_atomic_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenQueryContext(Atomic_queryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Atomic_queryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_query(self):
            return self.getTypedRuleContext(CommandParser.Atomic_queryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenQuery" ):
                return visitor.visitParenQuery(self)
            else:
                return visitor.visitChildren(self)


    class CompareQueryContext(Atomic_queryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Atomic_queryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJNAME(self):
            return self.getToken(CommandParser.OBJNAME, 0)
        def COMPARISON_OPERATOR(self):
            return self.getToken(CommandParser.COMPARISON_OPERATOR, 0)
        def value(self):
            return self.getTypedRuleContext(CommandParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareQuery" ):
                return visitor.visitCompareQuery(self)
            else:
                return visitor.visitChildren(self)



    def atomic_query(self):

        localctx = CommandParser.Atomic_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atomic_query)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = CommandParser.ParenQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(CommandParser.T__9)
                self.state = 57
                self.atomic_query()
                self.state = 58
                self.match(CommandParser.T__10)
                pass
            elif token in [17]:
                localctx = CommandParser.CompareQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(CommandParser.OBJNAME)
                self.state = 61
                self.match(CommandParser.COMPARISON_OPERATOR)
                self.state = 62
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BooleanContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(CommandParser.BOOLEAN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class NullContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(CommandParser.NULL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull" ):
                return visitor.visitNull(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CommandParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class DoubleContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(CommandParser.DOUBLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble" ):
                return visitor.visitDouble(self)
            else:
                return visitor.visitChildren(self)


    class LongContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CommandParser.INT, 0)
        def EXP(self):
            return self.getToken(CommandParser.EXP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLong" ):
                return visitor.visitLong(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CommandParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = CommandParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(CommandParser.BOOLEAN)
                pass
            elif token in [16]:
                localctx = CommandParser.NullContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(CommandParser.NULL)
                pass
            elif token in [18]:
                localctx = CommandParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(CommandParser.STRING)
                pass
            elif token in [19]:
                localctx = CommandParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.match(CommandParser.DOUBLE)
                pass
            elif token in [12, 20]:
                localctx = CommandParser.LongContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 69
                    self.match(CommandParser.T__11)


                self.state = 72
                self.match(CommandParser.INT)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 73
                    self.match(CommandParser.EXP)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





