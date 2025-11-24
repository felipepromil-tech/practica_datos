from datos import *


print("menu principal")
print("1. Consulta de personas")
print("2. Agregar personas ")
print("3. Editar persona por documento")
print("4. Eliminar persona por documento")
print("5. salida")



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

    # ============================
    #   OPCIÓN NUEVA: EDITAR
    # ============================
    def editar(self, documento):
        for persona in self.lista:
            if str(persona.documento) == str(documento):
                print("EDITAR DATOS:")

                nuevo_nombre = input("Nuevo nombre: ")
                nueva_edad = input("Nueva edad: ")
                nueva_ciudad = input("Nueva ciudad: ")
                nuevo_correo = input("Nuevo correo: ")

                if nuevo_nombre != "":
                    persona.nombre = nuevo_nombre
                if nueva_edad != "":
                    persona.edad = nueva_edad
                if nueva_ciudad != "":
                    persona.ciudad = nueva_ciudad
                if nuevo_correo != "":
                    persona.correo = nuevo_correo

                print("Persona editada.")
                return

        print("No se encontró la persona")

    # ============================
    #   OPCIÓN NUEVA: ELIMINAR
    # ============================
    def eliminar(self, documento):
        for persona in self.lista:
            if str(persona.documento) == str(documento):
                self.lista.remove(persona)
                print("Persona eliminada.")
                return
        print("No se encontró la persona.")



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

    # ============================
    # OPCIÓN NUEVA EDITAR
    # ============================
    elif opcion == "3":
        doc = input("Documento a editar:")
        menu.editar(doc)

    # ============================
    # OPCIÓN NUEVA ELIMINAR
    # ============================
    elif opcion == "4":
        doc = input("Documento a eliminar:")
        menu.eliminar(doc)

    elif opcion == "5":
        print("saliendo...")
        break


if __name__ == "__main__":
  menu()
      


    

    
        
