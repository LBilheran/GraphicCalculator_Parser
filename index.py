from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

source_code = "x * (x * 5) - 20"

lexer = Lexer(source_code)
tokens = lexer.parse()
print("Tokens :")
pprint(tokens)

parser = Parser(tokens)
ast = parser.parse()
print("\nAST :")
pprint(ast)

x_values = np.arange(-10, 10, 0.5)
y_values = [Interpreter.exec(ast, x) for x in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values, marker='o')
plt.title(source_code)
plt.grid(True)
plt.show()
