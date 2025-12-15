def add(a, b): 
    return a + b 
def divide(a, b): 
    if b == 0: 
        raise ValueError("Деление на ноль невозможно") 
    return a / b 
def multiply(a, b): 
    return a * b 
def subtract(a, b): 
    return a - b 
print(add(7.5, 2.5))