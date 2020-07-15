from linklist import LinkedList


class Graph:
    def __init__(self, vertices):
        # Total n of vertices:
        self.vertices = vertices
        # A list will contain linked lists for adjacency matrix
        self.array = []
        # Create a linked list for each vertex
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        # Complexity: O (1)
        # Add edge for directed graph
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_tail(destination)
            # for undirected graph:
            #self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(" Adjacency list of directed graph\n")
        print(" VERTICES : ", self.vertices)
        for i in range(self.vertices):
            print(" | ", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print(" None ")


a = Graph(6)
a.add_edge(0,1)
a.add_edge(0,2)

a.add_edge(1,3)
a.add_edge(1,4)
a.add_edge(2,5)
a.add_edge(4,5)
a.print_graph()
# print(a.array[0].get_head().data)

visited = []
que = []
def bfs(graph,source):
    visited.append(source)
    que.append(source)
    result = ""
    while que:
        elem = que.pop(0)
        temp = graph.array[elem].head
        result += str(elem)
        while temp:
            if temp.data not in visited:
                visited.append(temp.data)
                que.append(temp.data)
            temp=temp.next_element
    print(result)


bfs(a,0)
