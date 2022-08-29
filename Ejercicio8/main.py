from src.classQueue import Queue
import random


if __name__ == '__main__':
    tms = 240
    atencionMedica = 20
    tiempoAnotar = 60
    tiempoEspTotal = 0
    pacAnotados = 0
    reloj = 0
    sinTurno = 0
    demoraAnotar = 2
    pacientes = Queue()
    ginecologo = Queue(10)
    clinico = Queue(10)
    pediatra = Queue(10)
    oftalmologo = Queue(10)


    while reloj <= tiempoAnotar:
        llegaPaciente = random.randint(0, 1)
        if llegaPaciente == 1:
            # si llega un paciente se agrega a la cola
            pacientes.enqueue(reloj)
        if demoraAnotar == 0:
            if not pacientes.isEmpty():
                # Si la cola no esta vacia lo saca
                pac = pacientes.dequeue()
                # se establece una demora promedio de 1 a 2 minutos en la mesa de entrada
                demoraAnotar = random.randint(1, 2)
                tiempoEspTotal += reloj - pac
                nombre = input('Nombre:')
                dni = input('Dni: ')
                esp = input('Especialidad: ')
                match esp: 
                    case 'ginecologia':
                        if ginecologo.isFull():
                            print('maximo alcanzado')
                            sinTurno += 1 
                        else:
                            ginecologo.enqueue(0)
                            pacAnotados += 1
                    case 'clinico':
                        if clinico.isFull():
                            print('maximo alcanzado')
                            sinTurno += 1 
                        else:
                            clinico.enqueue(0)
                            pacAnotados += 1
                    case 'pediatra':
                        if pediatra.isFull():
                            print('maximo alcanzado')
                            sinTurno += 1 
                        else:
                            pediatra.enqueue(0)
                            pacAnotados += 1
                    case 'oftalmologo':
                        if oftalmologo.isFull():
                            print('maximo alcanzado')
                            sinTurno += 1 
                        else:
                            oftalmologo.enqueue(0)
                            pacAnotados += 1
        else:
            demoraAnotar -= 1
        reloj += 1

    promedio = tiempoEspTotal / pacAnotados

    print(f'Promedio de tiempo de espera en la cola de turnos: {promedio}')
    print(f'Cantidad de pacientes sin turno: {sinTurno}')

    reloj2 = 0
    pacienteAt = 0
    esperaTotal = 0
    while reloj2 < tms:
        if atencionMedica == 0:
            if not ginecologo.isEmpty():
                esperaPaciente = ginecologo.dequeue()
                esperaTotal = reloj2 - esperaPaciente
                pacienteAt += 1
                #tiempo promedio de atención del médico 20 minutos
                atencionMedica = random.randint(1, 20)
        else:
            atencionMedica -= 1
        ginecologo.actualizarTiempo(reloj2)
        reloj2 += 1
    promedioGinecologia = esperaTotal / pacienteAt

    print(f'Promedio de espera en especialidades {promedioGinecologia}')