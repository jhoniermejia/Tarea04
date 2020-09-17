#  Nota:  Profesor yo trabaje la actividad individual porque todos los grupos estan completos. gracias por su atencion...


class Banco:
	
	def __init__(self):
		self.cliente1=Cliente("jhonier mejia")
		self.cliente2=Cliente("jhoneider mejia")
		self.cliente3=Cliente("yohelis mejia")

	def Operacion(self):
		self.cliente1.depositar(2000)
		self.cliente2.depositar(5000)
		self.cliente3.depositar(40000)
		self.cliente2.extraer(2500)
 
	
	def Deposito_total(self):
		total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
 
 

class Cliente:
	
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0
 
	
	def depositar(self,cantidad):
		self.cantidad+=cantidad
 
	
	def extraer(self,cantidad):
		self.cantidad-=cantidad
 
	
	def devolver_cantidad(self):
		return self.cantidad
 
	
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
 
 

bancox=Banco()
bancox.Operacion()
bancox.Deposito_total()