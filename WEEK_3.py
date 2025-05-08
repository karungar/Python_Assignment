# This function calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        
        # Subtract the discount from the original price
        final_price = price - discount_amount
        
        # Return the discounted price
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Ask the user for the original price
print("Welcome to the Discount Calculator!")
original_price = float(input("Enter the original price of the item: $"))

# Ask the user for the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call our function to calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Check if a discount was applied
if discount_percent >= 20:
    print(f"A {discount_percent}% discount has been applied!")
    print(f"Original price: ${original_price:.2f}")
    
    # Calculate how much money was saved
    saved_amount = original_price - final_price
    print(f"You saved: ${saved_amount:.2f}")
    
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount was applied because the discount")
    print(f"percentage ({discount_percent}%) is less than 20%.")
    print(f"Price remains: ${final_price:.2f}")

print("-" * 30)  # Print a closing divider line
print("Thank you for using the Discount Calculator!")