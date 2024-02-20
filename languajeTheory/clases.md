# Clases en Python



En Python, las clases se definen utilizando la palabra clave `class` seguida del nombre de la clase. Los constructores se definen dentro de una clase utilizando el método especial `__init__()`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

En el ejemplo anterior, creamos la clase Persona con un constructor que toma dos parámetros: nombre y edad. Dentro del constructor, asignamos los valores pasados como argumentos a los atributos self.nombre y self.edad.

Para crear una instancia de la clase Persona y acceder a sus atributos y métodos, podemos hacer lo siguiente:

```python
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos y métodos de la instancia
print(persona1.nombre)  # Juan
print(persona1.edad)    # 30
persona1.saludar()       # Hola, mi nombre es Juan y tengo 30 años.
```
En el ejemplo anterior, creamos una instancia de la clase Persona llamada persona1 con el nombre "Juan" y la edad 30. Luego, accedemos a los atributos nombre y edad utilizando la sintaxis instancia.atributo. Además, llamamos al método saludar() de la instancia persona1, que muestra un mensaje en la consola.


## metodos


```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def aumentar_edad(self, cantidad):
        self.edad += cantidad
    
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

        def cambiar_nombre(self, nuevo_nombre):
            self.nombre = nuevo_nombre

        def aumentar_edad(self, cantidad):
            self.edad += cantidad

        def numero_de_hijos(self, cantidad=2):
            print(f"Tengo {cantidad} hijos.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos y métodos de la instancia
print(persona1.nombre)     # Juan
print(persona1.edad)       # 30
persona1.saludar()          # Hola, mi nombre es Juan y tengo 30 años.

persona1.cambiar_nombre("Carlos")
persona1.aumentar_edad(5)

print(persona1.nombre)     # Carlos
print(persona1.edad)       # 35
persona1.saludar()          # Hola, mi nombre es Carlos y tengo 35 años.
```

