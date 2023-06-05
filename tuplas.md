# Tuplas en Python

En Python, una tupla es una secuencia inmutable de elementos separados por comas. Se utilizan para almacenar varios elementos relacionados. A diferencia de las listas, las tuplas no se pueden modificar una vez creadas, lo que significa que son inmutables.

## Creación de tuplas

Puedes crear una tupla en Python de las siguientes maneras:

1. Utilizando paréntesis y separando los elementos con comas:

```python
tupla1 = (1, 2, 3, 4, 5)
```

2. Utilizando la función `tuple()`:

```python
tupla2 = tuple(['a', 'b', 'c'])
```

3. O simplemente separando los elementos con comas:

```python
tupla3 = 'x', 'y', 'z'
```

## Acceso a elementos de una tupla

Puedes acceder a los elementos de una tupla utilizando la indexación. El índice comienza en 0 para el primer elemento y puedes usar números negativos para acceder a los elementos desde el final de la tupla.

```python
tupla = ('a', 'b', 'c', 'd', 'e')
print(tupla[0]) 
Output: 'a'
print(tupla[2]) 
Output: 'c'
print(tupla[-1])
Output: 'e'
```

## Métodos de tuplas

Aunque las tuplas son inmutables y no tienen muchos métodos, hay algunos que puedes utilizar:

- `count()`: Devuelve el número de veces que aparece un elemento en la tupla.

```python
tupla = (1, 2, 2, 3, 4, 2)
print(tupla.count(2)) 
Output: 3
```

- `index()`: Devuelve el índice de la primera aparición de un elemento en la tupla.

```python
tupla = ('a', 'b', 'c', 'b', 'd')
print(tupla.index('b')) 
Output: 1
```

## Iteración sobre una tupla

Puedes iterar sobre los elementos de una tupla utilizando un bucle `for`.

```python
tupla = ('apple', 'banana', 'cherry')
for elemento in tupla:
    print(elemento)
```

## Ventajas de las tuplas

- Son más eficientes que las listas en términos de rendimiento y uso de memoria.
- Pueden utilizarse como claves en diccionarios, ya que son inmutables.

Las tuplas son una estructura de datos útil cuando necesitas almacenar elementos inmutables que no cambiarán durante la ejecución del programa.
