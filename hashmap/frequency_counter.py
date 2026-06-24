"""
Problem: Frequency Counter
===========================
Given a list of elements, return a dictionary showing how many times
each element appears (its frequency).

Interview Explanation:
    A frequency counter is a core pattern used in many SDET and coding
    problems. It's the building block for anagram detection, duplicate
    finding, and test data validation. Build it using a HashMap where
    key = element, value = count.

Example:
    Input:  ["apple", "banana", "apple", "cherry", "banana", "apple"]
    Output: {"apple": 3, "banana": 2, "cherry": 1}

Time Complexity:  O(n)
Space Complexity: O(k) where k = number of unique elements

SDET Use Case:
    Counting how many times each test status appears in a test run result list.
    e.g., {"PASS": 45, "FAIL": 5, "SKIP": 2}
"""

from collections import Counter


def frequency_counter(items: list) -> dict:
    """
    Manual HashMap approach.
    Shows you know the underlying logic (important for interviews).
    """
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def frequency_counter_pythonic(items: list) -> dict:
    """
    Pythonic approach using collections.Counter.
    Preferred in production code — good to mention both in interviews.
    """
    return dict(Counter(items))


def most_frequent(items: list) -> tuple:
    """
    Returns the most frequent element and its count.
    """
    if not items:
        return (None, 0)
    freq = Counter(items)
    most_common = freq.most_common(1)[0]
    return most_common  # (element, count)


def elements_appearing_more_than_n_times(items: list, n: int) -> list:
    """
    SDET utility: find all elements appearing more than n times.
    Useful for finding duplicate test data, repeated API responses, etc.
    """
    freq = Counter(items)
    return [item for item, count in freq.items() if count > n]


if __name__ == "__main__":
    # General usage
    fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print("=" * 50)
    print("Frequency Counter")
    print("=" * 50)
    print(f"Input:  {fruits}")
    print(f"Frequency: {frequency_counter(fruits)}")
    print(f"Most Frequent: {most_frequent(fruits)}")
    print()

    # SDET use case: test run results
    test_results = ["PASS", "FAIL", "PASS", "PASS", "SKIP", "FAIL", "PASS"]
    print("SDET Use Case — Test Run Results:")
    print(f"Input:  {test_results}")
    freq = frequency_counter(test_results)
    print(f"Frequency: {freq}")
    print(f"Pass rate: {freq.get('PASS', 0)}/{len(test_results)}")
    print()

    # Elements appearing more than once
    nums = [1, 2, 3, 2, 1, 4, 5, 1]
    print(f"Elements appearing more than 1 time in {nums}:")
    print(elements_appearing_more_than_n_times(nums, 1))
