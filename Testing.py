# Simple Calculator Program

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    print("Welcome to the Simple Calculator!")
    
    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display result in the specified format
    if isinstance(result, str):
        print(result)  # Print error message if any
    else:
        print(f"{num1} {operation} {num2} = {result}")

# Run the program
if __name__ == "__main__":
    main()
    