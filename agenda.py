from eventosEspecificos import Examen, TrabajoPractico, ReunionEstudio

class Agenda:
    def __init__(self):
        self.examenes = []
        self.trabajos = []
        self.reuniones = []
        self.eventos = []
    

    #Funcion comprobar fechas por array para despue :3
    #ultimoId = 0
    #def añadirEvento(self, evento):
    #   evento.id = Agenda.ultimo_id + 1  
    #    Agenda.ultimo_id += 1  
    #   self.eventos.append(evento)

    # Añadir un examen

    def añadirExamen(self):
        nuevoEvento = Examen(
            str(input("Ingrese la fecha (dia/mes/año): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: ")),
            str(input("Ingrese el formato (oral o escrito): "))
            )
        self.examenes.append(nuevoEvento)
        self.eventos.append(nuevoEvento)
        #self.añadirEvento(nuevoEvento)

    # Añadir un trabajo
    def añadirTrabajo(self):
        nuevoEvento = TrabajoPractico(
            str(input("Ingrese la fecha de entrega (dia/mes/año): ")),
            str(input("Ingrese la fecha de inicio (dia/mes/año): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: ")),
            )
        self.trabajos.append(nuevoEvento)
        self.eventos.append(nuevoEvento)

    # Añadir una reunion
    def añadirReunion(self):
        nuevoEvento = ReunionEstudio(
            str(input("Ingrese la fecha (dia/mes/año): ")),
            str(input("Ingrese una descripcion: ")),
            str(input("Ingrese el lugar: ")),
            str(input("Ingrese la materia: ")),
            str(input("Ingrese el tema: "))
        )
        self.reuniones.append(nuevoEvento)
        self.eventos.append(nuevoEvento)


    # Mostrar examenes
    def mostrarExamenes(self):
        for examen in self.examenes: # Por cada examen en la lista de examenes

            print(examen)

    def mostrarTrabajos(self):
        for trabajo in self.trabajos:

            print(trabajo)

    def mostrarReuniones(self):
        for reunion in self.reuniones:

            print(reunion)

    # Mostrar todo
    def mostrarEventos(self):
        for evento in self.eventos:
            print(evento)

    # Eliminar evento
    def eliminarEvento(self, descripcion):
        for evento in self.eventos:
            if descripcion == evento.descripcion:  
                self.eventos.remove(evento)
                print(f"Se ha eliminado el evento con la descripción: {descripcion}")

                # Eliminar de las otras listas
                if evento in self.examenes:
                    self.examenes.remove(evento)
                elif evento in self.trabajos:
                    self.trabajos.remove(evento)
                elif evento in self.reuniones:
                    self.reuniones.remove(evento)
            else:  
                print("No se encontró ningún evento con esa descripción.")