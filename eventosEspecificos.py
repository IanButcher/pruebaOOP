from evento import Evento
class Examen (Evento):
    def __init__(self, fecha, descripcion, materia, tema, formato):
        super().__init__(fecha, descripcion, materia, tema)
        self.formato = formato
        
    def __str__(self):
        return f"Se creo un nuevo examen de {self.materia}, tema: {self.tema} para el dia {self.fecha}"
    

class TrabajoPractico (Evento):
    def __init__(self, fecha, fechaInicio, descripcion, materia, tema):
        super().__init__(fecha, descripcion, materia, tema)
        self.fechaInicio = fechaInicio

    def __str__(self):
        return f"Se creo un nuevo trabajo practico de {self.materia}, tema: {self.tema} para el dia {self.fecha}"

class ReunionEstudio:
    def __init__(self, fecha, descripcion, lugar, materia, tema):
        super().__init__(fecha, descripcion, materia, tema)
        self.lugar = lugar

    def __str__(self):
        return f"Se creo una nueva reunion el dia {self.fecha} en {self.lugar}"