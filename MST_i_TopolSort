class Graph_M():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def topologicalSortPomoc(self, i, stack, visited):

        visited[i] = True

        for z in range(self.V):
            if self.graph[i][z] == 1:
                if visited[z] == False:
                    self.topologicalSortPomoc(z, stack, visited)

        stack.insert(0, i)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortPomoc(i, stack, visited)
        print(stack)

    def printMST(self, parent):
        print("Edge \tWeight")
        weight = 0
        for i in range(1, self.V):
            weight += self.graph[i][parent[i]]
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print(weight)

    def minKey(self, key, mstSet):

        min = 1001

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):

        key = [10000]*self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)



v = int(input("podaj liczbe wierzchołków"))
matrix = [0]*v
for i in range(v):
    matrix[i] = list(map(int, input().split()))

g = Graph_M(v)          # podaj ilosc wierzcholkow
g.graph = matrix           # tutaj macierz grafu
g.primMST()             # znajduje minimalne drzewo rozpinajace
g.topologicalSort()     # porządek topologiczny
