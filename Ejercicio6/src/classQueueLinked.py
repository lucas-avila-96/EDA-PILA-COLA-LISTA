from src.classNode import Node


class QueueLinked:
    __front = None
    __rear = None
    __count = 0

    def __init__(self):
        self.__rear = None
        self.__front = None
        self.__count = 0

    def __str__(self):
        out = ''
        current = self.__front
        while current is not None:
            out += current.getData() + '->'
            current = current.getNext()
        return out

    def dequeue(self):
        if self.__front is None:
            print('La cola esta vacia')
        temp = self.__front
        self.__front = self.__front.getNext()
        if self.__front is None:
            self.__rear = None
        self.__count -= 1
        return temp.getData()

    def enqueue(self, item):
        node = Node(item)
        if self.__front is None:
            self.__front = node
            self.__rear = node
        else:
            self.__rear.setNext(node)
            self.__rear = node
        self.__count += 1

    def isEmpty(self):
        return self.__rear is None and self.__front is None
