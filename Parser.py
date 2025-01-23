from enum import Enum
from Lexer import Type


"""
Grammaire générale :

expression = term ( ('+' | '-') term )*
term       = factor ( ('*' | '/' | '%') factor )* 
factor     = NUMBER | IDENT | '(' expression ')'

"""
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        node = self.parse_expression()
        return node

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        token = self.current()
        self.pos += 1
        return token

    def parse_expression(self):
        """
        Grammaire (simplifiée) :
            expression -> term (('+' | '-') term)*
        Priorité : on traite d'abord parse_term (qui gère '*','/','%').
        """
        node = self.parse_term()

        while True:
            token = self.current()
            if token and token['type'] == Type.SYMBOL and token['symbol'] in ['+', '-']:
                op = token['symbol']
                self.consume()
                right = self.parse_term()
                node = {
                    'op': op,
                    'left': node,
                    'right': right
                }
            else:
                break

        return node

    def parse_term(self):
        """
        Grammaire (simplifiée) :
            term -> factor (('*' | '/' | '%') factor)*
        On gère les opérateurs binaires de "niveau terme".
        """
        node = self.parse_factor()

        while True:
            token = self.current()
            if token and token['type'] == Type.SYMBOL and token['symbol'] in ['*', '/', '%']:
                op = token['symbol']
                self.consume()
                right = self.parse_factor()
                node = {
                    'op': op,
                    'left': node,
                    'right': right
                }
            else:
                break

        return node

    def parse_factor(self):
        """
        Grammaire (simplifiée) :
            factor -> NUMBER | IDENT | '(' expression ')'
        """
        token = self.current()
        
        if token['type'] == Type.NUMBER:
            self.consume()
            return token['symbol']

        elif token['type'] == Type.IDENT:
            self.consume()
            return {
                'var': token['symbol']
            }

        elif token['type'] == Type.SYMBOL and token['symbol'] == '(':
            self.consume()
            node = self.parse_expression()
            self.consume()
            return node
