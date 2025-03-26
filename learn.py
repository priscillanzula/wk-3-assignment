'''
i = 1

while i < 6:
  print(i)
  i = i + 1
'''
'''
i = 1

while i < 6:
  
  i = i + 1
  print(i)
  ''' 
#nested loop
''' 
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)

'''
'''
Outer loop (for group in groups): Iterates over each sublist in the groups list.
Example: The first iteration picks ["Jobs", "Gates"], the second picks ["Newton", "Euclid"], and so on.
Inner loop (for name in group): Iterates over each name in the current sublist.
Example: For ["Jobs", "Gates"], it prints Jobs and then Gates.
Output: Prints each name in the nested lists, one at a time.

'''
''' 
numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)
'''
'''
or num in numbers: Iterates over each number in the numbers list.
if (num < 0): Checks if the current number is negative.
If a negative number is found, it prints "Negative number detected!" and exits the loop using break.
print(num): Prints the number if it is not negative
'''

  #continue
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)