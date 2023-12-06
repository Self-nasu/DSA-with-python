import sys
import numpy as np
import time


def prim_mst(weight_matrix):
   num_nodes = len(weight_matrix)
   min_span_tree = [None] * num_nodes
   key = [sys.maxsize] * num_nodes   
   visited = [False] * num_nodes      

   key[0] = 0

   for _ in range(num_nodes):
       u = min_key(key, visited)
       visited[u] = True

       for v in range(num_nodes):
           if 0 < weight_matrix[u][v] < key[v] and not visited[v]:
               key[v] = weight_matrix[u][v]
               min_span_tree[v] = u

   return min_span_tree


def min_key(key, visited):
   min_val = sys.maxsize
   min_index = -1

   for v in range(len(key)):
       if key[v] < min_val and not visited[v]:
           min_val = key[v]
           min_index = v

   return min_index


def generate_random_weight_matrix(num_nodes):
   weight_matrix = np.random.randint(1, 100, size=(num_nodes, num_nodes))
   np.fill_diagonal(weight_matrix, 0)  # Diagonal elements set to 0
   return weight_matrix

num_nodes = 100
weight_matrix = generate_random_weight_matrix(num_nodes)

start_time = time.time()
min_spanning_tree = prim_mst(weight_matrix)
end_time = time.time()
time_taken = end_time - start_time
print(f"Time taken to find MST with {num_nodes} nodes: {time_taken:.6f} seconds")