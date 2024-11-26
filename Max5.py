# Step 1: Prompt the user to enter five numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

# Step 2: Calculate the sum of the numbers
total_sum = num1 + num2 + num3 + num4 + num5

# Step 3: Calculate the average
average = total_sum / 5

# Step 4: Display the result
print(f"The average of the five numbers is: {average}")
