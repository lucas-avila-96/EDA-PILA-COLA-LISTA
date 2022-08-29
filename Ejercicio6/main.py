
from src.classQueueLinked import QueueLinked



if __name__ == '__main__':
    cola = QueueLinked()

    cola.enqueue('a')
    cola.enqueue('b')
    cola.enqueue('c')
    cola.enqueue('d')
    cola.enqueue('e')


    cola.dequeue()
    cola.dequeue()

    print(cola)
