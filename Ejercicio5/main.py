from src.classGame import Game


if __name__ == '__main__':
    pieces = int(input("Ingrese el numero de piezas de juego: "))
    # Pila secuencial
    game = Game(pieces)
    game.start(pieces)
    print("Estado inicial del juego")
    print(game.getState())
    while not game.completed():
        print('Seleccione una pila para sacar una pieza:')
        piece = game.pop()
        print('Seleccione una pila donde colocar el pieza')
        game.push(piece)
        print(game.getState())
    print("Estado final del juego")
    print(game.getState())
    print('¡Felicitaciones, completaste el juego!')
