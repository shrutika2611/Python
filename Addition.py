def sum_of_numbers():
    try:
        # Ask the user how many numbers they want to sum
        n = int(input("How many numbers do you want to add? "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize a list to store the numbers
        numbers = []

        # Collect the numbers from the user
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)

        # Calculate the sum of the numbers
        total = sum(numbers)

        # Display the result
        print(f"The sum of the {n} numbers is: {total}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Call the function
sum_of_numbers()
