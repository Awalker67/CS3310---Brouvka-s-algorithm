import timeit

class Graph:

    def __init__(self, nodes):
        self.v = nodes # Indicates the number of nodes from parameter
        self.edges = [] #Initialize empy edges list
        self.component = {} #Initializes empty dictionary to store index a node's encompassing component

    def add_edge(self, u, v, weight):   #Function to add edge with connecting nodes and a weight
        self.edges.append([u, v, weight])    

    def find_component(self, u):  #Recursion to find component of node u until finding the node
        if self.component[u] == u:
            return u
        return self.find_component(self.component[u])

    def set_component(self, u):
        if self.component[u] == u:
            return
        else:
            for i in self.component.keys():     #Sets node for every unique component
                self.component[i] = self.find_component(i)


    def union(self, component, u, v):       #Method to unify two components into one given two nodes
        if component[u] <= component[v]:    #Checks if first component has less/equal nodes than the first
            self.component[u] = v           #Smaller components is added to the larger
            component[v] += component[u]    #Smaller components is added to the larger
            self.set_component(u)

        elif component[u] > component[v]:  #Else if first component has more nodes than the first
            self.component[v] = self.find_component(u)
            component[u] += component[v]
            self.set_component(v)

    def boruvka(self):
        component = []      #Initialize empty list of components
        weight = 0
        minimum_weight_edge = [-1] * self.v        #Initialize min edge with -1 by default

        for node in range(self.v):      #Find roots of components on both sides of the edge
            self.component.update({node: node})
            component.append(1)

        num_of_components = self.v

        print("---------------MST------------")
        while num_of_components > 1:
            for i in range(len(self.edges)):

                u = self.edges[i][0]
                v = self.edges[i][1]
                w = self.edges[i][2]

                u_component = self.component[u]
                v_component = self.component[v]

                if u_component != v_component:
                    # Checks if 1st edge's weight doesn't exist or is grather than 2nd edge's weight, then assign the 2nd weight to the 1st
                    if minimum_weight_edge[u_component] == -1 or minimum_weight_edge[u_component][2] > w:
                        minimum_weight_edge[u_component] = [u, v, w]
                    # Checks if 2nd edge's weight doesn't exist or is grather than 1st edge's weight, then assign the 1st weight to the second
                    if minimum_weight_edge[v_component] == -1 or minimum_weight_edge[v_component][2] > w:
                        minimum_weight_edge[v_component] = [u, v, w]

            for node in range(self.v):
                if minimum_weight_edge[node] != -1:     #Once minium weight edge is found, add the edge to the tree
                    u = minimum_weight_edge[node][0]
                    v = minimum_weight_edge[node][1]
                    w = minimum_weight_edge[node][2]

                    u_component = self.component[u]
                    v_component = self.component[v]

                    if u_component != v_component:
                        weight += w
                        self.union(component, u_component, v_component)
                        print("Added edge [" + str(u) + " - "
                              + str(v) + "]"
                              + " With weight: " + str(w))
                        num_of_components -= 1          #Reduce the total number of components when unionizing

            minimum_weight_edge = [-1] * self.v    #Set list back to -1 to reset
        print("----------------------------------")
        print("The total weight of the minimal spanning tree is: " + str(weight) +"\n")

start = timeit.default_timer()
g = Graph(6) 
g.add_edge(0, 1, 4) 
g.add_edge(0, 2, 4) 
g.add_edge(1, 2, 2) 
g.add_edge(2, 3, 3) 
g.add_edge(2, 4, 2) 
g.add_edge(2, 5, 4) 
g.add_edge(3, 5, 3) 
g.add_edge(4, 5, 3) 
g.boruvka()
stop = timeit.default_timer()
print('Time: ', (stop - start) * 5000 , "seconds")


start = timeit.default_timer()
g = Graph(9) 
g.add_edge(0, 1, 4) 
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2) 
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 8, 6)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 7)
g.boruvka()
stop = timeit.default_timer()
print('Time: ', (stop - start) * 5000 , "seconds")
