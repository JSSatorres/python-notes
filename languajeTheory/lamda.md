# Lambda Funcion en Python

Lambda functions, also known as anonymous functions, are a concise way to define small, one-line functions in Python. They are commonly used when a function is needed for a short period of time and doesn't require a formal definition.

## Sintaxis

La sintaxis para una función lambda es la siguiente:

```python
# Example 1: Basic lambda function
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2: Sorting a list of tuples based on the second element
students = [('Alice', 23), ('Bob', 19), ('Charlie', 21)]
students.sort(key=lambda x: x[1])
print(students)  # Output: [('Bob', 19), ('Charlie', 21), ('Alice', 23)]

# Example 3: Filtering a list using lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

