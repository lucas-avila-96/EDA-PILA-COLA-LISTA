import numpy as np

class Stack:
    __top1 = 0
    __top2 = 0
    __max = 0
    __items = None

    def __init__(self, max):
        self.__top1 = 0
        self.__top2 = max
        self.__max = max
        self.__items = np.empty(max, str)

    def __str__(self):
        out = ''
        for item in self.__items:
            out += str(item) + "->"
        return out

    def isEmptyStack1(self):
        return self.__top1 == 0

    def isEmptyStack2(self):
        return self.__top2 == self.__max

    def isFull(self):
        return self.__top1 + 1 == self.__top2

    def pushStack1(self, item):
        if self.isFull():
            print("Maximo alcanzado")
        else:
            self.__items[self.__top1] = item
            self.__top1 += 1
            print("Elemento insertado")

    def pushStack2(self, item):
        if self.isFull():
            print("Maximo alcanzado")
        else:
            self.__items[self.__top2] = item
            self.__top2 -= 1
            print("Elemento insertado")

    def popStack1(self):
        remove = None
        if self.isEmptyStack1():
            print("La pila está vacía")
        else:
            remove = self.__items[self.__top1 - 1]
            self.__top1 -= 1
        return remove

    def popStack2(self):
        remove = None
        if self.isEmptyStack2():
            print("La pila está vacía")
        else:
            remove = self.__items[self.__top2 - 1]
            self.__top2 += 1
        return remove



