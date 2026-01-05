# Function to XOR all binary digits in a string
def X_long_algoryhtm(s):
    from functools import reduce
    from operator import xor
    return reduce(xor, map(int, s.split()))

def X_code_golf(s):return s.count('1')%2

# Test cases
if __name__ == "__main__":
    test_cases = [
        "1 0 0 1 0",
        "1 0 1 1 1 0 0 1 0 0 0 0",
        "0 0 0 0",
        "1 1 1 1 1",
        "1 0 1 0 1 0 1"
    ]
    
    for t in test_cases:
        print(f"X('{t}') = {X(t)}")


