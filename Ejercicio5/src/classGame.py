
from src.classStack import Stack


class Game:
    __stack1 = None
    __stack2 = None
    __stack3 = None

    def __init__(self, d):
        self.__stack1 = Stack(d)
        self.__stack2 = Stack(d)
        self.__stack3 = Stack(d)

    def getState(self) -> str:
        return f"Pila 1:{self.__stack1}\nPila 2:{self.__stack2}\nPila 3:{self.__stack3}\n"

    def start(self, discos):
        for i in reversed(range(discos)):
            self.__stack1.push(i + 1)

    def completed(self):
        return self.__stack3.isFull()

    def pop(self):
        correctMove = False
        errorMessage = 'Error, no hay piezas para sacar. Intenta con otra stack'
        msjCorrecto = '¡Sacaste un pieza!'

        while not correctMove:
            stack = int(input("Pila:"))
            match stack:
                case 1:
                    if self.__stack1.isEmpty():
                        print(errorMessage)
                    else:
                        top = self.__stack1.pop()
                        print(msjCorrecto)
                        correctMove = True
                case 2:
                    if self.__stack2.isEmpty():
                        print(errorMessage)
                    else:
                        top = self.__stack2.pop()
                        print(msjCorrecto)
                        correctMove = True
                case 3:
                    if self.__stack3.isEmpty():
                        print(errorMessage)
                    else:
                        top = self.__stack3.pop()
                        print(msjCorrecto)
                        correctMove = True
                case _:
                    print("Ingrese un numero entre 1 y 3")
        return top

    def push(self, piece):
        errorMessage = 'Error. La ultima pieza es menor que el que intentas colocar'
        successfulMessage = '¡Realizaste un movimiento correcto!'
        correctMove = False
        while not correctMove:
            stack = int(input("Pila:"))
            match stack:
                case 1:
                    if self.__stack1.isEmpty() or self.__stack1.top() > piece:
                        self.__stack1.push(piece)
                        correctMove = True
                        print(successfulMessage)
                    else:
                        print(errorMessage)
                case 2:
                    if self.__stack2.isEmpty() or self.__stack2.top() > piece:
                        self.__stack2.push(piece)
                        correctMove = True
                        print(successfulMessage)
                    else:
                        print(errorMessage)
                case 3:
                    if self.__stack3.isEmpty() or self.__stack3.top() > piece:
                        self.__stack3.push(piece)
                        correctMove = True
                        print(successfulMessage)
                    else:
                        print(errorMessage)
                case _:
                    print("Ingrese un numero entre 1 y 3")
