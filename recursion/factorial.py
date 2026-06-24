"""
Problem: Factorial (Recursion)
================================
Given n, return n! (n factorial) = n * (n-1) * ... * 1.
Base case: 0! = 1.

Interview Explanation:
    Factorial is the "Hello World" of recursion. Key insight: n! = n * (n-1)!
    Every recursive function needs: (1) base case to stop, (2) recursive case
    that moves toward the base case. Without a base case → infinite recursion.
    O(n) time, O(n) space (call stack depth).

Example:
    Input:  5
    Output: 120  (5 * 4 * 3 * 2 * 1)

Time Complexity:  O(n)
Space Complexity: O(n) - recursive call stack
"""


def factorial(n: int) -> int:
    """
    Recursive factorial.
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case


def factorial_iterative(n: int) -> int:
    """
    Iterative version — O(1) space (no call stack).
    Good to compare with recursive in interviews.
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    test_cases = [0, 1, 2, 5, 10, 12]

    print("=" * 50)
    print("Factorial (Recursive vs Iterative)")
    print("=" * 50)

    for n in test_cases:
        rec = factorial(n)
        itr = factorial_iterative(n)
        match = "✓" if rec == itr else "✗"
        print(f"{match} {n}! = {rec}")
