class CuentaBancaria:

    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular=titular
        self.saldo=saldo
        
    def depositar(self,monto):
        self.saldo+=monto
        
    def retirar(self,monto):
        if self.saldo<monto:
            raise Exception("Saldo insuficiente")
        self.saldo-=monto
    def mostrar_datos(self):
        
        return F"Cuenta {self.numeroCuenta} -Titular {self.titular} - Saldo {self.saldo}"
    
