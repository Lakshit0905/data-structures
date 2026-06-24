"""
Problem: Reverse a Linked List
================================
Reverse a singly linked list.

Interview Explanation:
    Use three pointers: prev, current, next_node.
    At each step: save next, reverse the link, advance both pointers.
    After the loop, prev points to the new head.
    O(n) time, O(1) space.

Example:
    Input:  1 → 2 → 3 → 4 → 5 → None
    Output: 5 → 4 → 3 → 2 → 1 → None

Time Complexity:  O(n)
Space Complexity: O(1) iterative, O(n) recursive
"""


class ListNode:
    """Singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: list) -> ListNode:
    """Helper: build a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode) -> list:
    """Helper: convert linked list to Python list for easy printing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Iterative reversal using three pointers.
    """
    prev = None
    current = head

    while current:
        next_node = current.next   # Save next node
        current.next = prev        # Reverse the link
        prev = current             # Advance prev
        current = next_node        # Advance current

    return prev  # prev is now the new head


def reverse_linked_list_recursive(head: ListNode) -> ListNode:
    """
    Recursive reversal. O(n) space due to call stack.
    """
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    print("=" * 50)
    print("Reverse Linked List")
    print("=" * 50)

    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]

    for values in test_cases:
        head = build_linked_list(values)
        original = linked_list_to_list(head)

        reversed_head = reverse_linked_list(head)
        result = linked_list_to_list(reversed_head)

        print(f"Input:  {original}")
        print(f"Output: {result}")
        print("-" * 30)
