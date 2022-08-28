from src.classQueue import Queue
import random


if __name__ == '__main__':
    q = Queue()
    frecLLegada = 2
    tms = 60
    tiempoCajero = 5
    reloj = 0
    totalEspera = 0
    clienteAtendido = 0
    while reloj <= tms:
        n = random.randint(1, 2)
        if n == 1:
            q.enqueue(reloj)
        if tiempoCajero == 0:
            if not q.isEmpty():
                esperaCliente = q.dequeue()
                totalEspera = reloj - esperaCliente
                clienteAtendido += 1
                tiempoCajero = 5
        else:
            tiempoCajero -= 1
        reloj += 1
    promedio = totalEspera / clienteAtendido

    print(promedio)

        

        
    
    