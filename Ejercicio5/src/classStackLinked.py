from src.classNode import Node


class Stack:
    __head = None
    __size = 0

    def __init__(self):
        self.__head = None
        self.__size = 0

    def __str__(self):
        out = '\n'
        while current is not None:
            out += str(current.getData()) + "\n^\n"
            current = current.getNext()
        out += '-'
        return out

    def isEmpty(self):
        return self.__size == 0

    def push(self, item):
        new_node = Node(item)
        new_node.setNext(self.__head)
        self.__head = new_node
        self.__size += 1

    def pop(self):
        remove = None
        if self.isEmpty():
            print("La pila está vacía")
        else:
            remove = self.__head.getData()
            self.__head = self.__head.getNext()
            self.__size -= 1
        return remove

    def top(self):
        if self.isEmpty():
            print("La pila está vacía")
        return self.__head.getData()
