"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("All your vertices are mine, or rather, do not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()

        # make a set to track which nodes we have visited
        visited = set()

        # enqueue the starting node
        q.enqueue(starting_vertex)

        # loop while the queue isn't empty
        while q.size() > 0:
            # dequeue, this is our current node
            current_node = q.dequeue()

            # check if we've yet visited
            if current_node not in visited:
                print(current_node)
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)

            ### get the neighbors
                neighbors = self.get_neighbors(current_node)
            ### iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a queue
        stack = Stack()

        # make a set to track which nodes we have visited
        visited = set()

        # push on the starting node
        stack.push(starting_vertex)

        # loop while the stack isn't empty
        while stack.size() > 0:
            # pop, this is our current node
            current_node = stack.pop()

            # check if we've yet visited
            if current_node not in visited:
                print(current_node)
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)

            ### get the neighbors
                neighbors = self.get_neighbors(current_node)
            ### iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        # need a base case

        # needs to call itself
        """
        if vertex not in visited:
            print(vertex)

            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return

            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        1. stop when we find the target node

        2. return the path we took to get there
        -  note, this will automatically be the shortest path

        Enqueue a PATH TO the starting node, instead of just the starting node
        """
        # make a queue
        q = Queue()

        # make a set to track which nodes we have visited
        visited = set()

        # enqueue the PATH TO the starting node
        q.enqueue([starting_vertex])

        # loop while the queue isn't empty
        while q.size() > 0:
            # dequeue, this is our current path
            current_path = q.dequeue()
            current_node = current_path[-1]

            # check if we have found our target node
            if current_node == destination_vertex:
                # then we are done! return
                return current_path

            # check if we've yet visited
            if current_node not in visited:
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)

            ### get the neighbors
                neighbors = self.get_neighbors(current_node)
            ### iterate over the neighbors, enqueue the PATH to them
                for neighbor in neighbors:
                    # path_copy = list(current_path)
                    # path_copy = current_path.copy()
                    # path_copy = copy.copy(current_path)
                    # path_copy = current_path[:]

                    # path_copy.append(neighbor)
                    path_copy = current_path + [neighbor]

                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        will not necessarily be the shortest path!!
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    starting_vertex: 1
    destination_vertex: 5

    q = Queue()
    visited = set()

    current_path = [1]
    current_node = current_path[-1]

    1: [1]
    2: [1, 2]
    3: [1, 2, 3]
    5: [1, 2, 3, 5]
    
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))