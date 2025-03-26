#Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
#If the discount is 20% or higher, apply the discount; otherwise, return the original price.

#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
#Print the final price after applying the discount, or if no discount was applied, print the original price.


def calculate_discount(price, discount_percent):
     # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price and return it
        return price - (price * discount_percent / 100)
    else:
         # If the discount is less than 20%, return the original price
        return price
    
print(calculate_discount(100, 15))


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price
    
# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
