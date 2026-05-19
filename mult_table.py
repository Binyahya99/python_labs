# Ask the user to enter a number for the multiplication table
number = int(input("Enter a number: "))
# Loop through values from 1 to 10 to create the table
for i in range(1, 11):
    # Calculate the product of the user's number and the current multiplier
    product = number * i
    # Print the multiplication result in a readable format
    print(f"{number} x {i} = {product}")
