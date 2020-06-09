from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class bfss:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addGraph(self):
        macierz = []
        s = input().split()
        while (len(s) != 0):
            s = list(map(int, s))
            macierz.append(s)
            s = input().split()
            # print(macierz)

        # print(macierz)
        for i in range(len(macierz[0])):
            for j in range(len(macierz[0])):
                # print(f"i: {i} j: {j}")
                if macierz[i][j] == 1 and i != j:
                    # print(f"#{i} {j}")
                    self.addEdge(i, j)
        print("DFS:")
        self.DFS()
        print("\nBFS:")
        self.BFS()

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end = ' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        v = 0
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph)+1)

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
    def BFS(self):
        s = 0
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
