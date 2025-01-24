class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def loop_size(node):
    slow = fast = node

    # Step 1: Detect the loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0  # No loop

    # Step 2: Find the loop entry
    slow = node  # Reset slow to head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Count the loop size
    loop_count = 1
    current = slow.next
    while current != slow:
        loop_count += 1
        current = current.next

    return loop_count





