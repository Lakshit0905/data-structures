"""
Problem: Valid Parentheses
===========================
Given a string containing only '(', ')', '{', '}', '[', ']',
determine if the input string is valid.

Rules:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Interview Explanation:
    Classic stack problem. Push opening brackets onto the stack.
    When we see a closing bracket, check if the top of the stack
    is the matching opening bracket. If not → invalid. If the stack
    is empty at the end → valid.
    O(n) time, O(n) space.

Example:
    Input:  "()[]{}"   → True
    Input:  "(]"       → False
    Input:  "([)]"     → False

Time Complexity:  O(n)
Space Complexity: O(n)

SDET Use Case:
    Validating that JSON/XML responses have properly matching brackets/tags.
"""


def is_valid_parentheses(s: str) -> bool:
    """
    Stack-based validation.
    """
    stack = []
    # Map closing bracket → its matching opening bracket
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)  # Push opening bracket
        elif char in ')}]':
            if not stack or stack[-1] != matching[char]:
                return False  # No matching opening bracket
            stack.pop()  # Matched! Remove from stack

    return len(stack) == 0  # Valid only if stack is empty


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("{", False),
        ("((()))", True),
    ]

    print("=" * 50)
    print("Valid Parentheses (Stack)")
    print("=" * 50)

    for s, expected in test_cases:
        result = is_valid_parentheses(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' → {result} (expected: {expected})")
