from collections import deque
def knight(start, end):
    if start == end:
        return 0

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
                return moves_count + 1



            # Stay within the board and avoid revisiting positions
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                queue.append((nx, ny, moves_count + 1))
                visited.add((nx, ny))

    return -1

def knight(p1, p2):
    a, b = [('abcdefgh'.index(p[0]), int(p[1])) for p in [p1, p2]]
    x, y = sorted((abs(a[0] - b[0]), abs(a[1] - b[1])))[::-1]

    if (x, y) == (1, 0): return 3
    if (x, y) == (2, 2) or ((x, y) == (1, 1) and any(p in ['a1', 'h1', 'a8', 'h8'] for p in [p1, p2])): return 4

    delta = x - y

    return delta - 2 * ((delta - y) // (3 if y > delta else 4))


from collections import deque
moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

def knight(p1, p2):
    x, y = ord(p2[0])-97, int(p2[1])-1
    left, seen = deque([(ord(p1[0])-97, int(p1[1])-1, 0)]), set()
    while left:
        i, j, v = left.popleft()
        if i==x and j==y: return v
        if (i, j) in seen: continue
        seen.add((i, j))
        for a,b in moves:
            if 0 <= i+a < 8 and 0 <= j+b < 8:
                left.append((i+a, j+b, v+1))


