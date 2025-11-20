
from datos import *


print("menu principal")
print("1. Consulta de personas")
print("2. Agregar personas ")
print("3. salida")




class Menu:

    def __init__(self):
      self.lista = []

    def agregar (self,nombre,edad,documento,ciudad,correo):
      self.personas = datos(nombre,edad,documento,ciudad,correo)
      self.lista.append(self.personas)

    def consultar (self):
      if self.lista:
       print("las personas en la lista son:")
        
      for persona in self.lista:
       print (f"las personas que hay son:{persona}")
      else:
        print("no hay personas")

def menu():
  menu = Menu()
  while True:
    
    opcion = input("elija una opcion:")

    if opcion == "1":
      menu.consultar()
      

    elif opcion == "2":
     nombre = str(input("ingrese su nombre:"))
     edad = int(input("ingrese su edad:"))
     documento = int(input("ingrese su documento:"))
     ciudad = str(input ("ingrese su ciudad:"))
     correo = str(input("ingrese su correo:"))
     menu.agregar(nombre,edad,documento,ciudad,correo)
     

    elif opcion == "3":
     print("gracias por su colaboracion")
     return
    else:
      print("Error intente de nuevo")


if __name__ == "__main__":
  menu()
      


    

    
        
