#  Nota:  Profesor yo trabaje la actividad individual porque todos los grupos estan completos. gracias por su atencion...


class Cuenta:
        def __init__(self):
            self.titular="Jhonier Mejia"
            self.cantidad= 800000

        def imprimir(self):
            print(f"Nombre del Titular : {self.titular}")
            print(f"Cantidad : {self.cantidad}\n")

class CajadeAhorro(Cuenta):
        def __init__(self):
            super().__init__()
            
        def mostrardeCajaAhorro(self):
            super().imprimir()

class PlazoFijo(Cuenta):
        def __init__(self):
            super().__init__()
            self.plazo ="dos años"
            self.interes = 0.8
        
        def importeInteres(self):
            self.importe = (self.cantidad*self.interes)/100
            return self.importe

        def MostrarDatos(self):
            self.intereses = self.importeInteres()
            print("\n************* Datos del titular************* \n")
            super().imprimir()
            print(f"EL plazo de pago es de :  {self.plazo}")
            print(f"La cuota de Interes es del : {self.interes}")
            print(f"El total de intereses es de : {self.intereses}\n")


def MostrarDatosFinales():
        inter =PlazoFijo()
        inter.MostrarDatos()

def MostrarCaja():
        caja =CajadeAhorro()
        caja.mostrardeCajaAhorro()

def ImprimirCuenta():
        cuenta1 = Cuenta()
        cuenta1.imprimir()



def menu():
       
        op = 0

        while op !=4:
          
            print("   Estado de la Cuenta:  ")
            print("1. Imprimir datos cuenta Inicial: ")
            print("2. Mostrar Caja de Ahorro: ")
            print("3. Mostrar Estado de cuenta final: ")
            print("4. salir: ")
            op = int(input("Digite  una opcion:  "))

            if op==1:
                ImprimirCuenta()
            elif op==2:
                MostrarCaja()
            elif op==3:
                MostrarDatosFinales()
            elif op==4:
                print("Gracias por utilizar el programa ")
                break
            else:
                print("Opción incorrecta.......")
                break
            


def main():
    menu()

if __name__ == "__main__":
    main()