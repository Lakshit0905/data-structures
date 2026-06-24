"""
Problem: Detect Cycle in Linked List
======================================
Given a linked list, determine if it has a cycle in it.

Interview Explanation:
    Floyd's Cycle Detection (Tortoise and Hare algorithm).
    Use two pointers: slow moves 1 step, fast moves 2 steps.
    If there's a cycle, fast will eventually lap slow → they meet.
    If no cycle, fast reaches None.
    O(n) time, O(1) space. Much better than using a HashSet (O(n) space).

Example:
    Input:  3 → 2 → 0 → -4 → (back to node with val 2)
    Output: True

Time Complexity:  O(n)
Space Complexity: O(1) Floyd's, O(n) HashSet approach
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle_floyds(head: ListNode) -> bool:
    """
    Floyd's Cycle Detection — O(1) space.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # Move 1 step
        fast = fast.next.next   # Move 2 steps

        if slow == fast:
            return True  # Cycle detected — they met!

    return False  # fast reached end → no cycle


def has_cycle_hashset(head: ListNode) -> bool:
    """
    HashSet approach — O(n) space.
    Store visited nodes; if we see a node again → cycle.
    Easier to understand but uses extra space.
    """
    seen = set()
    current = head
    while current:
        if id(current) in seen:
            return True
        seen.add(id(current))
        current = current.next
    return False


def build_cycle_list(values: list, cycle_pos: int) -> ListNode:
    """Helper: build a linked list with a cycle at cycle_pos (-1 = no cycle)."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


if __name__ == "__main__":
    print("=" * 50)
    print("Detect Cycle in Linked List (Floyd's Algorithm)")
    print("=" * 50)

    # Test with cycle: tail connects back to index 1
    head_cycle = build_cycle_list([3, 2, 0, -4], cycle_pos=1)
    print(f"List [3,2,0,-4] with cycle at pos 1 → has_cycle: {has_cycle_floyds(head_cycle)}")

    # Test without cycle
    head_no_cycle = build_cycle_list([1, 2, 3, 4], cycle_pos=-1)
    print(f"List [1,2,3,4] with no cycle → has_cycle: {has_cycle_floyds(head_no_cycle)}")

    # Single node, no cycle
    head_single = build_cycle_list([1], cycle_pos=-1)
    print(f"List [1] with no cycle → has_cycle: {has_cycle_floyds(head_single)}")
