# Listas en Python

En Python, una `lista es una estructura de datos ***mutable*** que permite almacenar una ***colección ordenada*** de elementos. A diferencia de las tuplas, las listas pueden modificarse una vez creadas, lo que las hace muy flexibles`.

## Creación de listas

Puedes crear una lista en Python de las siguientes maneras:

1. Utilizando corchetes y separando los elementos con comas:

```python
lista1 = [1, 2, 3, 4, 5]
```

2. Utilizando la función `list()`:

```python
lista2 = list(['a', 'b', 'c'])
```

3. O simplemente separando los elementos con comas:

```python
lista3 = 'x', 'y', 'z'
```

## Acceso a elementos de una lista

Puedes acceder a los elementos de una lista utilizando la indexación. El índice comienza en 0 para el primer elemento y puedes usar números negativos para acceder a los elementos desde el final de la lista.

```python
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[0]) 
Output: 'a'
print(lista[2]) 
Output: 'c'
print(lista[-1])
Output: 'e'
```

## Métodos de listas

Las listas en Python vienen con una variedad de métodos incorporados que permiten realizar diversas operaciones en ellas. Aquí tienes algunos ejemplos:

- `append()`: Agrega un elemento al final de la lista.

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)
Output: [1, 2, 3, 4]
```

- `insert()`: Inserta un elemento en una posición específica de la lista.

```python
lista = ['a', 'b', 'c']
lista.insert(1, 'x')
print(lista)
Output: ['a', 'x', 'b', 'c']
```

- `remove()`: Elimina la primera aparición de un elemento de la lista.

```python
lista = ['apple', 'banana', 'cherry']
lista.remove('banana')
print(lista)    # Output: ['apple', 'cherry']
```

- `pop()`: Elimina y devuelve el último elemento de la lista.

```python
lista = [1, 2, 3, 4]
elemento = lista.pop()
print(elemento)
Output: 4
print(lista)
Output: [1, 2, 3]
```

- `count()`: Devuelve el número de veces que aparece un elemento en la lista.

```python
lista = [1, 2, 2, 3, 4, 2]
print(lista.count(2))
Output: 3
```

- `index()`: Devuelve el índice de la primera aparición de un elemento en la lista.

```python
lista = ['a', 'b', 'c', 'b', 'd']
print(lista.index('b'))
Output: 1
```

## Iteración sobre una lista

Puedes iterar sobre los elementos de una lista utilizando un bucle `for`.

```python
lista = ['apple', 'banana', 'cherry']
for elemento in lista:
    print(elemento)
```

## Ventajas de las listas

- Son estructuras de datos flexibles que pueden modificarse.
- Permiten almacenar y manipular colecciones de elementos de manera eficiente.

Las listas son una herramienta poderosa en Python para manejar conjuntos de datos y realizar diversas operaciones en ellos.
