#introduccion a POO
#representar un grupo de __animales__ que nos permita alimentar y _pasear_ unas __mascotas__
#puede ser __perros__ y __gatos__, cada mascota debe tener definido un __nombre__ y __raza__


class animal(object):
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    def pasear(self):
        pass
    def alimentar(self):
        pass
    def dar_info(self):
        return self.nombre + " de raza: " + self.raza + self.propietario
class mascota(animal):
    def __init__ (self,nombre,raza,propietario):
        super.__init__(self, nombre,raza)
        self.propietario=propietario
class gato(mascota):
    def pasear(self):
        print("paseando al gato")
    def alimentar(self):
        print("alimentando al gato ")
    def dar_info(self):
        print(self.nombre + " de raza: " + self.raza + self.propietario)
class perro(mascota):
    def pasear(self):
        print("paseando al perro")
    def alimentar(self):
        print("alimentando al perro")
    def dar_info(self):
        print(self.nombre + " de raza: " + self.raza + self.propietario)
class lagarto(mascota):
    def pasear(self):
        print("paseando al lagarto")
    def alimentar(self):
        print("alimentando al lagarto")
    def dar_info(self):
        print(self.nombre + " de raza: " + self.raza + self.propietario)

if __name__ == '__main__':
    mascotas=[perro("neron","bulldog", "juan"),gato("lucas","angora", "maria"),lagarto("coco","camaleon", "pepe")]
    for m in mascotas:
        m.pasear()
        m.alimentar()
        m.dar_info()

        
