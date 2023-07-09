# Función de Hipótesis, Función de Optimización y Función de Coste en Regresión Lineal

En el aprendizaje automático, la regresión lineal es un método comúnmente utilizado para predecir una variable dependiente continua a partir de una o más variables independientes. Para llevar a cabo este proceso, se utilizan diversas funciones y métricas. A continuación, se describen la función de hipótesis, la función de optimización, la función de error y la función de coste en el contexto de la regresión lineal.

## Función de Hipótesis
a función de hipótesis es un componente clave de la regresión lineal. En este contexto, se utiliza para modelar la relación entre las variables independientes (características) y la variable dependiente (valor a predecir). En la regresión lineal, la función de hipótesis se expresa como una ecuación lineal, que es una combinación lineal de las variables independientes.

La función de hipótesis para la regresión lineal se puede expresar de la siguiente manera:

scss

```python
h(x) = θ0 + θ1*x1 + θ2*x2 + ... + θn*xn

```

Donde:

`h(x)` es el valor predicho por la función hipótesis.
`θ0, θ1, θ2, ..., θn` son los parámetros del modelo que se estiman durante el entrenamiento.
`x1, x2, ..., xn` son los valores de las variables independientes (características).
El objetivo del entrenamiento en la regresión lineal es encontrar los mejores valores para los parámetros `θ0, θ1, θ2, ..., θn` que minimicen el error en las predicciones.


## Función de Coste

La función de coste es similar a la función de error y se utiliza para medir el rendimiento del modelo durante el entrenamiento. En la regresión lineal, la función de coste también se basa en el error cuadrático medio (MSE). La función de coste se define como el MSE, pero se agrega un término de regularización para penalizar modelos más complejos y evitar el sobreajuste.

La función de coste regularizada para la regresión lineal se expresa de la siguiente manera:

```python
Coste = (1/2n) * Σ(h(x) - y)^2 + λ * Σθi^2
```

Donde:

h(x) es el valor predicho por la función hipótesis.
y es el valor real de la variable dependiente correspondiente.
n es el número de ejemplos en el conjunto de datos.
λ es el parámetro de regularización.
θi son los parámetros del modelo.
El término de regularización penaliza los valores más grandes de los parámetros θi, lo que ayuda a controlar la complejidad del modelo.

En resumen, la función de hipótesis modela la relación entre las variables independientes y la variable dependiente, la función de optimización busca encontrar los mejores valores de los parámetros del modelo, la función de error mide la discrepancia entre las predicciones y los valores reales, y la función de coste agrega un término de regularización para controlar la complejidad del modelo. Estos conceptos son fundamentales en la regresión lineal y en muchos otros algoritmos de aprendizaje supervisado.

## Función de Optimización

La función de optimización se utiliza para encontrar los mejores valores de los parámetros del modelo que minimicen el error en las predicciones. En el caso de la regresión lineal, la función de optimización más comúnmente utilizada es el método de mínimos cuadrados.

El método de mínimos cuadrados busca minimizar la suma de los errores al cuadrado entre los valores predichos por la función hipótesis y los valores reales de la variable dependiente. Matemáticamente, esto se expresa como:

```python
min Σ(h(x) - y)^2  
```

Donde:

h(x) es el valor predicho por la función hipótesis.
y es el valor real de la variable dependiente correspondiente.
El objetivo es encontrar los valores de los parámetros θ0, θ1, θ2, ..., θn que minimicen esta función de optimización.