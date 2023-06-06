# Métodos para cadenas en Python

A continuación se presentan algunos métodos comunes para cadenas en Python, junto con una breve explicación y ejemplos de código.

## `upper()`
~~~
Creando códigos de bloque.
Puedes añadir tantas líneas y párrafos como quieras.  
~~~
Convierte todos los caracteres de una cadena a mayúsculas.

```python
text = "hello world"
upper_text = text.upper()
Resultado: "HELLO WORLD"
```


## `lower()`

Convierte todos los caracteres de una cadena a mayúsculas.

```python
text = "HELLO WORLD"
upper_text = text.lower()
Resultado: "hello world"
```
## `strip()`

Elimina los espacios en blanco al principio y al final de una cadena.

```python
text = "   hello world   "
stripped_text = text.strip()
Resultado: "hello world"
```

## `split()`

Divide una cadena en una lista de subcadenas utilizando un delimitador.

```python
text = "apple,banana,orange"
fruits = text.split(",")
Resultado: ['apple', 'banana', 'orange']
```
## `join()`

Une una lista de cadenas en una sola cadena utilizando un separador.

```python
fruits = ['apple', 'banana', 'orange']
text = ",".join(fruits)
Resultado: "apple,banana,orange"
```

# Acceder a todos los elementos de la lista
my_list[:]

# Acceder a los elementos del índice 3 hasta el final
my_list[3:]

# Acceder a los elementos con un paso de 2
my_list[::2]

# Acceder a los elementos en orden inverso
my_list[::-1]