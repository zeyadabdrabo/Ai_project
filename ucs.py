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

def ucs():
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, (x, y), path = heapq.heappop(pq)
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] == 0:
                    heapq.heappush(pq, (cost + 1, (nx, ny), path + [(nx, ny)]))

result = ucs()
print("UCS Path:", result)