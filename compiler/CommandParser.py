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
        4,1,20,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,17,8,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,1,2,
        1,2,1,2,1,2,3,2,32,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,42,8,
        3,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,4,1,4,1,4,1,4,1,4,3,
        4,57,8,4,1,4,1,4,3,4,61,8,4,3,4,63,8,4,1,4,0,1,6,5,0,2,4,6,8,0,1,
        1,0,12,13,71,0,16,1,0,0,0,2,24,1,0,0,0,4,31,1,0,0,0,6,41,1,0,0,0,
        8,62,1,0,0,0,10,17,3,2,1,0,11,17,3,6,3,0,12,13,5,1,0,0,13,14,3,0,
        0,0,14,15,5,2,0,0,15,17,1,0,0,0,16,10,1,0,0,0,16,11,1,0,0,0,16,12,
        1,0,0,0,17,1,1,0,0,0,18,19,5,3,0,0,19,20,5,11,0,0,20,21,5,4,0,0,
        21,25,3,4,2,0,22,23,5,5,0,0,23,25,5,11,0,0,24,18,1,0,0,0,24,22,1,
        0,0,0,25,3,1,0,0,0,26,27,5,11,0,0,27,28,5,9,0,0,28,32,3,4,2,0,29,
        30,5,11,0,0,30,32,5,9,0,0,31,26,1,0,0,0,31,29,1,0,0,0,32,5,1,0,0,
        0,33,34,6,3,-1,0,34,35,5,1,0,0,35,36,3,6,3,0,36,37,5,2,0,0,37,42,
        1,0,0,0,38,39,5,11,0,0,39,40,7,0,0,0,40,42,3,8,4,0,41,33,1,0,0,0,
        41,38,1,0,0,0,42,48,1,0,0,0,43,44,10,2,0,0,44,45,5,10,0,0,45,47,
        3,6,3,3,46,43,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,
        49,7,1,0,0,0,50,48,1,0,0,0,51,63,5,14,0,0,52,63,5,20,0,0,53,63,5,
        15,0,0,54,63,5,16,0,0,55,57,5,6,0,0,56,55,1,0,0,0,56,57,1,0,0,0,
        57,58,1,0,0,0,58,60,5,17,0,0,59,61,5,18,0,0,60,59,1,0,0,0,60,61,
        1,0,0,0,61,63,1,0,0,0,62,51,1,0,0,0,62,52,1,0,0,0,62,53,1,0,0,0,
        62,54,1,0,0,0,62,56,1,0,0,0,63,9,1,0,0,0,8,16,24,31,41,48,56,60,
        62
    ]

