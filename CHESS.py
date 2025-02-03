from collections import deque


def knight(start, end):
    if start == end:
        return 0  # No moves needed if the positions are the same

    # Convert algebraic notation to numerical coordinates (0-based)
    def algebraic_to_numeric(pos):
        return ord(pos[0]) - ord('a'), int(pos[1]) - 1

    # All possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

    # Convert start and end positions to numerical coordinates
    start_x, start_y = algebraic_to_numeric(start)
    end_x, end_y = algebraic_to_numeric(end)

    # BFS setup
    queue = deque([(start_x, start_y, 0)])  # (x, y, moves)
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y, moves_count = queue.popleft()

        # Check all possible knight moves
        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if (nx, ny) == (end_x, end_y):
                return moves_count + 1  # Found the shortest path

            # Stay within the board and avoid revisiting positions
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                queue.append((nx, ny, moves_count + 1))
                visited.add((nx, ny))

    return -1  # This should never happen on a valid 8x8 board
