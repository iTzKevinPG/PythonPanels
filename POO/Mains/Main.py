from Legum.LegumArmando import Legume
from Logs.Person import Person
from Vehiculos.Vehiculos import Moto, Avion
"""
legume1 = Legume(2021, "Armando")

legume1.addEmployee(1, "Eme", "300620", "eme.yuli@email.co")
legume1.addEmployee(2, "Kevin", "302340", "kevinuj@email.co")

legume1.addFruitProduct("Manzana", 1)
legume1.addFruitProduct("Uva", 2)

legume1.addLegumProduct("Cebolla", 1)
legume1.addLegumProduct("Tomate", 2)

legume1.showProducts()
legume1.showEmployees()
"""

"""
person1 = Person('Kevin','3026756898','Medellin','prueba@gmail.com')

person1.auth('Inicio Sesion')
person1.showParameters()
person1.changePhone('Edicion','3024569851')
person1.showParameters()
person1.showClassMethod()
"""

avion = Avion('Extra grandes', '2015', 'blanco', 'Extra', '4000C', '3Galones', 'Especial', '4')

avion.encender()
avion.mantenimiento()




moto = Moto('ZFM34B', '2021', 'Negra', 'Corriente', '3000C', '2Galones', 'Normal', '2')

moto.encender()
moto.reparacion()

print("------------@------------@-------------")
print(f"El motor de la moto es:{moto.getMotor()}")
print(f"La gasolina de la moto es:{moto.getGasolina()}")
print('')
print("------------@------------@-------------")
print(f"El motor del avion es:{avion.getMotor()}")
print(f"La gasolina del avion es:{avion.getGasolina()}")
