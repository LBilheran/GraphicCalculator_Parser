from StringBuilder import StringBuilder
from enum import Enum

class Type(Enum):
    SYMBOL = 1
    NUMBER = 2
    IDENT = 3

class Lexer:

    def __init__(self, src):
        self.src = src
        self.i = 0
        self.sb = StringBuilder()
        self.tokens = []

    def current(self):
        return self.src[self.i]

    def consume(self):
        self.sb.append(self.current())
        self.i += 1

    def hasNext(self):
        return self.i < len(self.src)
    
    def createToken(self, type):
        self.tokens.append({'symbol': str(self.sb), 
                            'type': type})
        self.sb.clear()

    # Null = ' ' | '\t'
    def parseNull(self):
        if self.current() in [' ', '\t']:
            self.consume()
            self.sb.clear()
            return True
        else:
            return False

    # D = [0-9]
    def parseDigit(self):
        if self.current() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.consume()
            return True
        else:
            return False

    # N = D+
    def parseNumber(self):
        if not self.parseDigit(): return False

        while self.hasNext():
            if not self.parseDigit(): break

        self.createToken(Type.NUMBER)

        return True

    # S = '=' | '+' | '-' | '*' | '/' | '%' | '(' | ')'
    def parseSymbol(self):
        if self.current() in ['=', '+', '-', '*', '/', '%', '(', ')']:
            self.consume()
            self.createToken(Type.SYMBOL)
            return True
        
        return False

    # I = 'x' | 'y'
    def parseIdent(self):
        if self.current() in ['x', 'y']:
            self.consume()
            self.createToken(Type.IDENT)
            return True
        
        return False

    def parse(self):
        
        while self.hasNext():
            if self.parseNull(): continue
            if self.parseNumber(): continue
            if self.parseSymbol(): continue
            if self.parseIdent(): continue

        return self.tokens

