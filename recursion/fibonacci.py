"""
Problem: Fibonacci Number
==========================
Return the nth Fibonacci number.
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

Interview Explanation:
    Naive recursion is O(2^n) — exponential due to repeated subproblems.
    Memoization (top-down DP) stores computed results → O(n) time, O(n) space.
    Iterative (bottom-up DP) is O(n) time, O(1) space — the best solution.
    Always discuss all three approaches in interviews!

Example:
    Input:  10
    Output: 55

Time Complexity:
    Naive:    O(2^n)
    Memo:     O(n)
    Iterative: O(n)
Space Complexity:
    Naive:    O(n) call stack
    Memo:     O(n)
    Iterative: O(1)
"""


def fib_naive(n: int) -> int:
    """
    Naive recursion — exponential time. DO NOT use for large n.
    Only show this to explain the problem before optimizing.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n: int, memo: dict = None) -> int:
    """
    Top-down memoization. O(n) time, O(n) space.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_iterative(n: int) -> int:
    """
    Bottom-up iterative. O(n) time, O(1) space. Best solution!
    """
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    print("=" * 50)
    print("Fibonacci — Three Approaches")
    print("=" * 50)

    for n in [0, 1, 5, 10, 20]:
        result = fib_iterative(n)
        print(f"F({n}) = {result}")

    print("\nFirst 10 Fibonacci numbers:")
    print([fib_iterative(i) for i in range(10)])
