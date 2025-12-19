import heapq

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

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        f, (x, y), path = heapq.heappop(pq)
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] == 0:
                    g = len(path) + 1
                    h = heuristic((nx, ny), goal)
                    heapq.heappush(pq, (g + h, (nx, ny), path + [(nx, ny)]))

result = astar()
print("A* Path:", result)