#Create a function named large_power() 
# that takes two parameters named base and exponent.

#If base raised to the exponent is greater than 5000, 
# return True, otherwise return False

def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False
    
print(large_power(2, 13))
#Create a function called divisible_by_ten() that has one parameter named num.

#The function should return True if num is divisible by 10, 
# and False otherwise. 
#Consider using modulo operator % to check for divisibility.


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_ten(20))


