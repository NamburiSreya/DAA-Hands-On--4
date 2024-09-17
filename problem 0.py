def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

input_value = int(input("Enter a non-negative integer to calculate Fibonacci sequence: "))

fibonacci_result = fib(input_value)
print(f"Fibonacci({input_value}) = {fibonacci_result}")