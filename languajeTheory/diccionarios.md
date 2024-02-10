# Diccionarios en Python

En Python, un diccionario es `una estructura de datos que permite almacenar pares clave-valor`. Cada clave del diccionario se asocia con un valor, y puedes acceder a los valores utilizando sus claves. Los diccionarios son útiles cuando necesitas almacenar y recuperar datos de forma eficiente utilizando una clave personalizada.

## Creación de diccionarios

Puedes crear un diccionario en Python de las siguientes maneras:

1. Utilizando llaves `{}` y separando los pares clave-valor con dos puntos `:`:

```python
diccionario1 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

2. Utilizando la función `dict()` y pasando una lista de tuplas clave-valor:

```python
diccionario2 = dict([("nombre", "María"), ("edad", 25), ("ciudad", "Barcelona")])
```

2.Crear una lista de dicionarios

```python
personas = [
    {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Juan Luis", "edad": 40, "ciudad": "Linares"}
]
```
## Acceso a elementos de un diccionario

Puedes acceder a los valores de un diccionario utilizando sus claves. Para acceder a un valor específico, simplemente utiliza la clave entre corchetes `[]` o el método `get()` del diccionario.

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(diccionario["nombre"])
Output: "Juan"
print(diccionario.get("edad"))
Output: 30
```

## Métodos de diccionarios

Los diccionarios en Python vienen con una variedad de métodos incorporados que permiten realizar diversas operaciones en ellos. Aquí tienes algunos ejemplos:

- `keys()`: Devuelve una lista de todas las claves del diccionario.

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
claves = diccionario.keys()
print(claves)
Output: ["nombre", "edad", "ciudad"]
```

- `values()`: Devuelve una lista de todos los valores del diccionario.

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
valores = diccionario.values()
print(valores)
Output: ["Juan", 30, "Madrid"]
```

- `items()`: Devuelve una lista de tuplas clave-valor del diccionario.

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
items = diccionario.items()
print(items)
Output: [("nombre", "Juan"), ("edad", 30), ("ciudad", "Madrid")]
```

- `update()`: Actualiza el diccionario con pares clave-valor de otro diccionario o una lista de tuplas clave-valor.

```python
diccionario = {"nombre": "Juan", "edad": 30}
diccionario.update({"ciudad": "Madrid"})
print(diccionario) 
Output: {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

## Iteración sobre un diccionario

Puedes iterar sobre las claves o los valores de un diccionario utilizando un bucle `for`.

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave in diccionario:
    print(clave, diccionario[clave])
```

Los diccionarios son una estructura de datos poderosa en Python que te permite almacenar y acceder a valores utilizando claves personalizadas. Son útiles para manejar datos estructurados y realizar operaciones de búsqueda eficientes.```
