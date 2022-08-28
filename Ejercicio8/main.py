import math
from src.classQueue import Queue
import random


if __name__ == '__main__':
    atencionMedica = 20
    tiempoAnotar = 60
    tiempoEspTotal = 0
    reloj = 0
    reloj2 = 0
    tms = 240
    sinTruno = 0
    demoraAnotar = 0
    pacientes = Queue()
    ginecologo = Queue(10)
    clinico = Queue(10)
    pediatria = Queue(10)
    oftalmologo = Queue(10)


    while reloj <= tiempoAnotar:
        n = random.randint(0, 1)
        if n == 1:
            pacientes.enqueue(reloj)
        reloj += 1
        if demoraAnotar == 0:
            tiempoAnotar = random.randint(1, 2)
            pac = pacientes.dequeue()
            nombre = input()
            dni = input()
            esp = input()
            match esp:
                case 'ginecologia':
                    if ginecologo.isFull():
                        print('maximo alcanzado')
                        sinTruno += 1 
                    else:
                        ginecologo.enqueue(0)
                case 'ginecologia':
                    if ginecologo.isFull():
                        print('maximo alcanzado')
                        sinTruno += 1 
                    else:
                        ginecologo.enqueue(0)
                case 'ginecologia':
                    if ginecologo.isFull():
                        print('maximo alcanzado')
                        sinTruno += 1 
                    else:
                        ginecologo.enqueue(0)
                case 'ginecologia':
                    if ginecologo.isFull():
                        print('maximo alcanzado')
                        sinTruno += 1 
                    else:
                        ginecologo.enqueue(0)
        else:
            demoraAnotar -= 1

        
        
    '''
    un while
    una cola para guardar los pacientes que llegan con el tiempo de llegada(reloj)


    while:

    
    
    '''
