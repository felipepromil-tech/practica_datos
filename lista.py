from datos import *


lista = []

nombre = (input("Ingrese su nombre:"))

documento = (input("ingrese su documento:"))

edad = (input("ingrese su edad:"))
ciudad = (input("Ingrese su ciudad:"))

correo = (input("Ingrese su correo:"))


date = (nombre,documento,edad,ciudad)

lista.append(date)


print (f"sus datos son : {date}")


