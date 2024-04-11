class Evento:
    def __init__ (self, fecha, descripcion, materia, tema):
        self.fecha = fecha
        self.descripcion = descripcion
        self.materia = materia
        self.tema = tema

        if self.fecha > 31.12:
            print("La fecha no es posible")
            self.fecha = "La fecha ingresada fue invalida"
    
    