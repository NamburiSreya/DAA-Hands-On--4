**prob 0 (que 1)**
Here's what I did:
I defined the function fib that takes a parameter n.
I implemented the base cases:
If n is 0, it returns 0
If n is 1, it returns 1
For all other cases, I used the recursive formula exactly as specified:
return fib(n - 1) + fib(n - 2)
To test the function, I added these lines:
python
input_value = int(input("Enter a non-negative integer to calculate Fibonacci sequence: "))

fibonacci_result = fib(input_value)
print(f"Fibonacci({input_value}) = {fibonacci_result}")

This prompts the user for input, calculates the Fibonacci number, and prints the result.
When I debugged the code for fib(5), I observed the following function call stack:
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
fib(2)
fib(1)
fib(0)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
This stack shows how the function breaks down the problem into smaller subproblems, calling itself recursively until it reaches the base cases.
I made sure to implement the return statement exactly as return fib(n - 1) + fib(n - 2) to ensure consistent results.

**prob 0 (que 2)** 
The time complexity of the original recursive Fibonacci implementation can be proven as follows:
Structure: Each fib(n) call generates two more recursive calls, creating a binary tree-like structure.
Growth pattern: At each recursion level, the number of function calls doubles, following a 2^n pattern.
Total calls: The sum of all function calls across the tree is proportional to 2^n.
Big-O notation: This exponential growth is expressed as O(2^n) time complexity.
Inefficiency: For larger n values, this leads to numerous redundant calculations, making the algorithm inefficient.
This analysis demonstrates why the naive recursive Fibonacci algorithm has exponential time complexity, explaining its poor performance for larger inputs.

**prob 0 (que 3)**
Improving the Fibonacci Implementation:
The current recursive Fibonacci algorithm has a major drawback: it becomes very slow for larger numbers due to its exponential time complexity. This happens because it repeats many calculations unnecessarily.
We can make it much faster by using smart techniques like memoization or dynamic programming. These methods work by remembering results we've already calculated, so we don't have to do the same work again.
For example, with memoization, we could use a dictionary or an array to store Fibonacci numbers we've already figured out. This way, if we need that number again, we can just look it up instead of recalculating it.
By using these techniques, we can dramatically speed up the algorithm. Instead of taking exponential time (O(2^n)), it could run in linear time (O(n)). This means it would work much better for bigger numbers, making the algorithm more practical and efficient.
