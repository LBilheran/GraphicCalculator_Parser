from pprint import pprint

from Lexer import Lexer
from Parser import Parser

lexer = Lexer("y = x * (x * 5)")
tokens = lexer.parse()

pprint(tokens)

parser = Parser(tokens)
parser.parse()