from src.classStackLinked import Stack

def binario(number, stack):
    while number != 0:
        stack.push(number % 2)
        number = number // 2
    result = ''
    for i in range(stack.getTope()):
        result += str(stack.pop()) 
    return result

if __name__ == "__main__":
    #Pila Secuencial
    #stack = Stack(50)
    #Pila Enlazada
    stack = Stack()
    number = int(input("Numero Decimal:"))
    bin = binario(number, stack)
    print(f"El Numero Decimal {number} en binario es {bin}")



'''
pilaLLena

pilavacia1
pilavacia2
'''
