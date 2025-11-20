
class datos:
    def __init__(self,nombre : str,edad : int,documento : int,ciudad : str,correo : str):
         
         self.nombre = nombre 
         self.edad = edad
         self.documento = documento
         self.ciudad = ciudad
         self.correo = correo
         
    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.documento}, {self.ciudad}, {self.correo}"

    

        


     

    