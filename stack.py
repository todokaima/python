class Stack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if  self.array == []: return None
        else: return self.array.pop()

    def length(self):
        return len(self.array)



