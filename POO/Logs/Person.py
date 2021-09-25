from Logs.ActionLog import save_log

class Person():

    #default parameters
    name: str
    phone: str
    direction: str
    email: str
    actionUser: str

    def __init__(self, name, phone, direction, email):
        self.name = name
        self.phone = phone
        self.direction = direction
        self.email = email
        pass

    def showParameters(self):
        print(f"El nombre es {self.name}")
        print(f"El telefono es {self.phone}")
        print(f"La direccion es {self.direction}")
        print(f"El correo es {self.email}")
        pass

    @save_log
    def auth(self, action):
        self.actionUser = action
        self.show_logMessage(self.name, self.actionUser)
        return self

    @staticmethod
    def show_logMessage(name, action):
        print(f"El usuario {name} realizo la accion: {action}.")
        pass 

    @save_log
    def changePhone(self, action, newPhone):
        self.phone = newPhone
        self.actionUser = action
        self.show_logMessage(self.name, self.actionUser)
        return self
        
    @classmethod
    def showClassMethod(cls):
        print(f"La clase actual es {cls}")


