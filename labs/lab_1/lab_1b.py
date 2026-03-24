"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def req_sanitized_num(inputString: str) -> float:
    '''
    Function that requests and sanitizes user input.
    This function is BLOCKING.

    params: inputString (string)
    returns: number (float) -> the sanitized number
    '''
    while True:
        try:
            number = float(input(inputString))
            return number
        except ValueError:
            print("Input cannot be used. Please enter a valid number.")

def ensureOption(prompt: str, options: list[str]) -> str:
    '''
    Guarantees a valid option of given options.
    '''
    while True:
        inputOption = input(prompt).strip().lower()
        if inputOption in options:
            return inputOption
        else:
            print(f"Invalid option. Please use a valid option of {options}")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = req_sanitized_num("Enter the first number: ")
    num2 = req_sanitized_num("Enter the second number: ")
    operation = ensureOption("Enter the operation (add, subtract, multiply, divide): ", ["add","subtract","multiply","divide"])

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
