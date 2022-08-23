import numpy as np

class Stack:
    __top = 0
    __cant = 0
    __items = None

    def __init__(self, cantidad = 0):
        self.__top = 0
        self.__cant = cantidad
        self.__items = np.empty(cantidad, int)

    def isEmpty(self):
        return self.__top == 0

    def push(self, item):
        if self.__top < self.__cant:
            self.__items[self.__top] = item
            self.__top += 1
        else:
            print("Maximo alcanzado")

    def pop(self):
        remove = None
        if self.isEmpty():
            print("La pila está vacía")
        else:
            remove = self.__items[self.__top - 1]
            self.__tope -= 1
        return remove

    def mostrar(self):
        for i in reversed(range(self.__top)):
            print(self.__items[i])

    def getTope(self):
        return self.__top
    

