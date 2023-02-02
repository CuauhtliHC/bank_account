from os import system, name

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""Nombre: {self.nombre} {self.apellido} 
Número de Cuenta: {self.numero_cuenta} 
Balance: ${self.balance}"""

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Saldo insuficiente")
        else:
            self.balance -= cantidad

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def crearCliente():
    clear()
    nombreCl = input("Ingrese su nombre: ")
    apellidoCl = input("Ingrese su apellido: ")
    accountNum = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombreCl, apellidoCl, accountNum)
    return cliente



def inicio():   
    miCliente = crearCliente()
    opcion = None
    while opcion != "3":
        clear()
        print(miCliente)
        print("""[1] Depositar 
[2] Retirar
[3] Salir""")
        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                cantidad = float(input("Ingrese la cantidad a depositar: $"))
                miCliente.depositar(cantidad)
            case "2":
                cantidad = float(input("Ingrese la cantidad a retirar: $"))
                miCliente.retirar(cantidad)
            case "3":
                print("Gracias por utilizar el sistema")
            case _:
                print("Opción inválida")


inicio()