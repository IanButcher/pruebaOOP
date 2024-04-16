from evento import Evento
class Examen (Evento):
    def __init__(self, fecha, descripcion, materia, tema, formato):
        super().__init__(fecha, descripcion, materia, tema)
        self.formato = formato.lower()
        if formato != "oral" or formato != "escrito":
            print("Formato invalido")
        
    def __str__(self):
        return f"Examen---- Materia: {self.materia}, tema: {self.tema} para el dia: {self.fecha} con el formato: {self.formato}. Descripcion: {self.descripcion}"
    

class TrabajoPractico (Evento):
    def __init__(self, fecha, fechaInicio, descripcion, materia, tema):
        super().__init__(fecha, descripcion, materia, tema)
        self.fechaInicio = fechaInicio

    def __str__(self):
        return f"Trabajo practico---- Materia: {self.materia}, tema: {self.tema},desde el dia: {self.fechaInicio} para el dia {self.fecha}. Descripcion: {self.descripcion}"

class ReunionEstudio:
    def __init__(self, fecha, descripcion, lugar, materia, tema):
        super().__init__(fecha, descripcion, materia, tema)
        self.lugar = lugar

    def __str__(self):
        return f"Reunion---- el dia {self.fecha} en {self.lugar} de la materia: {self.materia}. Descripcion: {self.descripcion}"