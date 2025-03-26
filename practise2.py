# Example of a basic if statement
#temperature = 30

#if temperature > 25:
   # print("It's a hot day!")

''' 
    # Example of an if-else statement
temperature = 20

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's a cool day!")


    # Example of an if...elif...else statement
temperature = 15

if temperature > 25:
    print("It's a hot day!")
elif temperature > 15:
    print("It's a warm day!")
else:
    print("It's a cold day!")

''' 
''' 
    #Write an if/elif/else statement for a college with a grading system as shown below:

#If grade is 90 or higher, print "A"
#Else if grade is 80 or higher, print "B"
#Else if grade is 70 or higher, print "C"
#Else if grade is 60 or higher, print "D"
#Else, print "F"
grade= int(input("Enter your grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


    #Write an if/elif/else statement for a college with a grading system as shown below:'
    '''
#Programming languages like Python implement two types of iteration:

#Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
#Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).
## Example of a for loop with range
for number in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {number}")

    #While Loops

#A while loop performs a set of instructions as long as a given condition is true.
# Example of a while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter


    
    #break
    #continue
    #Loop controls are statements that change the execution flow of a loop from its normal sequence.
    #The break statement is used to terminate the loop immediately when it is encountered.
    # Example of loop controls: break and continue
for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")

    #Explanation:
#break: Stops the loop entirely when number == 5.
#continue: Skips the current iteration when number is even and moves to the next loop iteration.
#The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration
#Nested Loops
# Example of a nested loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")