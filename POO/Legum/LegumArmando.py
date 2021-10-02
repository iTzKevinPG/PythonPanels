from Legum.Employee import Employee
from Legum.Fruits import Fruit
from Legum.Legum import Legum

class Legume(Employee,Fruit,Legum):
    
    #Default parameters
    
    nit: int 
    owner: str 
    
    def __init__(self, nit, owner):
        self.nit = nit
        self.owner = owner
        
    def addEmployee(self, idEmployee, name, phone, email):
        Employee.__init__(Employee, idEmployee, name, phone, email)
        pass
    
    def addFruitProduct(self, name, idProduct):
        Fruit.__init__(Fruit, idProduct, name)
        pass
    
    def addLegumProduct(self, name, idProduct):
        Legum.__init__(Legum, idProduct, name)
        pass
    
    def showEmployees(self):
            
        print("los Empleados son")
        
        for i in range(len(Employee.employees)):
            
            print(f"{i+1}. {Employee.employees[i]['name']} con identificador {Employee.employees[i]['idEmployee']}")
            pass
        
        pass
    
    def showProducts(self):
            
        Fruit.showFruits(Fruit)
        Legum.showLegums(Legum)
        
        pass