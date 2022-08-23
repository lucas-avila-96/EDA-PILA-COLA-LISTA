from src.classStack import Stack


if __name__ == '__main__':
    n = int(input("Ingrese el tamaño de la pila:"))
    pila = Stack(n)
    print("Seleccione la pila donde insertar")
    print("1 - Pila 1\n2 - Pila 2\n0 - Salir")
    p = int(input("Pila: "))
    while p != 0 and not pila.isFull():
        item = input("Ingrese un caracter: ")
        if p == 1:
            pila.pushStack1(item)
        elif p == 2:
            pila.pushStack1(item)
        else: print('Selecione una pila entre 1 y 2')
        p = int(input("Pila: "))
    print("Pila completa")


        
    
        

