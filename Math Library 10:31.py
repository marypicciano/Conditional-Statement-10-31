import math

def calculate_factorial_and_sqrt(num_factorial, num_sqrt):

    factorial_result = math.factorial(num_factorial)
    sqrt_result = math.sqrt(num_sqrt)

    return {
        'factorial': factorial_result,
        'square_root': sqrt_result
    }

# Example usage
factorial_num = 5
sqrt_num = 16
results = calculate_factorial_and_sqrt(factorial_num, sqrt_num)
print(f"Factorial of {factorial_num}: {results['factorial']}")
print(f"Square root of {sqrt_num}: {results['square_root']}")
