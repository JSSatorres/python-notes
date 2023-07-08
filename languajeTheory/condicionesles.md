# Ejemplos en Python

## Estructura condicional if, elif, else

La estructura condicional if se utiliza para `ejecutar un bloque de código si se cumple una condición`. La estructura `elif` se utiliza para comprobar condiciones adicionales.

```python
a = 10

if a > 0:
    print("a es mayor que cero")
elif a == 0:
    print("a es igual a cero")
else:
    print("a es menor que cero")
```

## Operadores lógicos (not, and, or)

Los operadores lógicos not, and y or se utilizan para combinar expresiones lógicas.

```python
a = True
b = False

if not a:
    print("a es False")  # No se imprime
else:
    print("a es True")

if a and b:
    print("Ambas condiciones son True")  # No se imprime
else:
    print("Al menos una condición es False")

if a or b:
    print("Al menos una condición es True")  # Se imprime
else:
    print("Ambas condiciones son False")

a = 10

if a > 0:
    print("a es mayor que cero")
elif a == 0:
    print("a es igual a cero")
else:
    print("a es menor que cero")

b = 5

if b > 0 and b < 10:
    print("b es mayor que cero y menor que diez")

c = 15

if c < 0 or c > 100:
    print("c es menor que cero o mayor que cien")

d = 20

if not d == 10:
    print("d no es igual a diez")
```