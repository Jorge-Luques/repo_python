
#ejemplos del Libro de pthon

# Creando una clase Perro
class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

# Creamos un objeto de la clase perro
"""
mi_perro = Perro("Tobias","caniche")
print(type(mi_perro))
print(mi_perro.nombre) 
print(mi_perro.raza)
print(Perro.especie)
mi_perro.ladra()
mi_perro.camina(10) """
#----------------------------------------------------
class Clase:
    def metodo(self):
        return 'Método normal', self
    
    def metodoInstancia(self):
        return "-Caracteristicas de Metodo Instancia-\n* Pueden acceder y modificar los atributos del objeto.\n* Pueden acceder a otros métodos.\n* Dado que desde el objeto self se puede acceder a la clase con ` self.class`, también pueden modificar el estado de la clase"

    @classmethod
    def metododeclase(cls):
        return "-Caracteristicas de Método de Clase-\n* No pueden acceder a los atributos de la instancia.\n* Pero si pueden modificar los atributos de la clase."

    @staticmethod
    def metodoestatico():
        return "-Caracteristicas de Método Estático-\n* Los métodos estáticos se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase concreta."

miClase = Clase()
print(miClase.metodoInstancia())

print(" con metodos de clase")
x = Clase.metododeclase()
print(x)
print("con instancia...",miClase.metododeclase())

print(" con metodos estaticos")
print(Clase.metodoestatico())
print("con instancia...",miClase.metodoestatico())
