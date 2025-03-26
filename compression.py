 # List comprehension
squares = [x**2 for x in range(5)]
print(squares)  

#Using Conditions in List Comprehensions
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

#Nested List Comprehensions

# Create a 3x3 matrix using nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
'''
Outer List Comprehension (for i in range(1, 4)):

This loop iterates over the values i = 1, 2, 3.
For each value of i, it creates a sublist (row) using the inner list comprehension.
Inner List Comprehension (for j in range(1, 4)):

This loop iterates over the values j = 1, 2, 3.
For each value of j, it calculates the product i * j and adds it to the current sublist.
Result:

For i = 1, the inner loop calculates [1*1, 1*2, 1*3] → [1, 2, 3].
For i = 2, the inner loop calculates [2*1, 2*2, 2*3] → [2, 4, 6].
For i = 3, the inner loop calculates [3*1, 3*2, 3*3] → [3, 6, 9].


'''
names = ["Alice", "Bob", "Charlie"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)  

numbers = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)