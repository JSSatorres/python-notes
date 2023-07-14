# Regresión Lineal en Python para Machine Learning

La regresión lineal es una técnica popular en el campo del machine learning para modelar y predecir relaciones lineales entre variables. En Python, podemos utilizar diversas bibliotecas para implementar la regresión lineal, siendo una de las más comunes scikit-learn. A continuación, se muestra un ejemplo de cómo usar esta biblioteca para realizar una regresión lineal.

## Paso 1: Importar las bibliotecas necesarias

Primero, debemos importar las bibliotecas necesarias. En este caso, utilizaremos numpy para el manejo de arrays y sklearn para realizar la regresión lineal.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

```
## Paso 2: Preparar los datos de entrenamiento

A continuación, debemos preparar nuestros datos de entrenamiento. Supongamos que tenemos dos variables: X, que representa la variable independiente, y que representa la variable dependiente. Necesitamos organizar estos datos en forma de arrays de numpy.

```python
X = np.array([[1], [2], [3], [4], [5]])  # Variable independiente
y = np.array([2, 3.5, 4.5, 6, 7])        # Variable dependiente
```

## Paso 3: Crear y entrenar el modelo

Ahora, crearemos una instancia del modelo de regresión lineal y lo entrenaremos utilizando nuestros datos de entrenamiento.

```python
model = LinearRegression()  # Crear una instancia del modelo
model.fit(X, y)             # Entrenar el modelo con los datos de entrenamiento      
```

## Paso 4: Realizar predicciones

Una vez que el modelo ha sido entrenado, podemos utilizarlo para hacer predicciones sobre nuevos datos. Supongamos que queremos predecir el valor de y para un valor de X dado, por ejemplo, X = 6.

```python
X_new = np.array([[6]])  # Nuevo valor de X para la predicción
y_pred = model.predict(X_new)  # Realizar la predicción
print(y_pred)  # Imprimir el resultado de la predicción   
```


## Paso 5: Evaluar el modelo

Finalmente, podemos evaluar el rendimiento del modelo utilizando métricas como el error cuadrático medio (MSE) o el coeficiente de determinación (R^2).

```python
y_pred_train = model.predict(X)  # Predicciones en los datos de entrenamiento
mse = np.mean((y_pred_train - y) ** 2)  # Calcular el error cuadrático medio
r2 = model.score(X, y)  # Calcular el coeficiente de determinación
print("MSE:", mse)
print("R^2:", r2)  
```