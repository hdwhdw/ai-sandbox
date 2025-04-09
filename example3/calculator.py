from utils import validate_inputs

def add(a, b):
    """Add two numbers and return the result."""
    validate_inputs(a, b)
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    validate_inputs(a, b)
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    validate_inputs(a, b)
    return a * b

def divide(a, b):
    """Divide a by b and return the result."""
    validate_inputs(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(operation, a, b):
    """Perform the specified operation on a and b.
    
    Args:
        operation: String representing the operation ('add', 'subtract', 'multiply', 'divide')
        a: First number
        b: Second number
        
    Returns:
        Result of the operation
    """
    # Validate the operation
    validate_inputs(a, b, operation)
    
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")
