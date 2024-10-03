# Definimos una clase padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal", self.especie ,"del tipo", type(self).__name__)


# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    def __init__(self, especie, edad, dueño="nadie"):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño

    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


print("clase padre de Perro",Perro.__bases__)
print("clases hijas de Animal",Animal.__subclasses__())

mi_perro = Perro('mamífero', 10,"Mario")
mi_perro.describeme()
print("el dueño es",mi_perro.dueño)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)
mi_abeja.describeme()

mi_perro.hablar()
mi_vaca.hablar()
mi_abeja.hablar()

mi_vaca.describeme()
mi_abeja.describeme()
mi_abeja.picar()

#-----------------------------------------------------
#    HERENCIA MULTIPLE
#-----------------------------------------------------

class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass
class Clase4(Clase2, Clase1):
    pass

print("en herencia multiple sigue un orden dado por MRO (Method Order Resolution)",Clase3.__mro__)
print(Clase4.__mro__)

