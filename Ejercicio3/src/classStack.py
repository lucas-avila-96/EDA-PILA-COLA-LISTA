import numpy as np


class Stack:
    __top = 0
    __size = 0
    __items = None

    def __init__(self, size):
        self.__top = 0
        self.__size = size
        self.__items = np.empty(self.__size, int)

    def __str__(self):
        out = '\n'
        for i in reversed(range(self.__top)):
            out += str(self.__items[i]) + "\n^\n"
        return out

    def isFull(self):
        return self.__top == self.__size

    def isEmpty(self):
        return self.__top == 0

    def push(self, item):
        if self.isFull():
            print("Pila completa")
        else:
            self.__items[self.__top] = item
            self.__top += 1

    def pop(self):
        remove = None
        if self.isEmpty():
            print("La pila está vacía")
        else:
            remove = self.__items[self.__top - 1]
            self.__top -= 1
        return remove

    def top(self):
        return self.__items[self.__top - 1]

    def getSize(self):
        return self.__top
