class Automovil:
    __motor: str
    __gasolina: str
    tipoGasolina: str
    aceite: str
    llantas: str

    def __init__(self, tipoGasolina, aceite, llantas):

        self.tipoGasolina = tipoGasolina
        self.aceite = aceite
        self.llantas = llantas
        pass

    def estadoAutomovil(self):

        print("------------@------------@-------------")
        print(f"El tipo de gasolina de su automovil es: {self.tipoGasolina}, y su cantidad es: {self.__gasolina}")
        print(f"El estado de su aceite: {self.aceite}, es bueno")
        print(f"El estado de su motor: {self.__motor}, es bueno")
        print('')
        pass

    def ignicionMotor(self):

        print("------------@------------@-------------")
        print(f"Se da paso de energia y gasolina al motor {self.__motor}")
        print('')
        pass

    def encender(self):

        self.estadoAutomovil()
        self.ignicionMotor()
        pass

    def cambioAceite(self, nuevoAceite):

        print("------------@------------@-------------")
        print(f"El automovil tiene el aceite: {self.aceite}, se va a cambiar por: {nuevoAceite}")
        self.aceite = nuevoAceite
        print("Se realizo el cambio exitosamente")
        print('')
        pass


    def cambioLlantas(self, nuevasLlantas):

        print("------------@------------@-------------")
        print(f"El automovil tiene las llantas: {self.llantas}, se van a cambiar por: {nuevasLlantas}")
        self.llantas = nuevasLlantas
        print("Se realizo el cambio exitosamente")
        print('')
        pass
     
    def getMotor(self):

        return self.__motor

    def setMotor(self, motor):

        self.__motor = motor
        pass

    def getGasolina(self):

        return self.__gasolina

    def setGasolina(self, gasolina):

        self.__gasolina = gasolina
        pass

    pass
    