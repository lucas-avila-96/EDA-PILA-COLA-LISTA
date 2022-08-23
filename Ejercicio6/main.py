
from src.classQueue import Queue



if __name__ == '__main__':
    cola = Queue()

    cola.enqueue('a')
    cola.enqueue('b')
    cola.enqueue('c')

    cola.dequeue()
    cola.dequeue()

    print(cola)
