from agenda import Agenda

# Crear agenda
agenda = Agenda()

while True:
    print("1. Para ver mis eventos")
    print("2. Para crear un examen")
    print("3. Para crear un trabajo practico")
    print("4. Para crear una reunion de estudio")
    eleccion = int(input())

    # Elecciones
    if eleccion == 1:
        agenda.mostrarEventos()

    elif eleccion == 2:
        agenda.mostrarExamenes()
        agenda.añadirExamen()

    elif eleccion == 3:
        agenda.mostrarTrabajos()
        agenda.añadirTrabajo()

    elif eleccion == 4:
        agenda.mostrarReuniones()
        agenda.añadirReunion()
    