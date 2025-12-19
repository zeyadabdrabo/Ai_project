def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def hill_climbing():
    current = start
    path = [current]

    while current != goal:
        x, y = current
        neighbors = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] == 0:
                neighbors.append((nx, ny))

        if not neighbors:
            return None

        next_node = min(neighbors, key=lambda n: heuristic(n, goal))
        if next_node in path:
            return None

        current = next_node
        path.append(current)

    return path

result = hill_climbing()
print("Hill Climbing Path:", result)