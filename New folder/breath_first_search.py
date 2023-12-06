from collections import deque

class graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self,main_node,childs):
        self.graph[main_node] = childs
        
    def breadth_first_search(self,start):
        # for starting node we put in dequeu and visted
        visted = set()
        myqueue = deque([start])
        visted.add(start)
        
        while myqueue: # this while will run untill the the queue has element in it
            # we have to pop the double ended queue as it is now processed
            outed_element = myqueue.popleft()
            print(outed_element, end=" ")
            
            # after we poped on element from queue we added its child element in the queue
            #  also  we added them in visted
            for childs in self.graph[outed_element]: 
                if childs not in visted:
                    myqueue.append(childs)
                    visted.add(childs)
                
my_graph = graph()
my_graph.add_edge(1, [2, 3])
my_graph.add_edge(2, [4, 5])
my_graph.add_edge(3, [6])
my_graph.add_edge(4, [])
my_graph.add_edge(5, [7, 8])
my_graph.add_edge(6, [])
my_graph.add_edge(7, [])
my_graph.add_edge(8, [])
# Performing BFS starting from node 1
print("Breadth-First Search:")
my_graph.breadth_first_search(1)