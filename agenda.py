from eventosEspecificos import Examen, TrabajoPractico, ReunionEstudio

class Agenda:
    def __init__(self):
        self.examenes = []
        self.trabajos = []
        self.reuniones = []

    def añadirExamen(self):
        nuevoEvento = Examen(
            float(input("Ingrese la fecha (dia.mes): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: ")),
            str(input("Ingrese el formato (oral o escrito): "))
            )
        self.examenes.append(nuevoEvento)

    def añadirTrabajo(self):
        nuevoEvento = TrabajoPractico(
            float(input("Ingrese la fecha de entrega (dia.mes): ")),
            float(input("Ingrese la fecha de inicio (dia.mes): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: ")),
            )
        self.trabajos.append(nuevoEvento)

    def añadirReunion(self):
        nuevoEvento = ReunionEstudio(
            float(input("Ingrese la fecha (dia.mes): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese el lugar: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: "))
        )
        self.reuniones.append(nuevoEvento)

    def mostrarExamenes(self):
        for examen in self.examenes:

            print(examen)

    def mostrarTrabajos(self):
        for trabajo in self.trabajos:

            print(trabajo)

    def mostrarReuniones(self):
        for reunion in self.reuniones:

            print(reunion)

    def mostrarEventos(self):
        self.mostrarExamenes()
        self.mostrarTrabajos()
        self.mostrarReuniones()