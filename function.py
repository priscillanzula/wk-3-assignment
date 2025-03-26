'''
syntax:

def function_name(parameters):
    """Optional docstring explaining the function."""
    # Code block
    return value  
'''

'''
# Function definition
def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))

'''
#1. Positional Arguments:
def add(a, b):
    return a + b

print(add(3, 5))

#2. Default Arguments:
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) 
print(greet("Alice"))
#3. Keyword Arguments:
def introduce(name, age):
     return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob")) 

#A function can return values using the return statement.

def square(number):
    return number ** 2

result = square(4)
print(result)  

# Lambda function for adding two numbers
add = lambda x, y: x + y
print(add(3, 5))  

# Using lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)

