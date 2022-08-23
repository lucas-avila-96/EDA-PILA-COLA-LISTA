
from classStack import Stack

if __name__ == "__main__":

    stack = Stack(5)

    for i in range(5):
        stack.push(i + 1)
    
    stack.mostrar()

    print(f"Tope: {stack.getTope()}")




    '''
    stack = Stack()
    expresion = input('Expresion: ')
    i = 0
    error = False
    while (i < len(expresion)) and not error:
        x = expresion[i]
        if(x == "[" or x == "{" or x == "(" ):
            stack.push(x)
        if( x == "]" or x == "}" or x == ")" ):
            aux = stack.pop()
            if aux != None:
                print(aux)
                print(x)
                if(x == "]" and aux != "[" ) or (x == "}" and aux != "{" ) or (x == ")" and aux != "(" ):
                    error = True
        i += 1
    if not stack.isEmpty() or (error):
        print(" ERROR DE CORRESPONDENCIA")
    else:
        print(" CORRESPONDENCIA")



    '''