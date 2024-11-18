def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    # Get input from user
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
