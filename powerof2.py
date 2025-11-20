def check_power_of_2(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    
    if n == 0:
        return False
    
    return (n & (n - 1)) == 0


# --------------------- User Input ----------------------

try:
    num = int(input("Enter an integer: "))
    if check_power_of_2(num):
        print(f"{num} is a power of 2")
    else:
        print(f"{num} is NOT a power of 2")
except ValueError as e:
    print(f"Exception: {e}")
