# Generated from Query.g4 by ANTLR 4.13.1
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
        4,1,14,36,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,
        3,1,28,8,1,1,1,1,1,3,1,32,8,1,3,1,34,8,1,1,1,0,1,0,2,0,2,0,1,1,0,
        6,7,41,0,12,1,0,0,0,2,33,1,0,0,0,4,5,6,0,-1,0,5,6,5,1,0,0,6,7,3,
        0,0,0,7,8,5,2,0,0,8,13,1,0,0,0,9,10,5,8,0,0,10,11,7,0,0,0,11,13,
        3,2,1,0,12,4,1,0,0,0,12,9,1,0,0,0,13,19,1,0,0,0,14,15,10,2,0,0,15,
        16,5,4,0,0,16,18,3,0,0,3,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,
        0,19,20,1,0,0,0,20,1,1,0,0,0,21,19,1,0,0,0,22,34,5,5,0,0,23,34,5,
        14,0,0,24,34,5,9,0,0,25,34,5,10,0,0,26,28,5,3,0,0,27,26,1,0,0,0,
        27,28,1,0,0,0,28,29,1,0,0,0,29,31,5,11,0,0,30,32,5,12,0,0,31,30,
        1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,22,1,0,0,0,33,23,1,0,0,0,
        33,24,1,0,0,0,33,25,1,0,0,0,33,27,1,0,0,0,34,3,1,0,0,0,5,12,19,27,
        31,33
    ]

class QueryParser ( Parser ):

    grammarFileName = "Query.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-'", "<INVALID>", "<INVALID>", 
                     "'eq'", "'ne'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LOGICAL_OPERATOR", "BOOLEAN", "EQ", "NE", "ATTRNAME", 
                      "STRING", "DOUBLE", "INT", "EXP", "WS", "NULL" ]

    RULE_query = 0
    RULE_value = 1

    ruleNames =  [ "query", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LOGICAL_OPERATOR=4
    BOOLEAN=5
    EQ=6
    NE=7
    ATTRNAME=8
    STRING=9
    DOUBLE=10
    INT=11
    EXP=12
    WS=13
    NULL=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompareExpContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.QueryContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ATTRNAME(self):
            return self.getToken(QueryParser.ATTRNAME, 0)
        def value(self):
            return self.getTypedRuleContext(QueryParser.ValueContext,0)

        def EQ(self):
            return self.getToken(QueryParser.EQ, 0)
        def NE(self):
            return self.getToken(QueryParser.NE, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query(self):
            return self.getTypedRuleContext(QueryParser.QueryContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.QueryContext
            super().__init__(parser)
            self.left = None # QueryContext
            self.right = None # QueryContext
            self.copyFrom(ctx)

        def LOGICAL_OPERATOR(self):
            return self.getToken(QueryParser.LOGICAL_OPERATOR, 0)
        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.QueryContext)
            else:
                return self.getTypedRuleContext(QueryParser.QueryContext,i)


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
        localctx = QueryParser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_query, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = QueryParser.ParenExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(QueryParser.T__0)
                self.state = 6
                self.query(0)
                self.state = 7
                self.match(QueryParser.T__1)
                pass
            elif token in [8]:
                localctx = QueryParser.CompareExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(QueryParser.ATTRNAME)
                self.state = 10
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 11
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QueryParser.LogicalExpContext(self, QueryParser.QueryContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.match(QueryParser.LOGICAL_OPERATOR)
                    self.state = 16
                    localctx.right = self.query(3) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            return QueryParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BooleanContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(QueryParser.BOOLEAN, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(QueryParser.NULL, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(QueryParser.STRING, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(QueryParser.DOUBLE, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(QueryParser.INT, 0)
        def EXP(self):
            return self.getToken(QueryParser.EXP, 0)

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

        localctx = QueryParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = QueryParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(QueryParser.BOOLEAN)
                pass
            elif token in [14]:
                localctx = QueryParser.NullContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(QueryParser.NULL)
                pass
            elif token in [9]:
                localctx = QueryParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(QueryParser.STRING)
                pass
            elif token in [10]:
                localctx = QueryParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(QueryParser.DOUBLE)
                pass
            elif token in [3, 11]:
                localctx = QueryParser.LongContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 26
                    self.match(QueryParser.T__2)


                self.state = 29
                self.match(QueryParser.INT)
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.match(QueryParser.EXP)


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
        self._predicates[0] = self.query_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




