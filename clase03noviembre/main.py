
#from clases.circulo import Circulo

#circulo=Circulo(5)

#print (circulo.area())

from clases. cuentaBancaria import CuentaBancaria
CuentaBancaria=CuentaBancaria("123456","Lilian Labbe", 25000)
print (CuentaBancaria.mostrar_datos_datos())

CuentaBancaria.depositar(1000000)
print (CuentaBancaria.mostrar_datos())

CuentaBancaria.retirar(10000000)
