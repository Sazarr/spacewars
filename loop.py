class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def loop_size(node):
    visited = set()
    current = node

    # Step 1: Detect the loop and get the entry point
    while current not in visited:
        visited.add(current)
        current = current.next

    # Step 2: Measure the loop size
    loop_start = current  # Store the first node in the loop
    count = 1
    current = current.next

    while current != loop_start:
        count += 1
        current = current.next

    return count



class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def loop_size(node):
    visited = set()
    current = node

    while current not in visited:
        visited.add(current)
        current = current.next

    loop_start = current
    count = 1
    current = current.next

    while current != loop_start:
        count += 1
        current = current.next

    return count
