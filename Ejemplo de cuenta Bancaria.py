#Ejemplo de cuenta bancaria con programación tradicional
balance = 0
interes = 0.05

def depositar(cuenta):
    global balance
    balance += cuenta

def retirar(cuenta):
    global balance
    balance -= cuenta

def calcular_interes():
    global balance, interes
    interes_t = balance * interes
    balance += interes_t

deposito = int(input("¿Cuánto dinero desea depositar?: "))
depositar(deposito)
retiro = int(input("¿Cuánto dinero desea retirar?: "))
retirar(retiro)
calcular_interes()

print("Su balance es", round(balance,2))

#Ejemplo de cuenta bancaria con POO
class Cuenta_Bancaria:
    def __int__(self,balance_inicial = 0, interes = 0.05):
        self.balance = balance_inicial
        self.interes = interes

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad

    def calcular_interes(self):
        interes_t = self.balance * self.interes
        self.balance += interes_t

cuenta = Cuenta_Bancaria()
deposito = int(input("¿Cuánto dinero desea depositar?: "))
cuenta.depositar(deposito)
retiro = int(input("¿Cuánto dinero desea rerirar?: "))
cuenta.retirar(retiro)
cuenta.calcular_interes()

print("Su saldo es ", round(cuenta.balance,2))