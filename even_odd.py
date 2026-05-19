# Even or Odd Checker
# Accept a number from the user, check whether it is even or odd, and display the result

# Prompt the user to enter a number and convert the input string to an integer
number = int(input("Enter a number: "))

# Check if the number is divisible by 2 with no remainder
if number % 2 == 0:
    # If the remainder is zero, the number is even
    print(f"{number} is even")
else:
    # Otherwise, the number is odd
    print(f"{number} is odd")
