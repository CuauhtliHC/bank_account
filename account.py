"""Modulo para importar clear y cls"""
from os import system, name

class Persona:
    """Clase para generar personas"""
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    """Clase para generar clientes"""
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""Nombre: {self.nombre} {self.apellido} 
Número de Cuenta: {self.numero_cuenta} 
Balance: ${self.balance}"""

    def depositar(self, cantidad):
        """Funcion para depositar"""
        self.balance += cantidad

    def retirar(self, cantidad):
        """Funcion para retirar"""
        if cantidad > self.balance:
            print("Saldo insuficiente")
        else:
            self.balance -= cantidad

def clear():
    """Funcion para limpiar la consola"""
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def crear_cliente():
    """Funcion para crear cliente"""
    clear()
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    account_num = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, account_num)
    return cliente



def inicio():
    """Funcion que inicia el programa"""
    mi_cliente = crear_cliente()
    opcion = None
    while opcion != "3":
        clear()
        print(mi_cliente)
        print("""[1] Depositar
[2] Retirar
[3] Salir""")
        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                cantidad = float(input("Ingrese la cantidad a depositar: $"))
                mi_cliente.depositar(cantidad)
            case "2":
                cantidad = float(input("Ingrese la cantidad a retirar: $"))
                mi_cliente.retirar(cantidad)
            case "3":
                print("Gracias por utilizar el sistema")
            case _:
                print("Opción inválida")


inicio()
