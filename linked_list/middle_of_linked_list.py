"""
Problem: Middle of the Linked List
=====================================
Given the head of a singly linked list, return the middle node.
If two middle nodes exist (even length), return the second one.

Interview Explanation:
    Brute force: traverse once to count length, traverse again to len//2.
    Two-pass, but requires knowing the length.
    Optimal: Slow/Fast pointer (Tortoise and Hare). Slow moves 1 step,
    fast moves 2 steps. When fast reaches end, slow is at the middle.
    O(n) time, O(1) space — single pass.

Example:
    Input:  1 → 2 → 3 → 4 → 5
    Output: Node with value 3

    Input:  1 → 2 → 3 → 4
    Output: Node with value 3 (second middle)

Time Complexity:  O(n)
Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def middle_of_linked_list(head: ListNode) -> ListNode:
    """
    Slow/Fast pointer approach — single pass.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next       # 1 step
        fast = fast.next.next  # 2 steps

    return slow  # Slow is at the middle when fast reaches the end


if __name__ == "__main__":
    print("=" * 50)
    print("Middle of Linked List (Slow/Fast Pointers)")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 3),
        ([1], 1),
        ([1, 2], 2),
    ]

    for values, expected_mid in test_cases:
        head = build_linked_list(values)
        mid = middle_of_linked_list(head)
        status = "✓" if mid.val == expected_mid else "✗"
        print(f"{status} List {values} → middle = {mid.val} (expected: {expected_mid})")
