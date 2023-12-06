class DisjointSet:
   def __init__(self, vertices):
       self.parent = {v: v for v in vertices}
       self.rank = {v: 0 for v in vertices}

   def find(self, v):
       if self.parent[v] != v:
           self.parent[v] = self.find(self.parent[v])
       return self.parent[v]

   def union(self, root1, root2):
       if self.rank[root1] < self.rank[root2]:
           self.parent[root1] = root2
       elif self.rank[root1] > self.rank[root2]:
           self.parent[root2] = root1
       else:
           self.parent[root2] = root1
           self.rank[root1] += 1


def kruskal(graph):
   min_spanning_tree = []
   disjoint_set = DisjointSet(graph['vertices'])

   edges = sorted(graph['edges'], key=lambda x: x[2])

   for edge in edges:
       src, dest, weight = edge
       root_src = disjoint_set.find(src)
       root_dest = disjoint_set.find(dest)

       if root_src != root_dest:
           min_spanning_tree.append(edge)
           disjoint_set.union(root_src, root_dest)

   return min_spanning_tree


def read_graph_from_file(file_name):
   vertices = set()
   edges = []

   with open(file_name, 'r') as file:
       for line in file:
           elements = line.split()
           if len(elements) == 3:
               src = int(elements[0])
               dest = int(elements[1])
               weight = int(elements[2])
               edges.append((src, dest, weight))
               vertices.add(src)
               vertices.add(dest)

   return {'vertices': list(vertices), 'edges': edges}

file_name = 'data.txt'
graph = read_graph_from_file(file_name)


min_spanning_tree = kruskal(graph)


print("Minimum Spanning Tree:")
for edge in min_spanning_tree:
   print(edge)