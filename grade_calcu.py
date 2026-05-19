# Student Grade Calculator Program
# This program accepts marks from 0-100 and displays corresponding letter grades

# Prompt user to enter marks between 0 and 100
marks = int(input("Enter your marks (0-100): "))

# Validate that the input is within the acceptable range
if marks < 0 or marks > 100:
    print("Invalid input! Please enter marks between 0 and 100.")
# Check if marks fall in the A grade range (80-100)
elif marks >= 80:
    print(f"Your grade is: A")
# Check if marks fall in the B grade range (70-79)
elif marks >= 70:
    print(f"Your grade is: B")
# Check if marks fall in the C grade range (60-69)
elif marks >= 60:
    print(f"Your grade is: C")
# Check if marks fall in the D grade range (50-59)
elif marks >= 50:
    print(f"Your grade is: D")
# If marks are below 50, assign F grade
else:
    print(f"Your grade is: F")
