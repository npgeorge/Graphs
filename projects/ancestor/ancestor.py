class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

#def getNeighbors()


def earliest_ancestor(ancestors, starting_node, distance=0):
    """
    Goal:
    Write a function that, given the dataset and 
    the ID of an individual in the dataset, returns 
    their earliest known ancestor – the one at the 
    farthest distance from the input individual.

    Conditions:
    If there is more than one ancestor tied 
    for "earliest", return the one with the 
    lowest numeric ID. If the input individual 
    has no parents, the function should return -1.

    1. Describe the problem in graphs terms
    - What are our nodes?
    - What are our edges? aka when are two nodes connected?

    -- Is this a directed or undirected graph? Cyclic or acyclic?


    - find earliest known ancestor, the one furthest from input individual
    - this is a DFS(Depth First Search problem)

    DAG: directed acyclic graph, from parent to child or from child to parent

    2. Build graph or write getNeighbors function

    3. Choose your fighter / which algorithm to use
    """
    
    # define the stack from the class above
    s = Stack()
    
    # initialize empty visited nodes set
    visited = set()

    #neighbor = visited[starting_node]

    # make a path with the start node pushed in
    s.push([starting_node])

    # now lets search in a while loop
    while s.size() > 0:
        
        # whatever is at the end of the line
        # lets pop it out and save it as the current_path
        current_path = s.pop()

        #whatver is last in the path is the current node
        current_node = current_path[-1]

        # stop if the entered node is already the furthest path
        if current_node == starting_node:
            return current_path

        # lets check if we've been here before
        if current_node not in visited:
            visited.add(current_node)

            neighbors = getNeighbors(current_node)

            for neighbor in neighbors:

                path_copy = list(current_path)

                path_copy.append(neighbor)

                s.push(path_copy)


# in class

# run a standard DFT, but recurse with distance to track the earliest ancestor found
def dft(ancestors, starting_node, distance):
    # because it is a directed acyclic graph
    # you can only traverse one way
    # so you don't need to track if you've visited a node or not

    parents = getNeighbors(node)

    # recurse all the way down to the end until we hit the earliest ancestor on that path
    if len(parents) == 0:
        return (node, distance)

    ancient_one = (node, distance)

    for parent in parents:
        node_pair = dft(ancestors, parent, distance + 1)

        if node_pair[1] > distance:
            ancient_one = node_pair

    return ancient_one

def earliest_ancestor(ancestors, starting_node, distance=0):
    # call BFT or DFT

    # if the earliest ancestor returned is the same as the starting node, return -1
