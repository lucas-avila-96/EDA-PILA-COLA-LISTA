from src.classStackLinked import Stack

def factorial(number, stack):
    f = 1
    while number:
        stack.push(number)
        number -= 1
    
    for i in range(stack.getTope()):
        f *= stack.pop()

    return f
if __name__ == "__main__":
    #Pila Secuencial
    #stack = Stack(50)
    #Pila Enlazada
    stack = Stack()
    print("Introduzca un entero positivo: ")
    number = int(input("Numero:"))
    f = factorial(number, stack)
    print(f"El factorial de {number} es {f}")