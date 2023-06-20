# Bucles en Python

Los bucles son estructuras de control que permiten repetir un bloque de código varias veces. En Python, hay dos tipos principales de bucles: el bucle `while` y el bucle `for`.

## Bucle while

El bucle `while` se utiliza para repetir un bloque de código mientras se cumpla una condición.

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

En el ejemplo anterior, el bucle while imprimirá los números del 0 al 4. La variable i se inicializa en 0 y se incrementa en 1 en cada iteración hasta que la condición i < 5 se vuelva falsa.

## Bucle for

El loop for se utiliza cuando se conoce la cantidad exacta de iteraciones que se deben realizar. Se utiliza principalmente para iterar sobre una secuencia de elementos, como una lista o una cadena de texto.

Ejemplo de un loop for que itera sobre una lista e imprime cada elemento:

```python
frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(fruta)
```

En el ejemplo anterior, el bucle while imprimirá los números del 0 al 4. La variable i se inicializa en 0 y se incrementa en 1 en cada iteración hasta que la condición i < 5 se vuelva falsa.