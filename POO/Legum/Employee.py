class Employee():
        
    #Instance parameters
    employees = []
    
    def __init__(self, idEmployee, name, phone, email):
        
        self.employees.append({'idEmployee': idEmployee, 'name': name, 'phone': phone, 'email': email})
        
        print(f"Se agrego el empleado: {name} con la identificacion: {idEmployee}")
        pass
      