class graph:
    def __init__(self):
        self.graph = {}
        
    def edge(self,node,neighbor):
        self.graph[node] = neighbor
    
    def depth_first_serach(self,start_node,vist=None):
        if vist is None:
            vist = set()
        vist.add(start_node)
        print(start_node,end =" ")
        
        for all_other_node in self.graph[start_node]:
            if all_other_node not in vist:
                self.depth_first_serach(all_other_node,vist)
                
mygraph = graph()
mygraph.edge(1,[2,3])
mygraph.edge(2,[4,5])
mygraph.edge(3,[6,7])
mygraph.edge(4,[])
mygraph.edge(5,[8])
mygraph.edge(6,[])
mygraph.edge(7,[9])
mygraph.edge(8,[])
mygraph.edge(9,[])

mygraph.depth_first_serach(1)