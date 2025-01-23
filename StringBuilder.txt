class StringBuilder:

    def __init__(self):
        self.arr = []

    def append(self, str):
        self.arr.append(str)

    def clear(self):
        self.arr.clear()

    def __str__(self):
        return "".join(self.arr)
