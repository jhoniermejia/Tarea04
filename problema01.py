
#  Nota:  Profesor yo trabaje la actividad individual porque todos los grupos estan completos. gracias por su atencion...


class Alumno:
    
    def inicializador(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
 
 
    
    def resultado(self):
        if self.nota > 2.9:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha reprobado")
 
 
 

alumno1=Alumno()
alumno2=Alumno()
 

alumno1.inicializador("jhonier mejia",4)
alumno2.inicializador("solmaris gomez",2.5)
 

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()