# Generated from Skyline.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(")\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'\13")
        buf.write("\3\3\3\2\3\4\4\2\4\2\2\2\60\2\6\3\2\2\2\4\25\3\2\2\2\6")
        buf.write("\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\b\3\1\2\n\13\7")
        buf.write("\7\2\2\13\f\5\4\3\2\f\r\7\b\2\2\r\26\3\2\2\2\16\17\7\4")
        buf.write("\2\2\17\26\5\4\3\f\20\26\7\13\2\2\21\26\7\f\2\2\22\26")
        buf.write("\7\r\2\2\23\26\7\3\2\2\24\26\7\t\2\2\25\t\3\2\2\2\25\16")
        buf.write("\3\2\2\2\25\20\3\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\24\3\2\2\2\26%\3\2\2\2\27\30\f\13\2\2\30")
        buf.write("\31\7\5\2\2\31$\5\4\3\f\32\33\f\n\2\2\33\34\7\6\2\2\34")
        buf.write("$\5\4\3\13\35\36\f\t\2\2\36\37\7\4\2\2\37$\5\4\3\n !\f")
        buf.write("\b\2\2!\"\7\n\2\2\"$\5\4\3\t#\27\3\2\2\2#\32\3\2\2\2#")
        buf.write("\35\3\2\2\2# \3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&")
        buf.write("\5\3\2\2\2\'%\3\2\2\2\5\25#%")
        return buf.getvalue()


class SkylineParser (Parser):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "'-'", "'*'", "'+'", "'('",
                    "')'", "<INVALID>", "':='"]

    symbolicNames = ["<INVALID>", "IDENTIFIER", "MINUS", "MULT", "PLUS",
                     "LPAR", "RPAR", "INTEGER", "ASSIGNMENT", "SIMPLE",
                     "LIST", "RANDOM", "WS"]

    RULE_root = 0
    RULE_expr = 1

    ruleNames = ["root", "expr"]

    EOF = Token.EOF
    IDENTIFIER = 1
    MINUS = 2
    MULT = 3
    PLUS = 4
    LPAR = 5
    RPAR = 6
    INTEGER = 7
    ASSIGNMENT = 8
    SIMPLE = 9
    LIST = 10
    RANDOM = 11
    WS = 12

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext, 0)

        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRoot"):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)

    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext, i)

        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)

        def SIMPLE(self):
            return self.getToken(SkylineParser.SIMPLE, 0)

        def LIST(self):
            return self.getToken(SkylineParser.LIST, 0)

        def RANDOM(self):
            return self.getToken(SkylineParser.RANDOM, 0)

        def IDENTIFIER(self):
            return self.getToken(SkylineParser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(SkylineParser.INTEGER, 0)

        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)

        def ASSIGNMENT(self):
            return self.getToken(SkylineParser.ASSIGNMENT, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.LPAR]:
                self.state = 8
                self.match(SkylineParser.LPAR)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(SkylineParser.RPAR)
                pass
            elif token in [SkylineParser.MINUS]:
                self.state = 12
                self.match(SkylineParser.MINUS)
                self.state = 13
                self.expr(10)
                pass
            elif token in [SkylineParser.SIMPLE]:
                self.state = 14
                self.match(SkylineParser.SIMPLE)
                pass
            elif token in [SkylineParser.LIST]:
                self.state = 15
                self.match(SkylineParser.LIST)
                pass
            elif token in [SkylineParser.RANDOM]:
                self.state = 16
                self.match(SkylineParser.RANDOM)
                pass
            elif token in [SkylineParser.IDENTIFIER]:
                self.state = 17
                self.match(SkylineParser.IDENTIFIER)
                pass
            elif token in [SkylineParser.INTEGER]:
                self.state = 18
                self.match(SkylineParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(
                        self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 9)")
                        self.state = 22
                        self.match(SkylineParser.MULT)
                        self.state = 23
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 8)")
                        self.state = 25
                        self.match(SkylineParser.PLUS)
                        self.state = 26
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 7)")
                        self.state = 28
                        self.match(SkylineParser.MINUS)
                        self.state = 29
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 6)")
                        self.state = 31
                        self.match(SkylineParser.ASSIGNMENT)
                        self.state = 32
                        self.expr(7)
                        pass

                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 9)

        if predIndex == 1:
            return self.precpred(self._ctx, 8)

        if predIndex == 2:
            return self.precpred(self._ctx, 7)

        if predIndex == 3:
            return self.precpred(self._ctx, 6)
