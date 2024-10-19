def sqrt(number):
    """
    Calculate the floored square root of a number using binary search.
    
    Args:
       number(int): Number to find the floored square root of.
    Returns:
       int: Floored Square Root.
    """
    # Edge case: Square root of 0 or 1 is the number itself.
    if number < 2:
        return number
    
    # Initialize the binary search boundaries
    low, high = 1, number
    
    # We are looking for the largest integer whose square is <= number
    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        mid_squared = mid * mid
        
        if mid_squared == number:
            return mid  # Exact square root found
        elif mid_squared < number:
            low = mid + 1  # Move the lower boundary up
            result = mid   # Store the result as a potential answer
        else:
            high = mid - 1  # Move the upper boundary down
    
    # At the end of the loop, 'result' will hold the floored square root
    return result

# Test cases
print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(27) else "Fail")
