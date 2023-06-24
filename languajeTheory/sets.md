# Conjuntos (Sets) en Python

En Python, un conjunto es una ***colección desordenada de elementos únicos***. Los conjuntos se utilizan para almacenar múltiples elementos sin un orden específico y garantizan que no haya duplicados.

## Creación de conjuntos

Puedes crear un conjunto en Python de las siguientes maneras:

1. Utilizando llaves `{}`:

```python
conjunto1 = {1, 2, 3, 4, 5}
```

2. Utilizando la función `set()`:

```python
conjunto2 = set(['a', 'b', 'c'])
```

## Acceso a elementos de un conjunto

Los sets en Python no admiten indexación, ya que no tienen un orden específico. No puedes acceder a elementos individuales directamente desde un conjunto.

## Operaciones con sets

Los sets en Python admiten varias operaciones útiles, como la unión, la intersección y la diferencia.

- Unión de sets: Devuelve un nuevo conjunto que contiene todos los elementos de los sets originales sin duplicados.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print(union)
Output: {1, 2, 3, 4, 5}
```

- Intersección de sets: Devuelve un nuevo conjunto que contiene solo los elementos que están presentes en ambos sets.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1 & conjunto2
print(interseccion)
Output: {3}
```

- Diferencia de sets: Devuelve un nuevo conjunto que contiene los elementos presentes en el primer conjunto pero no en el segundo.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto1 - conjunto2
print(diferencia)
Output: {1, 2}
```

## Métodos de sets

Los sets en Python vienen con varios métodos incorporados que permiten realizar diversas operaciones en ellos. Aquí tienes algunos ejemplos:

- `add()`: Agrega un elemento al conjunto.

```python
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)
 Output: {1, 2, 3, 4}
```

- `remove()`: Elimina un elemento del conjunto. Si el elemento no existe, se producirá un error.

```python
conjunto = {1, 2, 3}
conjunto.remove(2)
print(conjunto)
Output: {1, 3}
```

- `discard()`: Elimina un elemento del conjunto. Si el elemento no existe, no se producirá ningún error.

```python
conjunto = {1, 2, 3}
conjunto.discard(2)
print(conjunto)
Output: {1, 3}
```

- `union()`: Devuelve un nuevo conjunto que es la unión de dos sets.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
print(union)
Output: {1, 2, 3, 4, 5}
```

- `intersection()`: Devuelve un nuevo conjunto que es la intersección de dos sets.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
Output: {3}
```

- `difference()`: Devuelve un nuevo conjunto que es la diferencia entre dos sets.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto1.difference(conjunto2)
print(diferencia)
Output: {1, 2}
```

- `clear()`: Elimina todos los elementos del conjunto.

```python
conjunto = {1, 2, 3}
conjunto.clear()
print(conjunto) 
Output: set()
```

## Iteración sobre un conjunto

Puedes iterar sobre los elementos de un conjunto utilizando un bucle `for`.

```python
conjunto = {1, 2, 3}
for elemento in conjunto:
    print(elemento)
```

