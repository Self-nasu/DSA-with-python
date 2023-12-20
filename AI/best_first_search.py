from queue import PriorityQueue

class graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self,node,padosi): # entry format [1,[(2,4),(3,2)]] in this 1 is main node with two child 2 and 3
        # and there cost as 4 and 2
        self.graph[node] = padosi
        
    def best_first_search(self,start,goal):
        visited = set()
        myqueue = PriorityQueue()
        myqueue.put((0,start))
        
        while not myqueue.empty():
            cost,node = myqueue.get() # last inserted element of the queue
            
            if node not in visited: # chacking if the node we are going is visted or not
                print(node,end="-->")
                visited.add(node)
                
            if node == goal: # cheching the node we are at is goal node or not
                break
            
            for childs,cost in self.graph[node]: # now using this for loop untill we vist all the node
                if childs not in visited: # if the child is visted or not is not then put it in queue
                    myqueue.put((cost,childs))
                    
                    
mygraph = graph()
mygraph.add_edge(1,[(2,4),(3,2)])
mygraph.add_edge(2,[(4,5),(5,8)])
mygraph.add_edge(3,[(6,3)])
mygraph.add_edge(4,[])
mygraph.add_edge(5,[(7,6),(8,7)])
mygraph.add_edge(6,[])
mygraph.add_edge(7,[])
mygraph.add_edge(8,[])

mygraph.best_first_search(1,2)