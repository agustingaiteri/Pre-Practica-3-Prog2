class Vehiculo():
    
    #constructor - Inicializo las variables
    def __init__(self,marca,ruedas,color,enMarcha=False):
        self.marca=marca
        self.ruedas=ruedas
        self.color=color
        self.enMarcha=enMarcha
        
    def arrancar(self):
        self.enMarcha=True
        
    def tipoVehiculo(self):
        if(self.ruedas==4):
            return "Automovil"
        else:
            return "Motocicleta"
    
    def mostras(self):
        print(self.marca)
        print(self.color)
        print(self.ruedas)
        print(self.enMarcha)
                    
auto_1=Vehiculo("Ford",4,"Azul",False)
print(auto_1.marca)
print(auto_1.color)
auto_1.arrancar()
auto_1.tipoVehiculo()
print(auto_1.tipoVehiculo())
auto_1.mostrar()
auto_2=Vehiculo("Toyota",4,"Amarillo",False)
print(auto_2.marca)
print(auto_2.color)