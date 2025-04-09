def is_number(value):
    """Check if a value is a number (int, float) or can be converted to one."""
    if isinstance(value, (int, float)):
        return True
    
    # Try to convert string to number
    if isinstance(value, str):
        try:
            float(value)
            return True
        except ValueError:
            pass
    
    return False

def validate_inputs(a, b, operation=None):
    """Validate that inputs are numbers and operation is supported.
    
    Args:
        a: First number
        b: Second number
        operation: Optional operation to validate
        
    Returns:
        True if all validations pass
        
    Raises:
        TypeError: If a or b are not numbers
        ValueError: If operation is not supported
    """
    if not is_number(a) or not is_number(b):
        raise TypeError("Inputs must be numbers")
    
    if operation is not None:
        valid_operations = ["add", "subtract", "multiply", "divide"]
        if operation not in valid_operations:
            raise ValueError(f"Operation must be one of: {', '.join(valid_operations)}")
    
    return True
