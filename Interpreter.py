class Interpreter:

    @staticmethod
    def exec(node, x):
        if 'op' in node:
            left = Interpreter.exec(node['left'], x)
            right = Interpreter.exec(node['right'], x)

            if node['op'] == '+':
                return left + right
            elif node['op'] == '-':
                return left - right
            elif node['op'] == '*':
                return left * right
            elif node['op'] == '/':
                if right != 0:
                    return left / right
                else:
                    print("Division par zéro !")
                    return None
            elif node['op'] == '%':
                if right != 0:
                    return left % right
                else:
                    print("Division par zéro !")
                    return None

        if 'var' in node:
            return x
        
        return float(node)
