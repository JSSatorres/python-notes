# Introducción a Pandas

Pandas es una biblioteca de Python que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento. Está diseñada para facilitar la manipulación y el análisis de datos en Python.

## Instalación

Antes de comenzar a utilizar Pandas, debes asegurarte de tenerlo instalado en tu entorno. Puedes instalarlo ejecutando el siguiente comando en tu terminal:

```python
pip install pandas

```
## Importar Pandas

Una vez que Pandas esté instalado, puedes importarlo en tu script de Python utilizando la siguiente línea de código:

```python
import pandas as pd
```
## Estructuras de datos en Pandas

Pandas proporciona dos estructuras de datos principales: Series y DataFrame.

### Series
Una Serie es una estructura de datos unidimensional que puede contener cualquier tipo de datos. Puedes pensar en ella como una columna de una tabla. Para crear una Serie, puedes utilizar el siguiente código:

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])
```

### DataFrame
Un DataFrame es una estructura de datos bidimensional que puede contener columnas de diferentes tipos (numéricos, cadenas, booleanos, etc.). Puedes pensar en él como una tabla de datos. Para crear un DataFrame, puedes utilizar el siguiente código:

```python
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(data)
```

### DataFrame
Visualizar datos
Puedes utilizar el método head() para ver las primeras filas de un DataFrame:

```python
df.head()
```

### Selección de datos
Puedes seleccionar columnas específicas de un DataFrame utilizando la siguiente sintaxis:

```python
df['Nombre']

```

También puedes realizar selecciones basadas en condiciones lógicas:

```python
df[df['Edad'] > 30]
```

### Agregar datos
Puedes agregar una nueva columna a un DataFrame de la siguiente manera:

```python
df['Profesión'] = ['Ingeniero', 'Médico', 'Abogado', 'Profesor']
```

### Operaciones estadísticas
Pandas proporciona varios métodos para realizar operaciones estadísticas en los datos, como mean(), max(), min(), etc. Por ejemplo:

```python
df['Edad'].mean()

```
### Encontrar el elemento en la segunda fila y la primera columna

```python
element = df.iloc[1, 0]
```