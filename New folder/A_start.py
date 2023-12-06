import heapq
import numpy as np

def astar(adj_matrix, cost_matrix, start, goal):
    num_vertices = len(adj_matrix)
    open_set = []  # Priority queue to store nodes and their costs
    heapq.heappush(open_set, (0, start))  # Start with a cost of 0 for the initial node

    g_scores = {node: float('inf') for node in range(num_vertices)}  # Cost from start to this node
    g_scores[start] = 0

    came_from = {}  # Map of nodes to their predecessors

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path

        for neighbor in range(num_vertices):
            if adj_matrix[current][neighbor] == 1:
                tentative_g_score = g_scores[current] + cost_matrix[current][neighbor]

                if tentative_g_score < g_scores[neighbor]:
                    came_from[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path from start to goal

def heuristic(node, goal):
    return 0

# Example adjacency matrix and cost matrix
adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

cost_matrix = np.array([
    [0, 4, 2, 0],
    [4, 0, 5, 10],
    [2, 5, 0, 8],
    [0, 10, 8, 0]
])

start_node = 0  # Start node index
goal_node = 3   # Goal node index

path = astar(adjacency_matrix, cost_matrix, start_node, goal_node)

if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(map(str, path))}")
else:
    print(f"No path from {start_node} to {goal_node} exists.")
