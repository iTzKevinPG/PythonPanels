from Vehiculos.Automovil import Automovil

class Moto(Automovil):
    placa: str
    modelo: str
    color: str

    def __init__(self, placa, modelo, color, tipoGasolina, motor, gasolina, aceite, llantas):

        self.placa = placa
        self.modelo = modelo
        self.color = color
        Automovil.__init__(Automovil, tipoGasolina, aceite, llantas)
        Automovil.setMotor(Automovil, motor)
        Automovil.setGasolina(Automovil, gasolina)
        pass

    def cambioLlantas(self, nuevasLlantas, cantidadLlantas):

        print("------------@------------@-------------")
        print(f"La moto tiene las llantas: {Automovil.llantas}, se va a cambiar por: {nuevasLlantas}, con una cantidad de {cantidadLlantas}")
        Automovil.llantas = nuevasLlantas
        print("Se realizo el cambio exitosamente")
        print('')
        pass

    def reparacion(self):

        Automovil.cambioLlantas(Automovil, 'Llantas nuevas')
        self.cambioLlantas('Llantas extra grandes', '1')
        pass

    pass

class Avion(Automovil):
    turbinas: str
    modelo: str
    color: str

    def __init__(self, turbinas, modelo, color, tipoGasolina, motor, gasolina, aceite, llantas):

        self.turbinas = turbinas
        self.modelo = modelo
        self.color = color
        Automovil.__init__(Automovil, tipoGasolina, aceite, llantas)
        Automovil.setMotor(Automovil, motor)
        Automovil.setGasolina(Automovil, gasolina)
        pass

    def cambioAceite(self, nuevoAceite, cantidadAceite):

        print("------------@------------@-------------")
        print(f"El avion tiene el aceite: {Automovil.aceite}, se va a cambiar por: {nuevoAceite}, con una cantidad de {cantidadAceite}")
        Automovil.aceite = nuevoAceite
        print("Se realizo el cambio exitosamente")
        print('')
        pass

    def mantenimiento(self):

        Automovil.cambioAceite(Automovil, 'Aceite pegajoso')
        self.cambioAceite('aceite espeso', '3000 litros')
        pass
    pass

