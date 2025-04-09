from calculator import add, subtract, multiply, divide, calculate

def test_normal_usage():
    """Test calculator with normal number inputs."""
    print("\n=== Testing with normal number inputs ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")
    print(f"calculate('multiply', 8, 9) = {calculate('multiply', 8, 9)}")

def test_string_numbers():
    """Test calculator with string numbers to reveal the bug."""
    print("\n=== Testing with string number inputs (reveals the bug) ===")
    try:
        result = add("5", "3")
        print(f'"5" + "3" = {result} (Expected: 8, Got: {result})')
    except Exception as e:
        print(f'Error in add("5", "3"): {e}')
    
    try:
        result = subtract("10", "4")
        print(f'"10" - "4" = {result} (Expected: 6, Got: {result})')
    except Exception as e:
        print(f'Error in subtract("10", "4"): {e}')
    
    try:
        result = calculate("add", "7", "2")
        print(f'calculate("add", "7", "2") = {result} (Expected: 9, Got: {result})')
    except Exception as e:
        print(f'Error in calculate("add", "7", "2"): {e}')

def test_mixed_inputs():
    """Test calculator with mixed number types."""
    print("\n=== Testing with mixed input types ===")
    try:
        result = add(5, "3")
        print(f'5 + "3" = {result} (Expected: 8, Got: {result})')
    except Exception as e:
        print(f'Error in add(5, "3"): {e}')

if __name__ == "__main__":
    print("CALCULATOR TEST RESULTS")
    print("======================")
    
    test_normal_usage()
    test_string_numbers()
    test_mixed_inputs()