class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'create table'", "'with'", 
                     "'delete table'", "'-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'eq'", "'ne'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TABLE_CMD", 
                      "TABLE_ACTION", "TYPE", "LOGICAL_OPERATOR", "ATTRNAME", 
                      "EQ", "NE", "BOOLEAN", "STRING", "DOUBLE", "INT", 
                      "EXP", "WS", "NULL" ]

    RULE_command = 0
    RULE_table_management = 1
    RULE_attributes = 2
    RULE_query = 3
    RULE_value = 4

    ruleNames =  [ "command", "table_management", "attributes", "query", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TABLE_CMD=7
    TABLE_ACTION=8
    TYPE=9
    LOGICAL_OPERATOR=10
    ATTRNAME=11
    EQ=12
    NE=13
    BOOLEAN=14
    STRING=15
    DOUBLE=16
    INT=17
    EXP=18
    WS=19
    NULL=20

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


        def command(self):
            return self.getTypedRuleContext(CommandParser.CommandContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.table_management()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.query(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(CommandParser.T__0)
                self.state = 13
                self.command()
                self.state = 14
                self.match(CommandParser.T__1)
                pass


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

        def ATTRNAME(self):
            return self.getToken(CommandParser.ATTRNAME, 0)
        def attributes(self):
            return self.getTypedRuleContext(CommandParser.AttributesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateTable" ):
                listener.enterCreateTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateTable" ):
                listener.exitCreateTable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateTable" ):
                return visitor.visitCreateTable(self)
            else:
                return visitor.visitChildren(self)


    class DeleteTAbleContext(Table_managementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.Table_managementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ATTRNAME(self):
            return self.getToken(CommandParser.ATTRNAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteTAble" ):
                listener.enterDeleteTAble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteTAble" ):
                listener.exitDeleteTAble(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteTAble" ):
                return visitor.visitDeleteTAble(self)
            else:
                return visitor.visitChildren(self)



    def table_management(self):

        localctx = CommandParser.Table_managementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_table_management)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = CommandParser.CreateTableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(CommandParser.T__2)
                self.state = 19
                self.match(CommandParser.ATTRNAME)
                self.state = 20
                self.match(CommandParser.T__3)
                self.state = 21
                self.attributes()
                pass
            elif token in [5]:
                localctx = CommandParser.DeleteTAbleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(CommandParser.T__4)
                self.state = 23
                self.match(CommandParser.ATTRNAME)
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


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTRNAME(self):
            return self.getToken(CommandParser.ATTRNAME, 0)

        def TYPE(self):
            return self.getToken(CommandParser.TYPE, 0)

        def attributes(self):
            return self.getTypedRuleContext(CommandParser.AttributesContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = CommandParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attributes)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(CommandParser.ATTRNAME)
                self.state = 27
                self.match(CommandParser.TYPE)
                self.state = 28
                self.attributes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(CommandParser.ATTRNAME)
                self.state = 30
                self.match(CommandParser.TYPE)
                pass


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


    class CompareExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.QueryContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ATTRNAME(self):
            return self.getToken(CommandParser.ATTRNAME, 0)
        def value(self):
            return self.getTypedRuleContext(CommandParser.ValueContext,0)

        def EQ(self):
            return self.getToken(CommandParser.EQ, 0)
        def NE(self):
            return self.getToken(CommandParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExp" ):
                listener.enterCompareExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExp" ):
                listener.exitCompareExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExp" ):
                return visitor.visitCompareExp(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query(self):
            return self.getTypedRuleContext(CommandParser.QueryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExp" ):
                listener.enterParenExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExp" ):
                listener.exitParenExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExp" ):
                return visitor.visitParenExp(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.QueryContext
            super().__init__(parser)
            self.left = None # QueryContext
            self.right = None # QueryContext
            self.copyFrom(ctx)

        def LOGICAL_OPERATOR(self):
            return self.getToken(CommandParser.LOGICAL_OPERATOR, 0)
        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.QueryContext)
            else:
                return self.getTypedRuleContext(CommandParser.QueryContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExp" ):
                listener.enterLogicalExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExp" ):
                listener.exitLogicalExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExp" ):
                return visitor.visitLogicalExp(self)
            else:
                return visitor.visitChildren(self)



    def query(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandParser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_query, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CommandParser.ParenExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 34
                self.match(CommandParser.T__0)
                self.state = 35
                self.query(0)
                self.state = 36
                self.match(CommandParser.T__1)
                pass
            elif token in [11]:
                localctx = CommandParser.CompareExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(CommandParser.ATTRNAME)
                self.state = 39
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CommandParser.LogicalExpContext(self, CommandParser.QueryContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 43
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 44
                    self.match(CommandParser.LOGICAL_OPERATOR)
                    self.state = 45
                    localctx.right = self.query(3) 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull" ):
                listener.enterNull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull" ):
                listener.exitNull(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLong" ):
                listener.enterLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLong" ):
                listener.exitLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLong" ):
                return visitor.visitLong(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CommandParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = CommandParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(CommandParser.BOOLEAN)
                pass
            elif token in [20]:
                localctx = CommandParser.NullContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(CommandParser.NULL)
                pass
            elif token in [15]:
                localctx = CommandParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(CommandParser.STRING)
                pass
            elif token in [16]:
                localctx = CommandParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.match(CommandParser.DOUBLE)
                pass
            elif token in [6, 17]:
                localctx = CommandParser.LongContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 55
                    self.match(CommandParser.T__5)


                self.state = 58
                self.match(CommandParser.INT)
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 59
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.query_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




