#  Nota:  Profesor yo trabaje la actividad individual porque todos los grupos estan completos. gracias por su atencion...


class AdmAgenda:
	
	def __init__(self):
		
		self.contactos=[]
 
	
	def menu(self):

            op = 0

            while op !=5:
          
                print("       AGENDA :  ")
                print("1. Añadir contacto: ")
                print("2. Lista de contactos: ")
                print("3. Buscar contacto: ")
                print("4. Editar o modificar contacto: ")
                print("4. salir: ")
                
		
 
                op=int(input("Introduzca la opción deseada: "))
                if op==1:
                    self.AñadirContactos()
                elif op==2:
                    self.listaDeContactos()
                elif op==3:
                    self.BuscarContactos()
                elif op==4:
                    self.EditarContactos()
                elif op==5:
                    print("Gracias por usar el programa ...")
                
        
                
                self.menu()
 
 
	
	def AñadirContactos(self):
            continua="s"
            while continua == "s":
                print("*************Añadir nuevo contacto*****************")
                nom=input("Digite el nombre: ")
                telf=int(input("Digite  el teléfono: "))
                email=input("Digite  el email: ")
                continua=input("Desea seguir añadiendo contactos [s/n]: ")

                self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		
 
	
	def listaDeContactos(self):		
		print("***************Lista de contactos****************")	
		if len(self.contactos) == 0:
			print(" Todavia No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x])
		
 
	
	def BuscarContactos(self):	
		print("***************Buscador de contactos*****************")	
		nom=input("Digite  el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print(self.contactos[x])
				
				return x
		
 
 
	
	def EditarContactos(self):
		print("******************Editar o modificar contacto*****************")	
		data=self.BuscarContactos()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			op=int(input("Digite la opción deseada: "))
			if op==1:
				nom=input("Digite  el nuevo nombre: ")
				self.contactos[data]['nombre']=nom
			elif op==2:
				telf=input("Digite  el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif op==3:
				email=input("Digite  el nuevo email: ")
				self.contactos[data]['email']=email
			elif op==4:
				condition=True
 
 
 

agenda=AdmAgenda()
agenda.menu()