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
            self.array[source].insert_at_head(destination)
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


a = Graph(3)
a.add_edge(0,1)
a.add_edge(0,2)
a.print_graph()
print(a.array[0].get_head().data)

